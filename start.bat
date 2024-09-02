@echo off

if not exist "venv" (
    python -m venv venv
    echo Środowisko wirtualne utworzone.
)

call venv\Scripts\activate
echo Środowisko wirtualne aktywowane.

REM Instalacja zależności
pip install -r requirements.txt

set FLASK_APP=run.py
set FLASK_ENV=development

flask db init
flask db migrate
flask db upgrade

flask run

deactivate