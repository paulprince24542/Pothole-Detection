@echo off
echo Starting Django development server...
echo.

REM Navigate to the directory of your Django project
cd /d "D:\Pothole-Detection\server\pothole_ui"

REM Activate the virtual environment if necessary
call conda activate pothole

REM Start the Django development server
python manage.py runserver

echo Django development server has been started.
pause