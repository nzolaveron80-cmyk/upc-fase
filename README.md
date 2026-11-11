# Site FASE · UPC — Django + SQLite

## 1. Installation locale

```bash
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser   # votre compte administrateur
python manage.py runserver
```

Ouvrez http://127.0.0.1:8000 (site) et http://127.0.0.1:8000/admin (administration).

## 2. Gestion du contenu

Tout se fait dans l'administration Django :
- **Configuration du site** : nom, devise, présidente, mot, coordonnées.
- **Citations d'accueil** : trois citations maximum affichées.
- **Promotions** et **délégués** (chef et adjoint) : inlines dans la promotion.
- **Responsables** : classés par catégorie (décanat, gouvernement, départements…).
- **Cours** et leurs **fichiers** (inline).
- **BAT et exercices**.
- **Actualités** : action « Archiver » (retire de l'accueil et crée une archive) et « Restaurer sur l'accueil ».
- **Archives** avec album photo (inline).
- **Marketplace**.

## 3. Mise en production (PythonAnywhere)

Variables d'environnement à définir (fichier WSGI ou onglet « Web ») :
```
DJANGO_SECRET_KEY=une-longue-chaine-aleatoire
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=votrepseudo.pythonanywhere.com
```

Ensuite :
```bash
python manage.py collectstatic
```

Dans l'onglet **Web**, déclarez :
- URL `/static/` → dossier `/home/votrepseudo/fase-django/staticfiles/`
- URL `/media/`  → dossier `/home/votrepseudo/fase-django/media/`

## 4. Sauvegarde

La base est le fichier `db.sqlite3`, les fichiers envoyés sont dans `media/`.
Sauvegardez les deux régulièrement (`python manage.py dumpdata > sauvegarde.json` est aussi possible).
