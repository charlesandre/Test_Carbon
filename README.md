# Test Technique Carbon IT

## La carte aux trésors

Exercice réalisé en python.

#### Prérequis

* Python 2.7
* Git
* Pip
* Docker

#### Pour lancer :

* Cloner le repo :

```
git clone https://github.com/charlesandre/Test_Carbon.git
cd Test_Carbon/
pip install -r requirements.txt #filecmp for the tests and click.
```

#### Lancer les tests :

```
python test.py
```

#### Executer :

Placer un fichier d'input dans le dossier data.
Passer en paramètre le nom du fichier d'input et d'output

```
python run.py inputfile outputfile #The output will be created, default : input.txt and output.txt
```


### Avec Docker :
```
docker build -t myApp ./

#Docker will run the tests when building

docker run myApp # Default input and output file will be used.
```


Fait par Charles ANDRE
