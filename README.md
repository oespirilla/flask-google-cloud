

# DEMO Flask application for Cloud Run

## Local Environment

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

## Deploy to Cloud Run
First you need to build a container, we are going to use GCR (Google Container Registry) to store our container image:

#### Create a Docker Image
Run the following command replacing the PROJECT_ID variable with your Google Cloud Project Id, this is going to create a Docker Image based on your Dockerfile:
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/my-app
```
Ok, now you have a Docker image in your container registry. Let's use this image to deploy it to Cloud Run
```bash
gcloud run deploy --image gcr.io/PROJECT_ID/my-app --platform managed

```
Now go to your Google Cloud Console and under Cloud Run, you will see a service called "my-app".

