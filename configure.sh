

if test -d "venv"; then
    echo "Venv exists."
else
    echo "Venv does not exist."
    python -m venv venv
    echo "Venv created."
    source venv/bin/activate
    pip install -r requirements.txt
fi