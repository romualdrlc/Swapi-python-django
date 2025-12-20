FROM python:3.14

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copier uniquement les dépendances (cache Docker efficace)
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Collecte des fichiers statiques (si activée)
RUN python manage.py collectstatic --noinput

# Lancement Django via Gunicorn
CMD ["gunicorn", "star_wars_api.wsgi:application", "--bind", "0.0.0.0:8000"]
