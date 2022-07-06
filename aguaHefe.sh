### setup the python environment

if [ -d ".venv" ]; then
    echo "venv environment exists"
else
    python -m venv .venv
fi

# Winders versus Linux
if [ -e ".venv/scripts/activate" ]; then
    source .venv/scripts/activate
else
    chmod .venv/bin/activate
    source .venv/bin/activate
fi

set -x
pip install -r requirements.txt

export FLASK_APP="src.webapp"
export FLASK_ENV="development"

### run the bugger
python -m flask run

set +x
