source .venv/bin/activate
pip install -r necessary-requirements-to-run.txt --timeout 10000
if ! [[ -d "models" ]]; then
    if ! [[ -f "models.zip" ]]; then
        gdown 1ujSYC3tEC3VNoxqUIWO2PG7Lg5HAdYqn
    fi
    unzip models.zip
fi
python3 app.py
