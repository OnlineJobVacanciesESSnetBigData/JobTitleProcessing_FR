# -*- coding: utf-8 -*-
"""
Process external data on nomenclature to reuse it in the classifier.
"""

from job_title_processing.tools import load_root_path
import pandas as pd
import os

def manage_nomanclature_FR():
    """Get occupation code description, store it in csv file."""
    ROOT_DIR = load_root_path()
    fr_path = os.path.join(ROOT_DIR, "ressources_txt","FR", "nomenclature")
    label_file = os.path.join(fr_path,"ROME_nomenclature.csv")
    if os.path.exists(label_file):
        df = pd.read_csv(label_file, encoding="utf-8-sig", sep=";")
        return df
    file = os.path.join(fr_path,"ROME_ArboPrincipale.xlsx")
    if os.path.exists(file):
        xl = pd.ExcelFile(file)
        df = pd.read_excel(file, sheet_name=xl.sheet_names[1])
        cols = df.columns
        # Get ROME code and labels only
        mask_2 = df[cols[2]] != ' '
        mask_ogr = df['Code OGR'] == ' '
        df = df.loc[mask_2 & mask_ogr].copy()
        # Get relevant columns
        df["ROME_code"] = df[cols[0]] + df[cols[1]] + df[cols[2]]
        df.rename(columns={cols[3]: 'ROME_text'}, inplace=True)
        # To csv
        df.to_csv(
                label_file, encoding="utf-8-sig", sep=";", index=False,
                columns=['ROME_code', 'ROME_text']
                )
        return df
    else:
        print(
                '''*** \n'''
                '''Please download the 'Arborescence principale' file available on'''
                ''' https://www.pole-emploi.org/opendata/repertoire-operationnel-des-meti.html?type=article \n''' 
                '''Put in job_title_processing\\job_title_processing\\ressources_txt\\FR\\nomenclature \n'''
                '''***'''
              )
        return None

def get_labels_ROME_FR():
    """
    Read job titles and matching occupation code from Pole Emploi data.
    Store results in a csv file.
    """
    ROOT_DIR = load_root_path()
    fr_path = os.path.join(ROOT_DIR, "ressources_txt","FR", "nomenclature")
    label_file = os.path.join(fr_path,"ROME_label.csv")
    if os.path.exists(label_file):
        df = pd.read_csv(label_file, encoding="utf-8-sig", sep=";")
        return df
    file = os.path.join(fr_path,"ROME_ArboPrincipale.xlsx")
    if os.path.exists(file):
        xl = pd.ExcelFile(file)
        df = pd.read_excel(file, sheet_name=xl.sheet_names[1])
        cols = df.columns
        # Get ROME code and labels only
        mask = df['Code OGR'] != ' '
        df = df.loc[mask].copy()
        # Get relevant columns
        df["ROME"] = df[cols[0]] + df[cols[1]] + df[cols[2]]
        df.rename(columns={cols[3]: 'titre'}, inplace=True)
        # To csv
        df.to_csv(
                label_file, encoding="utf-8-sig", sep=";", index=False,
                columns=['ROME', 'titre']
                )
        return df
    else:
        print(
                '''*** \n'''
                '''Please download the 'Arborescence principale' file available on'''
                ''' https://www.pole-emploi.org/opendata/repertoire-operationnel-des-meti.html?type=article \n''' 
                '''Put in job_title_processing\\job_title_processing\\ressources_txt\\FR\\nomenclature \n'''
                '''***'''
              )
        return None
    
def get_map_ROME_FAP_FR(file_name=None):
    # TODO
    return None

def get_map_ROME_NAF_FR():
    # TODO
    return None

def get_map_ROME_ISCO_FR():
    # TODO
    return None