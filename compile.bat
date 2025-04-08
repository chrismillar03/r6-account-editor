@echo off

if not exist .venv (
	python -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip > nul
pip install -r requirements.txt > nul
py compile.py
call .venv\Scripts\deactivate.bat
