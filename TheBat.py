@echo off
:monitor
timeout /t 2 /nobreak > nul
set "ESP32_PORT=COM6"
for /f "tokens=2 delims==" %%I in ('wmic path Win32_SerialPort Get DeviceID^,PNPDeviceID /format:list ^| find "VID_XXXX&PID_XXXX"') do set "ESP32_PORT=%%I"
if not "%ESP32_PORT%"=="" (
    echo ESP32 conectado em %ESP32_PORT%
    start "" /b python script.py
) else (
    taskkill /f /im python.exe 2>nul
    echo ESP32 desconectado
)
goto :monitor