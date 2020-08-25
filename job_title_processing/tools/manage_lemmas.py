# -*- coding: utf-8 -*-
"""
Load lemmas from .json or .py files.
Manage external ressources.
"""

import json
import os
from job_title_processing.tools import load_root_path

def manage_lemmas_expr(language):
    if language == 'FR':
        return manage_lemmas_expr_FR()
    else:
        raise ValueError('Not implemented language.')

def manage_lemmas(language):
    if language == 'FR':
        return manage_lemmas_FR()
    else:
        raise ValueError('Not implemented language.')
        
def manage_lemmas_FR():
    """Agregate ressources as a list of dictionnaries."""
    ROOT_DIR = load_root_path()
    fr_path = os.path.join(ROOT_DIR, "ressources_txt","FR")
    lemmas_list = [] # Init
    # 1. Use Morphalou dictionnary to nomalize words
    # TODO : read morphalou from internet if not loaded yet
    # https://www.ortolang.fr/market/lexicons/morphalou
    morphalou_file = os.path.join(fr_path, "lemmas_morphalou.json")
    with open(morphalou_file, "r") as f:
        morphalou = json.load(f)
    lemmas_list += [morphalou]
    
    # 2. External ressources to get feminine version of job title
    job_FM_file = os.path.join(fr_path, "lemmas_job_FM.json")
    with open(job_FM_file, "r") as f:
        job_FM = json.load(f)
    lemmas_list += [job_FM]
    
    # 3. External ressources to get acronyms explicitations
    from job_title_processing.ressources_txt.FR.job import job_normalize_map
    job_normalize_dict = {}
    for (t1, t2) in job_normalize_map:
        # TODO check if problem (similar keys)
        job_normalize_dict[t1] = t2
    lemmas_list += [job_normalize_dict]
    
    return lemmas_list

def manage_lemmas_expr_FR():
    """Get french lemmas expressions."""
    from job_title_processing.ressources_txt.FR.job import job_lemmas_expr
    return job_lemmas_expr