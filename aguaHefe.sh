### setup the python environment
# python -m venv .venv
if test -f ".venv/scripts/activate"; then
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
