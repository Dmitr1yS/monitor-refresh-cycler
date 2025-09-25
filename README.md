
# Monitor Refresh Rate Cycler

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Windows utility to periodically cycle the refresh rate of selected monitors. This can be useful for "rebooting" the video signal for older or problematic monitors that may occasionally lose connection or display artifacts.


*(This is an example screenshot. You should create your own and replace this link!)*

## Why Use This?

This tool can help force a "re-sync" of the video signal for monitors that occasionally lose connection or show glitches. Changing the refresh rate forces the GPU to re-initialize the connection without the need to physically unplug the cable.

## ✨ Features

-   Auto-detects connected monitors and their available refresh rates for the current resolution.
-   A simple GUI to select one or more monitors to cycle.
-   Customizable switching interval in seconds.
-   Safely restores the original refresh rate when the application is closed.

## ⚠️ Requirements

-   Windows 10 / 11
-   Python 3.x (for running from source)
-   **Administrator Privileges are required** to run this application, as it needs permission to change system display settings.

## ⚙️ How to Run from Source

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Dmitr1yS/monitor-refresh-cycler.git
    cd monitor-refresh-cycler
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the script with Administrator rights:**
    Right-click on your terminal (PowerShell, CMD) and select "Run as administrator", then run:
    ```bash
    python app.py
    ```

## 🚀 How to Build the `.exe`

If you want to compile your own standalone executable:

1.  Ensure PyInstaller is installed:
    ```bash
    pip install pyinstaller
    ```
2.  Run the build command from the project directory:
    ```bash
    python -m PyInstaller --onefile --windowed --hidden-import=win32timezone --name="Monitor Cycler" --icon="icon.ico" app.py
    ```
3.  The finished `Monitor Cycler.exe` will be in the `dist` folder. Remember to run it **as an Administrator**.

## 📥 Downloads

A pre-compiled, ready-to-use version of this application can be found on the [**Releases**](https://github.com/Dmitr1yS/monitor-refresh-cycler/releases) page.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Русский

# Утилита для циклической смены герцовки монитора

[![Лицензия: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Простая утилита для Windows, которая периодически переключает частоту обновления (герцовку) выбранных мониторов. Это может быть полезно для «перезагрузки» видеосигнала на старых или проблемных мониторах, которые могут терять соединение или отображать артефакты.


*(Это пример скриншота. Вам следует сделать свой и заменить эту ссылку!)*


## 🎯 Назначение

Эта утилита помогает принудительно "пересинхронизировать" видеосигнал для мониторов, которые периодически теряют соединение или показывают сбои. Смена частоты обновления заставляет видеокарту заново инициализировать подключение без необходимости физически отключать кабель.

## ✨ Возможности

-   Автоматическое определение подключенных мониторов и доступных для них частот обновления при текущем разрешении.
-   Простой графический интерфейс для выбора одного или нескольких мониторов.
-   Настраиваемый интервал переключения в секундах.
-   Безопасное восстановление исходной герцовки при закрытии программы.

## ⚠️ Требования

-   Windows 10 / 11
-   Python 3.x (для запуска из исходного кода)
-   **Права Администратора** для запуска. Это необходимо для изменения системных настроек дисплея.

## ⚙️ Установка и запуск из исходников

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Dmitr1yS/monitor-refresh-cycler.git
    cd monitor-refresh-cycler
    ```
2.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Запустите скрипт от имени Администратора:**
    Нажмите правой кнопкой мыши на терминал (PowerShell, CMD), выберите "Запуск от имени администратора", а затем выполните:
    ```bash
    python app.py
    ```

## 🚀 Сборка `.exe` файла

Если вы хотите скомпилировать собственный `.exe` файл:

1.  Убедитесь, что PyInstaller установлен:
    ```bash
    pip install pyinstaller
    ```
2.  Выполните команду сборки из папки проекта:
    ```bash
    python -m PyInstaller --onefile --windowed --hidden-import=win32timezone --name="Monitor Cycler" --icon="icon.ico" app.py
    ```
3.  Готовый файл `Monitor Cycler.exe` будет находиться в папке `dist`. Не забудьте запускать его **от имени Администратора**.

## 📥 Готовая версия

Скомпилированную, готовую к использованию версию программы можно найти на странице [**Релизов**](https://github.com/Dmitr1yS/monitor-refresh-cycler/releases).

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).