# Gasket AI Backend with Optimized Pillow Color Detection

This backend uses Pillow to extract dominant colors from a trading card image, resized for low memory usage on Render.

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
