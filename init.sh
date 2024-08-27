sudo apt update
sudo apt -y install python3-pip
sudo apt -y install postgresql postgresql-contrib

pip3 install psycopg2
pip3 install tornado
pip3 install -U spacy==3.7.5
python3 -m spacy download en_core_web_sm
python3 -m spacy download ru_core_news_sm
