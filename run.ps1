if (-not (Test-Path -Path .venv)) {
    python -m venv .venv
}

./.venv/Scripts/Activate

pip install -r requirements.txt

python main.py

Deactivate