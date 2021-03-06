## Résumé

Site web d'Orange County Lettings <br>
[![CircleCI](https://circleci.com/gh/mavamalonga/OC-Lettings/tree/main.svg?style=svg)](https://circleci.com/gh/mavamalonga/OC-Lettings/tree/main)

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Mise en place de l'intégration et déploiement continu (Pipeline CI/CD)

### Prérequis

- Compte Docker Hub 
- Compte CircleCI
- Compte Sentry
- Compte Heroku 

### Stockage de variables dans l'environnement local : Etape pour l'éxécution en local

- Créer un fichier `.env` dans le répertoire racine du projet 

.env ou dotenv est un simple fichier texte de configuration permettant de contrôler les constantes de l'environnement de vos applications.

### Installation Docker 

- Rendez-vous sur le site officiel de docker et téléchargez l'application `Docker desktop`
- Ouvrez l'application Docker desktop, cliquez sur sign-in, connectez-vous à votre compte Docker Hub pour faire la liaison avec l'application Docker desktop en local
- Créer un fichier `.dockerignore` 

`.dockerignore` vous permet d'exclure des fichiers du contexte comme un fichier .gitignore vous permet d'exclure des fichiers de votre référentiel git. Cela aide à rendre la construction plus rapide et plus légère en excluant du contexte les gros fichiers ou le référentiel qui ne sont pas utilisés dans la construction.

### Installation Sentry

- Rendez-vous le site officiel de Sentry, ouvrez un compte personnel et créez un projet Python/Django pour l'application
- Sentry génére un bout de code (SDK) en python à intégrer dans le fichier settings du projet, récuperez seulement la clé dns 
- Enregistrer la clé dsn dans le fihcier .env ==> `dsn_key = "votre clé"` pour une utilisation local

Cette clé nous servira également pour la production, elle sera enregistrée dans votre compte circleCI.

### Installation Heroku

- Rendez-vous sur le site officiel de Heroku, ouvrez un compte personnel
- Cliquez sur `New > Create new app` pour créer le framework de l'application
- Ouvrez l'onglet settings, personnalisez `App name` et faitez la liaison avec le respository GitHub de l'application
- Dans l'onglet `deploy` cochez la case `Wait for CI to pass before deploy` et sélectionnez la branche à deployer

### Installation CircleCi

- Rendez-vous sur le site officiel de CircleCi, ouvrez un compte personnel
- Liéez votre compte Github à votre compte CircleCi
- Dans l'espace projects, sélectionnez le repository de notre projet en cliquant sur `Set up project`
- Sélectionnez le project dans le dashboard CircleCi puis cliquez sur `Project settings > Environnement variables`
- Enregistrez les variables environnements nécessaires lors de l'éxécution du pipeline CI/CD : DEBUG, DOCKERHUB_PASS, DOCKERHUB_USER, HEROKU_API_KEY, HEROKU_APP_NAME, SECRET_KEY, dsn

## Exécution de l'intégration et déploiement continu

Bravo! Vous avez effectué les étapes nécessaire pour l'intégration et le déploiement continu de l'application. Après chaque commit faite sur le repository GitHub, CircleCi lancera l'éxécution du fichier config.yml.

### Les étapes du Pipeline CI/CD 

### 1) unittest-and-linter 
CircleCi créer un environnement virtuel, installe les dépendances du project et éxécute l'ensemble des tests unitaires de l'application puis, CircleCI lance flake8 pour vérifier la confomité du code selon les règles PEP8 définit dans le fichier setup.cfg.
Si les tests réussissent CircleCi passe au job suivant, sinon l'éxécution s'arrête puis CircleCi renvoie la cause de l'echec.
Cette étape ne filtre pas les branches, elle sera éxécutée lors de chaque commit sur une branche du repository GitHub.

Vous pouvez éxécuter ces étapes avec une container docker en local.
- Ouvrez un terminal et déplacez vous dans le répertoire racine du project
- Lancer la commande `docker build --tag app_name:latest .` 
- Ouvrez Docker desktop, cliquez sur images puis lancez le container créee avec le bouton run
- Allez dans containers/app et ouvrez le terminal CLI du container
- Tapez les commandes suivantes: <br>
    `python manage.py test` <br>
    `flake8 --max-line-length=99` <br>

### 2) build-and-push-docker-image
CircleCi crée un container docker à partir du fichier Dockerfile du projet puis, 
une fois l'image créee elle est publiée sur le compte Docker Hub assigné.
Cette étape s'éxécute uniquement pour les commits faite sur la branche `main` du repository GitHub.

Pour faire la même chose en local.
- Ouvrez un terminal et déplacez vous dans le répertoire racine contenant le fichier Dockerfile
- Tapez les commandes suivantes : <br>
    `docker login -u DOCKERHUB_USER -p DOCKERHUB_PASS` <br>
    `docker build -t DOCKERHUB_USER/oc_lettings:lastest .` <br>
    `docker push DOCKERHUB_USER/oc_lettings:lastest` <br>

### 3) deploy-on-heroku
CircleCi fait la liaison avec le compte heroku grâce à l'API Key puis, procède à la configuration de l'environemment de production en mentionnant les valeurs des variables SECRET_KEY, HEROKU_APP_NAME pour identifier l'application, DEBUG, et dsn pour Sentry. <br>
Une fois la configuration finit, une image et créee à partir de Dockerfile puis deployée sur heroku en production.<br>Cette étape s'éxécute uniquement pour les commits faite sur la branche `main` du repository GitHub.
<br>

Pour faire la même chose manuellement.
Tout d'abord veillez à enregistrer les variables SECRET_KEY, DEBUG, dsn dans le fichier .env
du projet puis, suivez les étapes suivantes:
- Ouvrez un terminal et déplacez vous dans le répertoire racine contenant le fichier Dockerfile
- Tapez les commandes suivantes : <br>
    `heroku container:login` <br>
    `heroku container:push web --app NOM_APP_HEROKU` <br>
    `heroku container:release --app NOM_APP_HEROKU web` <br>

#### Lancer l'application en local
Si vous souhaitez éxécuter votre application en local avec une image docker, suivez les étapes suivantes: <br>
- Pour récupérer une image existant depuis Docker Hub <br>
    `docker pull DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE` <br>
    `docker run --name IMAGE_NAME -d -p PORT:PORT DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE` <br>
- Pour une image existante dans Docker desktop <br>
    `docker run --name IMAGE_NAME -d -p PORT:PORT DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE` <br>

### Contact
Pour tout autre question contactez-moi par mail : mavamalonga.alpha@gmail.com
