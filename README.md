# Job Title Processing

This repo contains a package to clean job titles and classify them into occupation nomenclature. 
It was designed for French language but French ressources are separated from the main code. It should
be fairly easy to add your own language.

## Getting started

### Prerequisites

* **Python**

A Python 3 (>= 3.7) installation is required. Python 2.x is **not** supported.

Following explanations assume you are using [Anaconda](https://www.anaconda.com/download/),
which contains both Python 3, useful development tools and a number of
libraries which should cover most of this project's requisites.

As this package and its installation setup are still in development, it is
advised to procede to the installation **in a virtual environment only**. To
learn how to set up such an environment, please refer to the `venv`
[documentation](https://docs.python.org/3/library/venv.html). However, here are
some basics to create and use and environment 

```
conda create --name myenv
activate myenv
```

* **Dependencies**

You also have to download/ugrade following dependencies: 
* Matplotlib (>=3.3.1)
* Pandas (>= 1.1.1)
* Nltk (>=3.4)
* Sklearn (>= 0.23.2)

To install the previous libraries using `conda`, simply type the following commands in a
command line (on a Linux system, it may be necessary to preceed each command
with `sudo`) :

```
conda install matplotlib
conda install pandas
conda install nltk
conda install scikit-learn
```

### Installation

To install this package as a `job_title_processing`, launch following command in the main folder:

```
pip install -e .
```

For Spyder user, package may not be visible unless you install Spyder within environment:

```
conda install spyder
spyder
```

Then you can import `job_title_processing` from Spyder as any other package.

## Ressources (French)

*To be completed*

## Implementing text processing tools

Please refer to the hand book jupyter notebook ([here](https://github.com/OnlineJobVacanciesESSnetBigData/JobTitleProcessing_FR/blob/master/notebooks/Hand_Note_Book.ipynb)), which shows you how to use package cleaner, lemmatizer and classifier.

If you are using a conda env, you should activate a kernel to use jupyter notebooks.

```
activate myenv
conda install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python 3 (myenv)"
jupyter notebook
```

## General remarks

* Specific language ressources (stopwords, job related words, ...) must be uploaded in the `ressources_txt` folder.
Fench ressources can be used as an example of required format. 

* **Training data and models are not shared for now** but main results for French case can be
found in the [notebooks](https://github.com/OnlineJobVacanciesESSnetBigData/JobTitleProcessing_FR/tree/master/notebooks).

## Authors

Package was designed on the behalf of Dares ([dares.travail-emploi.gouv.fr](https://dares.travail-emploi.gouv.fr/dares-etudes-et-statistiques/)) which is the division of Research, Economic analysis and Statistics of the French Ministry of Labour.

## Related publications

*To be completed*