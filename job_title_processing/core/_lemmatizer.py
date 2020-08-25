# -*- coding: utf-8 -*-
"""
Lemmatizer
"""

import re
import pandas as pd
from job_title_processing.core import SeriesCleaner
from job_title_processing.tools import manage_lemmas, manage_lemmas_expr

class Lemmatizer():
    
    """Lemmatize text in a string with provided dictionnary."""
    
    def __init__(
            self, lemmas_list=None, language=None, series_cleaner=None,
            lemmas_expr={}
            ):
        """
        * lemmas_list : list of dictionnary of key/value (//!\\ no blanks in key)
        * lemmas_expr :dict of lemmas which contains blanks
        """
        if language is None and lemmas_list is None:
            raise ValueError("Lemmas and language can not be both None.")
        if language is not None:
            # TODO check if language is implemented
            lemmas_list = manage_lemmas(language) 
#            lemmas_expr = manage_lemmas_expr(language)
            lemmas_expr = manage_lemmas_expr(language) #  'cours particulier' : 'professeur',
        if series_cleaner is None:
            series_cleaner = SeriesCleaner() # Carefull : normalize accents + Maj
        self.cleaner = series_cleaner
        self.lemmas = self.get_clean_lemmas(lemmas_list)
        self.lemmas_expr_re = self.get_lemmas_expr_re(lemmas_expr)
#        self.A_ahocorasick = self._init_automaton_ahocorasick()

    def _lemmatize_str(
            self, text, lemmas, clean=True, regex=True, drop_duplicate=True, expr=True
            ):
        text = self.cleaner.clean_str(text) # Clean text
        tokens = [] # Lemmatize
        for word in text.split(' '):
            if regex:
                if word in self.lemmas.keys():
                    word = self.lemmas[word]
                tokens += [word]
#            else:
#                tokens += [self._lemmatize_str_ahocorasick(word)]
        if expr: # Replace lemmas ith a blank
            text = self.replace_expr(' '.join(tokens))
        tokens = text.split(' ')
        if drop_duplicate:
            tokens = list(set(tokens))
        return ' '.join(tokens)
    
    def lemmatize_str(self, text, clean=True, regex=True, drop_duplicate=True, expr=True):
        return self._lemmatize_str(text, self.lemmas, clean, regex, drop_duplicate, expr)

    def get_lemmas_expr_re(self, dict_):
        dict_re = {
            "\\b(" + self.lemmatize_str(key, drop_duplicate=False, expr=False) + ")\\b" : 
            self.lemmatize_str(value, drop_duplicate=False, expr=False)
            for key, value in dict_.items()
            }
        if '' in dict_re: del dict_re['']
        return dict_re
        
    def replace_expr(self, text):
        for key, value in self.lemmas_expr_re.items(): 
            text = re.sub(key, value, text)
        return re.sub('  +', ' ', text)   

    def get_clean_lemmas(self, lemmas_list):
        """
        Get a cleaned and unique dictionnary of lemmas:
            * clean lemmas with cleaner
            * clean lemmas between them (check same keys in multiple dict, 
                                         etc.)
        """
        clean_dict = {}
        for lemmas_dict in lemmas_list:
            for key, value in lemmas_dict.items():
                clean_key = self.cleaner.clean_str(key)
                clean_value = self.cleaner.clean_str(value)
                if clean_key == "": # Warn if empty str
#                    print("Warning: empty key " + str(key) + ' : ' + str(value))
                    continue
#                if clean_key in clean_dict.keys() and clean_value != clean_dict[clean_key]:
#                    print(
#                        "Key (" + str(clean_key) + " : " +
#                        str(clean_dict[clean_key]) + ") replaced by (" + 
#                        str(clean_key) + " : " + str(clean_value) + ")"
#                        )
                if clean_key != clean_value:
                    clean_dict[clean_key] = clean_value
#        print("Clean Lemmas")
        # Clean keys inbetween them
        # 1. Treat chains of lemmas
        final_dict = {}
        for key, value in clean_dict.items():
            while (value in clean_dict.keys()):
                value = clean_dict[value]
                if value == key:
                    print("Problem with " + str(key))
                    break
            final_dict[key] = value
        # 2. Treat multiple words values (//!\\ keys = 1 word only)
        for key, value in final_dict.items():
            words = value.split(' ')
            if len(words) > 1:
                final_value = self._check_multiple_words(words, final_dict, key)
                final_dict[key] = ' '.join(final_value)
        return final_dict
    
    def _check_multiple_words(self, words, dict_, key):
        final_value = []
        for word in words:
            if word == key:
                print('Redondant lemmas ' + str(key))
                break
            if word in dict_.keys():
                value = dict_[word]
                if len(value.split(' ')) > 1:
                    final_value += self._check_multiple_words(
                        value.split(' '), dict_, word
                        )
                else:
                    final_value += [value]
            else:
                final_value += [word]
        return final_value
    
    def lemmatize_series(self, series, drop_duplicate=True):
        return series.apply(lambda x : self.lemmatize_str(x, drop_duplicate=drop_duplicate))
    
    def lemmatize_df(
            self, df, title_colname, sub_colnames=[], keep_col=[],clean=True
            ):
        res = df.apply(
                lambda row : self._lemmatize_row(
                        row, title_colname, sub_colnames
                        ), axis=1
                        )
        res.name = 'title_lemmatize'
        return pd.concat([df, res], axis=1)
        
    def _lemmatize_row(
            self, row, title_colname, sub_colnames=[], clean=True, 
            drop_duplicate=True
            ):
        lemmatize_title = self.lemmatize_str(row[title_colname], drop_duplicate=False)
        for colname in sub_colnames:
            lemmatize_col = self.lemmatize_str(row[colname], drop_duplicate=False)
            lemmatize_col_re = "\\b" + lemmatize_col + "\\b"
            lemmatize_title_sub = re.sub(lemmatize_col_re, '', lemmatize_title)
            if lemmatize_title_sub != "":
                lemmatize_title = lemmatize_title_sub
        lemmatize_title = re.sub('^\s+|\s+$', '', lemmatize_title)
        lemmatize_title = re.sub('\s+', ' ', lemmatize_title)
        if lemmatize_title == "":
            lemmatize_title = self.cleaner.clean_str(row[title_colname])
        if drop_duplicate:
            tokens = lemmatize_title.split(' ')
            tokens = list(set(tokens))
            text = ' '.join(tokens)
        else:
            text = lemmatize_title
        return text

    def lemmatize_csv(
            self, input_csv, output_csv, title_colname, sub_colnames=[],
            keep_col=[], clean=True, chunksize=20000, sep=";", encoding='utf-8-sig',
            break_=True
            ):
        
        chunks = pd.read_csv(
                input_csv, sep=sep, encoding=encoding, chunksize=chunksize
                )
        mode, header = 'w', True
        for chunk in chunks:
            clean_title = self.lemmatize_df(
                    chunk, title_colname, sub_colnames, keep_col, clean
                    )
            clean_title.to_csv(
                    output_csv, index=False, mode=mode, header=header, sep=sep,
                    encoding=encoding, columns = keep_col
                    )
            mode, header = 'a', False
            if break_:
                break