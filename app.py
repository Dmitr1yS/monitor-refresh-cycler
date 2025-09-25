import tkinter as tk
from tkinter import messagebox
import sys
import ctypes

try:
    import win32api
    import win32con
except ImportError:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Import Error", "The pywin32 library was not found.\nPlease install it using the command: pip install pywin32")
    sys.exit()


class RefreshRateChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Refresh Rate Cycler")

        self.monitors_info = self.get_available_monitors()
        if not self.monitors_info:
            messagebox.showwarning("Warning", "No monitors found with two or more available refresh rates at the current resolution.")
        
        self.monitor_vars = []
        self.running = False
        self.after_id = None

        self.create_widgets()

    def get_available_monitors(self):
        monitors = {}
        
        DISPLAY_DEVICE_ACTIVE = 1  

        try:
            i = 0
            while True:
                device = win32api.EnumDisplayDevices(None, i, 0)
                if device.StateFlags & DISPLAY_DEVICE_ACTIVE:
                    current_settings = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
                    
                    available_rates = set()
                    
                    j = 0
                    while True:
                        try:
                            settings = win32api.EnumDisplaySettings(device.DeviceName, j)
                            if (settings.PelsWidth == current_settings.PelsWidth and
                                settings.PelsHeight == current_settings.PelsHeight):
                                available_rates.add(settings.DisplayFrequency)
                            j += 1
                        except win32api.error:
                            break 
                    
                    if len(available_rates) > 1:
                        monitors[device.DeviceName] = {
                            "device": device,
                            "original_settings": current_settings,
                            "rates": sorted(list(available_rates))
                        }
                i += 1
        except win32api.error:
            pass
        return monitors

    def create_widgets(self):
        monitor_frame = tk.LabelFrame(self.root, text="Select Monitors (to cycle refresh rate)")
        monitor_frame.pack(padx=10, pady=10, fill="x")

        if not self.monitors_info:
            tk.Label(monitor_frame, text="No suitable monitors found.").pack()

        for device_name, info in self.monitors_info.items():
            var = tk.BooleanVar()
            rates_str = ", ".join(f"{rate}Hz" for rate in info['rates'])
            label_text = f"Display {info['device'].DeviceString} ({rates_str})"
            
            self.monitor_vars.append({"var": var, "name": device_name})
            
            cb = tk.Checkbutton(monitor_frame, text=label_text, variable=var)
            cb.pack(anchor="w")

        interval_frame = tk.Frame(self.root)
        interval_frame.pack(padx=10, pady=5, fill="x")
        tk.Label(interval_frame, text="Interval (seconds):").pack(side="left")
        self.interval_entry = tk.Entry(interval_frame, width=10)
        self.interval_entry.insert(0, "4")
        self.interval_entry.pack(side="left")

        separator = tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill="x", padx=5, pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=10, pady=10)
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_toggling)
        self.start_button.pack(side="left", padx=5)
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_toggling, state=tk.DISABLED)
        self.stop_button.pack(side="left", padx=5)
        
        if not self.monitors_info:
            self.start_button.config(state=tk.DISABLED)

    def start_toggling(self):
        if self.running: return
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.toggle_refresh_rate()

    def stop_toggling(self):
        if not self.running: return
        self.running = False
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        
        for monitor in self.monitor_vars:
            if monitor["var"].get():
                device_name = monitor["name"]
                original_settings = self.monitors_info[device_name]["original_settings"]
                try:
                    win32api.ChangeDisplaySettingsEx(device_name, original_settings, 0)
                except win32api.error as e:
                    print(f"Failed to restore original settings for {device_name}: {e}")
        
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def toggle_refresh_rate(self):
        if not self.running: return

        for monitor in self.monitor_vars:
            if monitor["var"].get():
                device_name = monitor["name"]
                info = self.monitors_info[device_name]
                available_rates = info["rates"]
                
                current_settings = win32api.EnumDisplaySettings(device_name, win32con.ENUM_CURRENT_SETTINGS)
                current_rate = current_settings.DisplayFrequency
                
                try:
                    current_index = available_rates.index(current_rate)
                    next_index = (current_index + 1) % len(available_rates)
                    next_rate = available_rates[next_index]
                except ValueError:
                    next_rate = available_rates[0]

                new_settings = current_settings
                new_settings.DisplayFrequency = next_rate
                
                try:
                    win32api.ChangeDisplaySettingsEx(device_name, new_settings, 0)
                except win32api.error as e:
                    messagebox.showerror("Error", f"Failed to change refresh rate for {device_name}.\n\n{e}")
                    self.stop_toggling()
                    return

        try:
            interval_ms = int(float(self.interval_entry.get()) * 1000)
            self.after_id = self.root.after(interval_ms, self.toggle_refresh_rate)
        except ValueError:
            messagebox.showerror("Error", "Invalid interval format. Please enter a number.")
            self.stop_toggling()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Administrator Rights Required", "Please restart the script with administrator privileges.")
        root.destroy()
        sys.exit()

    root = tk.Tk()
    app = RefreshRateChangerApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (app.stop_toggling(), root.destroy()))
    root.mainloop()