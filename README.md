# apolloaipackage

INSTALLATION INSTRUCTIONS: "apolloaipackage" ------> across different system setups.

(1) Linux Installation Process -- without docker:

Check if pip is updated. -- pip install --upgrade pip

Check if Git is present.

![git_rep](https://user-images.githubusercontent.com/23459946/45771011-f96df900-bc11-11e8-8d52-e09575b89777.png)

This is the git repository page.
git clone "https://github.com/kauku123/apolloaipackage"

The folloing are the necssary libraries for executing the scripts in this apolloaipackage.
1. numpy
2. scipy
3. scikit-learn
4. matplotlib
5. jupyter
6. tensorflow

Using "pip install -r requirements.txt" ---> install these libraries for executing the models.

![nb2py](https://user-images.githubusercontent.com/23459946/45773945-b2840180-bc19-11e8-8e2b-6c714e1b33ab.png)
Screenshot shows the IPython notebooks converted to .py executable files.
This package mostly contains IPython notebooks (jupyter). So as to obtain executable python (.py) files of these notebooks, clone into the directory and run:
"jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb"

For the local datasets, only nearestneighbor.ipynb requires a dataset from theinternet. 
So added an import statement from sklearn for accessing this dataset locally.

Run the model: python model.py ------>debug mode; python model.py --debug.

_________________________________________________________________________________

(2) Windows Installation Process -- without docker


For windows, Tensorflow is supported only for Python3.x. Checkif Python on the machine is updated. Else, update:
Installations can be found here: https://www.python.org/downloads/

Check if pip is updated. -- pip install --upgrade pip

Check if Git is present.

git clone "https://github.com/kauku123/apolloaipackage"

Using "pip install -r requirements.txt" install required libraries for executing the models.

This package mostly contains IPython notebooks (jupyter). So as to obtain executable python (.py) files of these notebooks, clone into the directory and run:
"jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb"

For the local datasets, only nearestneighbor.ipynb requires a dataset from theinternet. 
So added an import statement from sklearn for accessing this dataset locally.

Run the model: python model.py ------>debug mode; python model.py --debug.

_________________________________________________________________________________

(3) Linux Installation Process -- with virtualenv:

Check if pip is updated. -- pip install --upgrade pip

Install virtualenv ---> pip install --user virtualenv

virtualenv enables the user to operate python environments simultaneously for multiple projects. Aids in installing modules and packages without hindering the python system environment.
Check if Git is present.

git clone "https://github.com/kauku123/apolloaipackage"

Using "pip install -r requirements.txt" install required libraries for executing the models.

This package mostly contains IPython notebooks (jupyter). So as to obtain executable python (.py) files of these notebooks, clone into the directory and run:
"jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb"

For the local datasets, only nearestneighbor.ipynb requires a dataset from theinternet. 
So added an import statement from sklearn for accessing this dataset locally.

Run the model: python model.py ------>debug mode; python model.py --debug.

_________________________________________________________________________________

(4) Windows Installation Process -- with virtualenv:

For windows, Tensorflow is supported only for Python3.x. Checkif Python on the machine is updated. Else, update:
Installations can be found here: https://www.python.org/downloads/

Check if pip is updated. -- pip install --upgrade pip

Install virtualenv --->  py -m pip install --user virtualenv

virtualenv enables the user to operate python environments simultaneously for multiple projects. Aids in installing modules and packages without hindering the python system environment.

Check if Git is present.

git clone "https://github.com/kauku123/apolloaipackage"

Using "pip install -r requirements.txt" install required libraries for executing the models.

This package mostly contains IPython notebooks (jupyter). So as to obtain executable python (.py) files of these notebooks, clone into the directory and run:
"jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb"

For the local datasets, only nearestneighbor.ipynb requires a dataset from theinternet. 
So added an import statement from sklearn for accessing this dataset locally.

Run the model: python model.py ------>debug mode; python model.py --debug.

_________________________________________________________________________________

(5) Linux Installation Process - with Docker


Install Docker from ---> https://docs.docker.com/install/linux/docker-ce/ubuntu/

Pull Docker from: docker pullInstall docker from sssk/apolloaipackage

![docker_apolloaipackage](https://user-images.githubusercontent.com/23459946/45770002-3c7a9d00-bc0f-11e8-8a44-d6767822fb2e.png)


Run it on local machine using ---> docker run " repository name  "

Access the returned URL from the localhost and edit the Ipy notebooks.

Also automated build from GitHub is active. So, one can easily access the git rep also.

This is the docker hub repository. Can access the git repository from the source link.

Check if Git is present.

git clone "https://github.com/kauku123/apolloaipackage"

Using "pip install -r requirements.txt" install required libraries for executing the models.

This package mostly contains IPython notebooks (jupyter). So as to obtain executable python (.py) files of these notebooks, clone into the directory and run:
"jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb"

For the local datasets, only nearestneighbor.ipynb requires a dataset from theinternet. 
So added an import statement from sklearn for accessing this dataset locally.

Run the model: python model.py ------>debug mode; python model.py --debug.


