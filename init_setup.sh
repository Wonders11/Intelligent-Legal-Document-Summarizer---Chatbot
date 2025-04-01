echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.10 version" 


conda create --prefix ./legal_ai_project python=3.10 -y


echo [$(date)]: "activating the environment" 

source activate ./legal_ai_project

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 