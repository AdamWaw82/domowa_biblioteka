#!/bin/bash
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "Środowisko wirtualne utworzone."
fi
source venv/bin/activate
echo "Środowisko wirtualne aktywowane."

pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade

flask run

deactivate
