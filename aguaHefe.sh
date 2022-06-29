### setup the python environment
# python -m venv .venv
source .venv/scripts/activate

set -x
pip install -r requirements.txt

export FLASK_APP="src.webapp"
export FLASK_ENV="development"

### run the bugger
python -m flask run

set +x