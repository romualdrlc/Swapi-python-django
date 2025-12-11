# Star Wars API Django

## Installation

1. Cloner le dépôt :

```bash
git clone https://ton-repo.git
cd ton-projet
```

2. Créer un environnement virtuel Python et l'activer :

```bash
Copier le code
python3 -m venv venv
source venv/bin/activate # sur Windows : venv\Scripts\activate
```

3. Installer les dépendances :

```bash
Copier le code
pip install -r requirements.txt
```

4. Configurer les variables d'environnement (si tu utilises .env ou autre) :

```bash
Copier le code
cp .env.example .env
```

# puis éditer .env avec ta config

5. Appliquer les migrations de la base de données :

```bash
Copier le code
python manage.py migrate
```

6. (Optionnel) Créer un super-utilisateur admin :

```bash
Copier le code
python manage.py createsuperuser
```

7. Lancer le serveur de développement :

```bash
Copier le code
python manage.py runserver
```

8. Ouvrir le navigateur à l’adresse :

```bash
http://127.0.0.1:8000/
```
