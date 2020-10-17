## Development

##### DEMO Flask application

#### Install virtualenv
```bash
python3 -m pip install virtualenv
```

#### Create virtualenv
```bash
python3 -m virtualenv -p python3 venv
```

#### Activate virtualenv
```bash
source venv/Scripts/activate
```

#### Install requirements
```bash
pip install -r requirements.txt
```

#### Run
```bash
python main.py
```
#### Deploy to Google Cloud Functions
```bash
gcloud functions deploy dog --entry-point random_dog --runtime python38 --trigger-http --allow-unauthenticated
gcloud functions deploy doglist --entry-point list_dog --runtime python38 --trigger-http --allow-unauthenticated
```