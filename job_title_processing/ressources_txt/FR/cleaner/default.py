# -*- coding: utf-8 -*-

default_punctuation = [
        "\[", "\]",
        "\{", "\}",
        "\(", "\)",
        "\<", "\>",
        "\\\\",
        "\?", "\!", "\.", "\,", "\;", "\:",
        "\'", "\’", 
        "\\\"", "\`", '\\x92',
        "\*", "\°", "\_", "\+", "\&", "\/", "-", "\|",
        "=", "#", "%", "·", 
        "\$", "\^", "£", "€",
        "¿",
        "«", "»"
        ]
    
default_specialcharmap = [
           ('œ', 'oe'), ('æ','ae')
        ]

default_stopwords = [ # écrire avec et sans accents
        # Must be  unique words
        'le', 'la', 'les', 'un', 'une', 'uns', 'unes', 'des', 
        'du', 'de', 'et', 'ou', 'avec', 'au', 'aux', 'que', 'qui', 
        'pour', 'pr', 'en', 'dans', 'sur', 'chez', 'à',
        'etc', 'auprès', 'après', 'par', "plusieurs", "tout",
        # One letter string --> 'b to b' ??
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]


