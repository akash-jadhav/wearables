# wearables

# mac

export PY_PATH="$(brew --prefix python@3.9)/bin"
export virtualenv_command="${PY_PATH}/python3.9 -m venv venv"
eval $virtualenv_command
source $(pwd)/venv/bin/activate

# windows

To create venv
python -m venv venv

To activate:
.\venv\Scripts\activate
