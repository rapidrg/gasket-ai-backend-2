# Gasket AI Backend

A simple Flask API that accepts an uploaded trading card image and returns a mock gasket color match result.

## API

- `POST /analyze-card` — Upload an image using the key `cardImage`.

## To run locally

```bash
pip install -r requirements.txt
python app.py
```

## Deployment

You can deploy this app to platforms like Render using:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
