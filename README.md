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
* Xlrd (>= 1.0.0)

To install the previous libraries using `conda`, simply type the following commands in a
command line (on a Linux system, it may be necessary to preceed each command
with `sudo`) :

```
conda install matplotlib
conda install pandas
conda install nltk
conda install scikit-learn
conda install xlrd
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

## Resources (French)

Package works without following ressources, but using them will improve its 
performance for French language.

### Lemmatization resources

This package makes use of an external resource to conduct lemmatization, i.e. the
task of associating word forms in a text with a reference lemma.

To perform lemmatization, Morphalou corpus is used. It is a corpus covering
the French language, available [here](https://www.ortolang.fr/market/lexicons/morphalou/4). 
Its use requires you to download morphalou 4 (or 3.1) and unzip folder called 
Morphalou3.1_formatCSV in `ressources_txt\FR\lemmatizer` folder.

Please note that this resource is distributed under its own license,
which you should read and abide by in your usage.

### Taxonomy resources

In order to match ROME occupation codes to their official names, download 
Pôle Emploi's ROME taxonomy available [here](https://www.pole-emploi.org/opendata/repertoire-operationnel-des-meti.html?type=article).
Put the file named `ROME_ArboPrincipale.xlsx` in `ressources_txt\FR\nomenclature` folder
(you must create this folder).

## Implementing text processing tools

Please refer to the hand book jupyter notebook ([here](https://github.com/OnlineJobVacanciesESSnetBigData/JobTitleProcessing_FR/blob/master/notebooks/Hand_Note_Book.ipynb)), which shows you how to use package cleaner, lemmatizer and classifier.

If you are using a conda env, you should activate a kernel to use jupyter notebooks.

```
activate myenv
conda install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python 3 (myenv)"
jupyter notebook
```

Once jupyter is launched, please check you are using the desired kernel. You can
change it in Kernel >> Change kernel. 

## General remarks

* Specific language ressources (stopwords, job related words, ...) must be uploaded in the `ressources_txt` folder.
Fench ressources can be used as an example of required format. 

* **Training data and models are not shared for now** but main results for French case can be
found in the [notebooks](https://github.com/OnlineJobVacanciesESSnetBigData/JobTitleProcessing_FR/tree/master/notebooks).

## Authors

Package was designed on the behalf of Dares ([dares.travail-emploi.gouv.fr](https://dares.travail-emploi.gouv.fr/dares-etudes-et-statistiques/)) which is the division of Research, Economic analysis and Statistics of the French Ministry of Labour.

Main author : Claire de Maricourt

## Related publications

* Analysis of French OJAs scraped in 2019 (in French): [Online job advertisements, a new data source on labour market](https://dares.travail-emploi.gouv.fr/publication/les-offres-demploi-en-ligne-nouvelle-source-de-donnees-sur-le-marche-du-travail)

* Methodological report of ESSnet Big Data 2: [Methodological framework for processing online job adverts data](https://ec.europa.eu/eurostat/cros/content/wpb-milestones-and-deliverables-0_en)
