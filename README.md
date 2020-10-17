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

#### Deploy to Google App Engine Standard
```bash
gcloud app deploy app.yaml
```