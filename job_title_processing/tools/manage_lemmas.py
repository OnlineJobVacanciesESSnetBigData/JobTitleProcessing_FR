# -*- coding: utf-8 -*-
"""
Load lemmas from .json or .py files.
Manage external ressources.
"""

import json
import os
import pandas as pd
from job_title_processing.tools import load_root_path

def manage_lemmas_expr(language):
    # More than one word "lemmas"
    if language == 'FR':
        return manage_lemmas_expr_FR()
    else:
        raise ValueError('Not implemented language.')
        
def manage_lemmas_expr_FR():
    """Get french lemmas expressions."""
    from job_title_processing.ressources_txt.FR.job import job_lemmas_expr
    return job_lemmas_expr

def manage_lemmas(language):
    # One word lemmas
    if language == 'FR':
        return manage_lemmas_FR()
    else:
        raise ValueError('Not implemented language.')
        
def manage_lemmas_FR():
    """Agregate ressources as a list of dictionnaries."""
    ROOT_DIR = load_root_path()
    fr_path = os.path.join(ROOT_DIR, "ressources_txt","FR", "lemmatizer")
    lemmas_list = [] # Init
    # 1. Use Morphalou dictionnary to nomalize words
    morphalou = _get_morphalou_FR(fr_path)
    if morphalou is not None:
        lemmas_list += [morphalou]

    # 2. External ressources to get feminine version of job titles
    masc_fem = _get_fem_masc_lemmas_FR(fr_path)
    if morphalou is not None:
        lemmas_list += [masc_fem]
    
    # 3. External ressources to get acronyms explicitations
    # TODO transform acronyms into a csv file
    from job_title_processing.ressources_txt.FR.cleaner.job import job_normalize_map
    job_normalize_dict = {}
    for (t1, t2) in job_normalize_map:
        # TODO check if problem (similar keys)
        job_normalize_dict[t1] = t2
    lemmas_list += [job_normalize_dict]
    
    return lemmas_list

def _get_morphalou_FR(fr_path, verbs=False):
    """ 
    Function to find morphalou csv file and transform it into a json file 
    if not done already.

    Return a dictionnary with lemmas.
    """
    morphalou_json = os.path.join(fr_path, "lemmas_morphalou.json")
    # Check if json file is already here
    if os.path.exists(morphalou_json):
        with open(morphalou_json, "r", encoding="utf-8-sig") as f:
            lemmas_dict = json.load(f)
            return lemmas_dict
    # Look for morphalou csv files
    morphalou_csv_folder = os.path.join(fr_path, "Morphalou3.1_formatCSV")
    if os.path.exists(morphalou_csv_folder):
        print("*** Processing Morphalou files ***")
        # Process commun nouns csv
        noun_csv = os.path.join(morphalou_csv_folder, "commonNoun_Morphalou3.1_CSV.csv")
        nouns = pd.read_csv(
                noun_csv, sep=";", encoding="utf-8", skiprows=14, 
                low_memory=False, usecols=['LEMME', 'FLEXION']
                )
        nouns.LEMME = nouns.LEMME.fillna(method='ffill')
        nouns = nouns.iloc[1:]
        # Process adjectives csv
        adj_csv = os.path.join(morphalou_csv_folder, "adjective_Morphalou3.1_CSV.csv")
        adjectives = pd.read_csv(
                adj_csv, sep=";", encoding="utf-8", skiprows=14, 
                low_memory=False, usecols=['LEMME', 'FLEXION']
                )
        adjectives.LEMME = adjectives.LEMME.fillna(method='ffill')
        adjectives = adjectives.iloc[1:]
        
        df = nouns.append(adjectives)
        lemmas_dict = dict(zip(df.FLEXION, df.LEMME))
        
        # Only record entries with different key/value
        to_remove = []
        for key, value in lemmas_dict.items():
            if key == value:
                to_remove += [key]
        for key in to_remove:
            del lemmas_dict[key]
        
        # Get json file
        with open(morphalou_json, 'w', encoding="utf-8-sig") as f:
            json.dump(lemmas_dict, f, ensure_ascii=False)
        print("*** Successfully processed Morphalou files ***")
        return lemmas_dict
    else:
        print(
                '''*** \n'''
                '''Please download Morphalou3.1_formatCSV folder available on'''
                ''' https://www.ortolang.fr/market/lexicons/morphalou/4 \n''' 
                '''Unzip it in job_title_processing\\job_title_processing\\ressources_txt\\FR\\lemmatizer \n'''
                '''***'''
              )
        return None
            
def _get_fem_masc_lemmas_FR(fr_path):
    masc_fem_json = os.path.join(fr_path, "lemmas_job_masc_fem.json")
    # Check if json file is already here
    if os.path.exists(masc_fem_json):
        with open(masc_fem_json, "r", encoding="utf-8-sig") as f:
            lemmas_dict = json.load(f)
            return lemmas_dict
    # Look for masculine/feminine csv file
    masc_fem_csv = os.path.join(fr_path, "lemmas_job_masc_fem.csv")
    if os.path.exists(masc_fem_csv):
        print("*** Processing Masculine/Feminine lemmas file ***")
        # Process commun nouns csv
        masc_fem = pd.read_csv(
                masc_fem_csv, sep=";", encoding="utf-8", usecols=['LEMME', 'FLEXION']
                )
        lemmas_dict = dict(zip(masc_fem.FLEXION, masc_fem.LEMME))
        
        # Only record entries with different key/value
        to_remove = []
        for key, value in lemmas_dict.items():
            if key == value:
                to_remove += [key]
        for key in to_remove:
            del lemmas_dict[key]
            
        # Get json file
        with open(masc_fem_json, 'w', encoding="utf-8-sig") as f:
            json.dump(lemmas_dict, f, ensure_ascii=False)
        print("*** Successfully processed Masculine/Feminine lemmas files ***")
        return lemmas_dict
    else:
        print(
                '''*** \n'''
                ''' Masculine/Feminine lemmas csv fil not found. \n'''
                '''***'''
              )
        return None
    