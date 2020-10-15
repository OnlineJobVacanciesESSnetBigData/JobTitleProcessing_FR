# -*- coding: utf-8 -*-
"""
Cleaner.
"""
import pickle
import os
import pandas as pd
from job_title_processing.core import SeriesCleaner
from job_title_processing.core import Lemmatizer
from job_title_processing.tools import load_root_path
from job_title_processing.tools import predict_svm
from job_title_processing.tools import get_nomenclature

class JobOffersTitleCleaner(SeriesCleaner):

    def __init__(
            self, language='FR', jobword=True, location=True, remove_csv=None, 
            remove_csv_colname=None, pickle=None
            ):
        """
        Dedicated cleaner for job offers titles:
            * language           : implemented langage to look for src (str)
            * jobwords           : True if job related words must be removed 
                                   else False
            * location           : True if locatio such as country, regions, 
                                   districts must be removed else False
            * remove_csv         : csv with more words to remove 
                                   (to put in "ressources_txt")
            * remove_csv_colname : colname to use for remove_csv
            * pickle             :  DO NOT USE
        """
#        ROOT_DIR = load_root_path()
#        self.lang_path = os.path.join(ROOT_DIR, "data", language)
#        os.makedirs(self.lang_path) if not os.path.exists(self.lang_path) else None
        
        if pickle is not None and os.path.exists(os.path.join(self.lang_path, pickle)):
            self.load(pickle)
            
        else:
            if language == 'FR':
                ### Load ressources - Location
                from job_title_processing.ressources_txt.FR.cleaner.location import (
                    loc_departments, loc_countries, loc_regions, loc_others,
                    loc_replace_infirst
                    )
                # Load ressources - classic stuff
                from job_title_processing.ressources_txt.FR.cleaner.default import (
                    default_punctuation, default_stopwords, default_specialcharmap
                    )
                # Load ressources - job related words
                from job_title_processing.ressources_txt.FR.cleaner.job import (
                    jobwords, job_replace_infirst
                    #, job_normalize_map
                    )
            # Not implemented languages
            else:
                raise NotImplementedError("Provided langage not implemented.")
            
            # Merge ressources
            replace_infirst = {**loc_replace_infirst, **job_replace_infirst}
            # Add jobwords
            remove_words = jobwords if jobword else []
            # Add location ressources
            if location:
                remove_words += loc_departments + loc_regions + loc_countries + loc_others
            if remove_csv is not None:
                # Read words to remove in csv file and add them
                ROOT_DIR = load_root_path()
                csv = os.path.join(ROOT_DIR, "ressources_txt", language,"cleaner", remove_csv)
                series_remove = pd.read_csv(csv, usecols=[remove_csv_colname])
                remove_words += list(series_remove[remove_csv_colname])
            # Init str cleaner
            super().__init__(
                default_punctuation, default_specialcharmap, default_stopwords,
                replace_infirst, remove_words
                )
    
    # Borrowed code
    def save(self, filename):
        filename = os.path.join(self.lang_path, filename)
        dirname = os.path.dirname(filename)
        os.makedirs(dirname) if not os.path.exists(dirname) else None
            
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f, 2)
            f.close()
        
    def load(self, filename):
        filename = os.path.join(self.lang_path, filename)
        with open(filename, 'rb') as f:
            tmp_dict = pickle.load(f)
            f.close()
            self.__dict__.update(tmp_dict)
        
class JobOffersTitleLemmatizer(Lemmatizer):
    
    def __init__(self, language='FR', pickle=None, cleaner=None):
        """
        Dedicated lemmatizer for job offers titles:
            * language : implemented langage to look for src (str)
            * cleaner  : SeriesCleaner to use
            * pickle   : DO NOT USE
        """
#        ROOT_DIR = load_root_path()
#        self.lang_path = os.path.join(ROOT_DIR, "pickle", language)
#        os.makedirs(self.lang_path) if not os.path.exists(self.lang_path) else None
        
        # Check if pickled lemmatizer exist
        if pickle is not None and os.path.exists(os.path.join(self.lang_path, pickle)):
            self.load(pickle)
        elif cleaner is not None:
            super().__init__(series_cleaner=cleaner, language=language)
        else:
            jot_cleaner = JobOffersTitleCleaner(language=language)
            super().__init__(series_cleaner=jot_cleaner, language=language)
     
    # Borrowed code
    def save(self, filename):
        filename = os.path.join(self.lang_path, filename)
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f, 2)
            f.close()
        
    def load(self, filename):
        filename = os.path.join(self.lang_path, filename)
        with open(filename, 'rb') as f:
            tmp_dict = pickle.load(f)
            f.close()
            self.__dict__.update(tmp_dict)
            
class JobOffersTitleOccupationMatcher():
    # Only from French language
    """Class to make it easier to match a dataframe containing job titles."""
    
    def __init__(self, lemmatizer, svm_model_file):
        self.lemmatizer = lemmatizer
        with open(svm_model_file, 'rb') as f:
            self.svm =  pickle.load(f)
            f.close()
    
    def match_job_title(self, text):
        # Transform everything into a series
        if type(text) == str:
            series = pd.Series([text])
        elif type(text) == list:
            series = pd.Series(text)
        elif type(text) == pd.core.series.Series:
            series = text
        else:
            print("*** Provide handled datatype (str, list, pandas Series)***")
            return None
        match = pd.DataFrame()
        match['Job offer title'] = series
        lemmatized_txt = self.lemmatizer.lemmatize_series(series)
        match['Clean and lemmatized text'] = lemmatized_txt
        match['ROME occupation code'] = predict_svm(self.svm, lemmatized_txt)
        # Retrieve class name
        df_class_name = get_nomenclature('FR')
        
        res = pd.merge(
                match, df_class_name, how='left', left_on='ROME occupation code', 
                right_on="ROME_code"
                ).drop("ROME_code", axis=1)
        res.rename(
                {
                "ROME_text" : 'ROME label'
                }, axis=1, inplace=True
        )
        return res
        
        
            
            
            
            
            
            
            
            
            
