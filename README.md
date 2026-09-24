# Campus Connect

Plateforme universitaire Django pour étudiants.

## Architecture

- `frontend/` : templates HTML + CSS
- `core/` : logique métier, modèles, vues et administration
- `backend/` : configuration Django
- `db.sqlite3` : base locale créée après migration
- `manage.py` : point d'entrée Django à la racine (important pour Vercel)

## Lancer localement

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Puis ouvre http://127.0.0.1:8000/

Administration : http://127.0.0.1:8000/admin/

## Déploiement Vercel

Le projet est volontairement structuré avec `manage.py` à la racine. Vercel détecte actuellement Django directement et ne demande plus obligatoirement un `vercel.json` ou un dossier `/api` pour un projet Django standard.

Avant le premier déploiement, configure dans Vercel :
- `DJANGO_SECRET_KEY` = une vraie clé secrète
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = `.vercel.app` (ou ton domaine)

La base locale SQLite est uniquement pour le développement. Pour la production, configure `DATABASE_URL` avec une base MySQL en ligne.

## Base de données

Le code utilise SQLite automatiquement si `DATABASE_URL` n'est pas défini.

Quand tu seras prêt à mettre MySQL en ligne, nous configurerons `DATABASE_URL` dans Vercel et lancerons les migrations.

## Important

Ne mets jamais ton vrai mot de passe MySQL ou ta vraie clé Django dans GitHub.
Utilise les variables d'environnement de Vercel.
