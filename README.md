# Gasket AI Backend with Color Detection

This backend extracts dominant colors from a trading card image to suggest matching gasket colors.

## API

- `POST /analyze-card` — Upload an image using the key `cardImage`

## To run locally

```bash
pip install -r requirements.txt
python app.py
```

## Deployment

Use Render:
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
