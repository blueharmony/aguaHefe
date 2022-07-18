### setup the python environment
#set -x
#which python
#which python3

echo ""
echo "Patience, setting up the Python environment..."

if [ -d ".venv" ]; then
    echo "venv environment exists"
else
    python3 -m venv .venv
fi

# Winders versus Linux
if [ -e ".venv/scripts/activate" ]; then
    source .venv/scripts/activate
else
    chmod .venv/bin/activate
    source .venv/bin/activate
fi

set -x
pip3 install -r requirements.txt

export FLASK_APP="src.webapp"
export FLASK_ENV="development"

### run the bugger
python -m flask run

set +x
