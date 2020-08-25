# -*- coding: utf-8 -*-
"""
"""

import os

def load_root_path():
    """Load the package's json configuration file."""
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(FILE_DIR)
    return ROOT_DIR
