@echo off

if not exist "venv" (
    python -m venv venv
    echo Środowisko wirtualne utworzone.
)

call venv\Scripts\activate
echo Środowisko wirtualne aktywowane.

REM Instalacja zależności
pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade

flask run

deactivate