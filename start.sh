source .venv/bin/activate
pip install -r necessary-requirements-to-run.txt --timeout 10000
gdown 1ujSYC3tEC3VNoxqUIWO2PG7Lg5HAdYqn
unzip models.zip
python3 app.py
