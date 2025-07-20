# ⛈️ Vigilance Météo Villes - Backend

Backend API application built with [FastAPI](https://fastapi.tiangolo.com/).
Backend for the ["vigilance-meteo-villes-front"](https://github.com/paulcharayron/vigilance-meteo-villes-front) frontend app.

---

## 📦 Features

- ⚡️ FastAPI — high-performance web framework
- 📄 OpenAPI & ReDoc auto-generated docs

- Provides an interface to access the public vigilance data from Météo France's APIs
- Exposes french departments flags files for a pretty display on the frontend

---

## 🚀 Getting Started locally

### 1. Clone & install dependencies

```bash
git clone https://github.com/paulcharayron/vigilance-meteo-villes-back.git
cd vigilance-meteo-villes-back
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the app

```bash
cd app
fastapi dev main.py
```
