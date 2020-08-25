# -*- coding: utf-8 -*-
"""
Cleaner
"""

import re
import unicodedata

        
class StringCleaner():
    
    """
    Class to roughly clean string.
        >>> jotc.clean_str("é $ ^ or er * %%% auprès télé (rgzerg)")
        >>> 'or er tele rgzerg'
    
    Use  "to_replace_infirst" to replace expressions or words before there
    are cleaned (eg. "3D"). Use a lemmatizer to perform word replacement after
    cleaning.
    
    """
    
    def __init__(
            self, punctuation=[], special_char=[], stopwords=[], 
            replace_infirst={}, remove_words=[]
#            , remove_words_csv='',
#            remove_words_csv_col=''
            ):

        self.special_char = special_char
        
        # Process punctuation
        self._punctuation_clean = [
            self.clean_str(punct, False, False, False, False, False)
            for punct in punctuation 
            ]
        self.punctuation_re = self.get_regex(self._punctuation_clean, False, False)
        
        # Process stopwords
        self._stopwords_clean = [
                self.clean_str(stopword, False, True, True, False, False) 
                for stopword in stopwords
                ]
        self.stopwords_re = self.get_regex(self._stopwords_clean, True, False)
        
        # Process replace in first
        self.replace_infirst_re = {
            "\\b(" + self.clean_str(key, False, False, False, False, False) + ")\\b" : 
                self.clean_str(value, False, False, False, False, False)
            for key, value in replace_infirst.items()
            }
        if '' in self.replace_infirst_re: del self.replace_infirst_re['']
 
        # Process additionnal words to remove
        
        self._remove_words_clean = [
                self.clean_str(remove_word, False, True, True, True, False) 
                for remove_word in remove_words
                ]
        self.remove_words_re = self.get_regex(self._remove_words_clean, True, False)
        

        
        
    # Compile array of words into regex pattern
    def get_regex(self, str_arr, bound=True, clean=True):
        "Clean and compile ressources for more efficient regex."
        # Clean array
        clean_strings = []
        for i, str_ in enumerate(str_arr):
            clean_str = self.clean_str(str_) if clean else str_
            if (len(clean_str) != 0) and (clean_str not in clean_strings):
                clean_strings += [clean_str]
        # Sort array 
        clean_strings.sort(key=len, reverse=True)
        # Compile regex
        compile_str = "\\b(" if bound else ""
        for i, clean_string in enumerate(clean_strings):
            if clean_string == "\\": # Otherwis epb with punctuation
                continue
            if i == 0:
                compile_str += clean_string
            else:
                compile_str += '|' + clean_string
#        compile_str += "|\\" if add_back else ""
        compile_str += ")\\b" if bound else ""
        return compile_str
    
    def normalize_char(self, text, lower=True):
        """
        Clean accents and char such as : 
            accent_charmap = [ 
                ('àâå', 'a'), ('éèêë', 'e'), ('ùûü', 'u'), ('îï', 'i'), 
                ('ôö', 'o'), ('ÿ', 'y'), ('ç', 'c')
            ]
        Clean some punctuation.
        Replace special char.
        """
        text = text.lower() if lower else text
        # Transform special char
        for character in self.special_char:
            text = re.sub('[%s]' % character[0], character[1], text)
        # Clean accents
        text = unicodedata.normalize('NFKD', text)
        text = text.encode("ascii", errors='ignore').decode("utf-8")
        return text
    
    def remove_punctuation(self, text):
        if self.punctuation_re == '':
            return text
        text = re.sub(self.punctuation_re, ' ', text)
        return re.sub('  +', ' ', text)
    
    def remove_stopwords(self, text):
        text = re.sub(self.stopwords_re, '', text)
        return re.sub('  +', ' ', text)
    
    def remove_digits(self, text):
        text = re.sub('\d', '', text)
        return re.sub('  +', ' ', text)
    
    def replace_infirst(self, text):
        for key, value in self.replace_infirst_re.items(): 
            text = re.sub(key, value, text)
        return re.sub('  +', ' ', text)
    
    def remove_words(self, text):
        text = re.sub(self.remove_words_re, '', text)
        return re.sub('  +', ' ', text)
    
    def clean_str(
            self, text, replace_infirst=True, punctuation=True, digits=True, 
            stopwords=True, remove_words=True
            ):
        # Do it anyway
        text = str(text)
        text = self.normalize_char(text)
        text = re.sub('[\r\n\t]', ' ', text)
        text = re.sub('  +', ' ', text)
        
        # To replace in first
        text = self.replace_infirst(text) if replace_infirst else text
        
        # Punctuation
        text = self.remove_punctuation(text) if punctuation else text
        
        # Digits
        text = self.remove_digits(text) if digits else text
        
        # Stopwords
        text = self.remove_stopwords(text) if stopwords else text
        
        # More words to remove
        text = self.remove_words(text) if remove_words else text
        
        return re.sub('^\s+|\s+$', '', text)
    
    # TODO clean and substract string ? As for series
    # TODO handle brackets
    