@echo off
title EduVision DV - Power BI Dashboard Launcher
echo ====================================================================
echo             Launching EduVision DV in Power BI Desktop
echo ====================================================================
echo.
echo Target File: %~dp0dashboard\EduVision_DV.pbip
echo.

if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\PBIDesktopStore.exe" (
    start "" "%LOCALAPPDATA%\Microsoft\WindowsApps\PBIDesktopStore.exe" "%~dp0dashboard\EduVision_DV.pbip"
) else (
    start "" "%~dp0dashboard\EduVision_DV.pbip"
)

echo Dashboard launch command sent to Power BI Desktop.
timeout /t 3 >nul
exit
