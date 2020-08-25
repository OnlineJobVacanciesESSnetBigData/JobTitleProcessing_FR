# Job Title Processing

This repo contains a package to clean job titles and classify them into occupation nomenclature. 
It was designed for French language but French ressources are separated from the main code. It should
be fairly easy to add your own language.

## Getting started

### Prerequisites

A Python 3 (>= 3.7) installation is required.


You also have to download/ugrade following dependencies: 
* Pandas (>= 1.0.5)
* Numpy (>= 1.17.0 ; dependency of Pandas)
* Nltk (>=3.4.4)
* Matplotlib (>=3.1.1)
* Sklearn (>= 0.20.2)


### Installation


To install the package, use the `setup.py` file in the main folder. You can install it in a develop mode.

```
cd job_title_processing
python setup.py develop
```

## Implement text processing tools

### a. Create a text cleaner

### b. Create a text lemmatizer

### c. Train a SVM model


Some ressources for French language can be found in XXX.
Training data and models are not shared for now, but main results for French case can be
 found in the [notebooks](https://github.com/OnlineJobVacanciesESSnetBigData/JobTitleProcessing_FR/tree/master/notebooks).