# -*- coding: utf-8 -*-
"""
Adaptated version of string cleaner to pandas series.
"""

from job_title_processing.core import StringCleaner

class SeriesCleaner(StringCleaner):
    
    def __init__(self, punctuation=[], special_char=[], stopwords=[], 
            replace_infirst={}, remove_words=[]):
        super().__init__(
            punctuation, special_char, stopwords, replace_infirst, 
            remove_words
            )
    
    def clean_series(
            self, series, replace_infirst=True, punctuation=True, digits=True, 
            stopwords=True, remove_words=True
            ):
        # Do it anyway
        series = series.astype(str)
        series = self.normalize_char_series(series)
        series = series.str.replace('[\r\n\t]', ' ')
        series = series.str.replace('\s+', ' ')
        
        # To replace in first
        series = self.replace_infirst_series(series) if replace_infirst else series
        
        # Punctuation
        series = self.remove_punctuation_series(series) if punctuation else series
        
        # Digits
        series = self.remove_digits_series(series) if digits else series
        
        # Stopwords
        series = self.remove_stopwords_series(series) if stopwords else series
        
        # More words to remove
        series = self.remove_words_series(series) if remove_words else series
        
        return series.str.replace('^\s+|\s+$', '')

    def normalize_char_series(self, series, lower=True):
        # Lower
        series = series.str.lower() if lower else series
        # Transform special char
        for character in self.special_char:
            series = series.str.replace('[%s]' % character[0], character[1])
        # Clean accents
        series = series.str.normalize('NFKD')
        series = series.str.encode('ascii', errors='ignore').str.decode('utf-8')
        return series

    def remove_punctuation_series(self, series):
        if self.punctuation_re == '':
            return series
        series = series.str.replace(self.punctuation_re, ' ')
        return series.str.replace('\s+', ' ')
    
    def remove_stopwords_series(self, series):
        series = series.str.replace(self.stopwords_re, '')
        return series.str.replace('\s+', ' ')
    
    def remove_digits_series(self, series):
        series = series.str.replace('\d', '')
        return series.str.replace('\s+', ' ')
    
    def replace_infirst_series(self, series):
        for key, value in self.replace_infirst_re.items(): 
            series = series.str.replace(key, value)
        return series.str.replace('\s+', ' ')
    
    def remove_words_series(self, series):
        series = series.str.replace(self.remove_words_re, '')
        return series.str.replace('\s+', ' ')
