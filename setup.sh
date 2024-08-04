VENV_DIR="/home/jangwon/PycharmProjects/writingAI"

python3.10 -m venv $VENV_DIR/venv

# activate the VENV
source $VENV_DIR/venv/bin/activate

## pip install
#pip install -r requirements.txt

# export python root dir (needed for import)
export PYTHONPATH=${VENV_DIR}
                                                                                                      
# install pip
pip install Flask requests streamlit openai beautifulsoup4
