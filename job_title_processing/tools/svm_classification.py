# -*- coding: utf-8 -*-
"""
Useful fucntion for classification.
"""

# Functions to split train / test + train / test SVM model

import nltk
import os
import itertools
import pickle

import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

from job_title_processing.tools.occupation_nomenclature import get_nomenclature

def split(X, Y, test_size=0.2, random_state=343265, folder=None, filename=None):
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X.tolist(), Y.tolist(), test_size=test_size,
        random_state=random_state, stratify=Y.tolist()
        )
    
    # Remove empty string
    df_train = pd.DataFrame(list(zip(X_train, Y_train)), columns =['X', 'Y'])
    X_train, Y_train = df_train.loc[X != ''].X, df_train.loc[X != ''].Y
    
    df_test = pd.DataFrame(list(zip(X_test, Y_test)), columns =['X', 'Y'])
    X_test, Y_test = df_test.loc[X != ''].X, df_test.loc[X != ''].Y
    
    # Save data
    if folder is not None:
        os.makedirs(folder) if not os.path.exists(folder) else None
        data = [X_train, X_test, Y_train, Y_test]
        if filename is None:
            filename = "train_test.pickle"
        file = os.path.join(folder, filename)
        with open(file, "wb") as f:
            pickle.dump(data, f)

    return X_train.tolist(), X_test.tolist(), Y_train.tolist(), Y_test.tolist()

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def train_svm(X_train, Y_train, folder=None, C=1, min_df=1, filename=None):
    svm = Pipeline([
        ('vectorize', CountVectorizer(tokenizer=tokenize, min_df=min_df)),
        ('svm', LinearSVC(C=C, max_iter=3000, verbose=True))
        ])
    svm = svm.fit(X_train, Y_train)
    # Save model
    if folder is not None:
        if filename is None:
            filename = "svm" + "_C-" + str(C) + "_mindf-" + str(min_df) + ".pickle"
        file = os.path.join(folder, filename)
        with open(file, 'wb') as f:
            pickle.dump(svm, f)
            f.close()
    return svm

def predict_svm(svm, X):
    prediction = svm.predict(X)
    return prediction

def global_metrics_svm(Y_true, Y_pred, level=1):
    if level==2:
        Y_true = [code[0:3] for code in Y_true]
        Y_pred = [code[0:3] for code in Y_pred]
    if level==3:
        Y_true = [code[0] for code in Y_true]
        Y_pred = [code[0] for code in Y_pred]
    report = metrics.classification_report(
            Y_true, Y_pred, output_dict=True, labels=np.unique(Y_true)
            )
    df = pd.DataFrame(report).transpose()
    print("Accuracy : " + str(metrics.accuracy_score(Y_true, Y_pred)))
    print(df.loc[['micro avg','macro avg','weighted avg']])

def group_by_accuracy(
        df, group_by, Y_test_col="Y_test", Y_pred_col="Y_pred", 
        values=None
        ):
    """Evaluate accuracy on subgroups of test set."""
    accuracy = [] # accuracy in each group
    mean_accuracy = [] # mean of accuracy by label in group
    res_dict = {}
    
    if values is None:
        values = df[group_by].unique()
        
    for group_value in values:
        mask = df[group_by] == group_value
        Y_test_mask = df.loc[mask, Y_test_col]
        Y_pred_mask = df.loc[mask, Y_pred_col]
        # Overall accuracy
        accuracy += [metrics.accuracy_score(Y_test_mask, Y_pred_mask)]
        # Accuracy distribution within group
        distribution_accuracy = []
        for label in np.unique(Y_test_mask):
            mask_rome = df[Y_test_col] == label
            Y_test_label = df.loc[mask_rome, Y_test_col]
            Y_pred_label = df.loc[mask_rome, Y_pred_col]
            distribution_accuracy += [metrics.accuracy_score(Y_test_label, Y_pred_label)]
        mean_accuracy += [np.mean(distribution_accuracy)]
        res_dict[group_value] = distribution_accuracy
        
    res_df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in res_dict.items()]))
    return res_df, accuracy, mean_accuracy

def group_by_f1(df, group_by, Y_test_col="Y_test", Y_pred_col="Y_pred", values=None):
    """Evaluate accuracy on subgroups of test set."""
    macro_f1 = []
    micro_f1 = []
    res_dict = {}
    
    if values is None:
        values = df[group_by].unique()
        
    for group_value in values:
        mask = df[group_by] == group_value
        Y_test_mask = df.loc[mask, Y_test_col]
        Y_pred_mask = df.loc[mask, Y_pred_col]
        # Overall accurracy
        macro_f1_group = metrics.f1_score(
                Y_test_mask, Y_pred_mask, average='macro', 
                labels=np.unique(Y_test_mask)
                )
        macro_f1 += [macro_f1_group]
        micro_f1_group = metrics.f1_score(
                Y_test_mask, Y_pred_mask, average='micro', 
                labels=np.unique(Y_test_mask)
                )        
        micro_f1 += [micro_f1_group]
        # Accuracy distribution within group
        distribution_f1 = []
        for label in np.unique(Y_test_mask):
            mask_rome = df[Y_test_col] == label
            Y_test_label = df.loc[mask_rome, Y_test_col]
            Y_pred_label = df.loc[mask_rome, Y_pred_col]
            
            # Get 0 / 1 vectors 
            test_0_1 = [1] * len(Y_test_label)
            pred_0_1 = (Y_pred_label == Y_test_label)*1
            
#            distribution_f1 += [metrics.accuracy_score(Y_test_label, Y_pred_label)]
            distribution_f1 += [metrics.f1_score(test_0_1, pred_0_1)]
#        mean_accuracy += [np.mean(distribution_accuracy)]
        res_dict[group_value] = distribution_f1
        
    res_df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in res_dict.items()]))
    return res_df, macro_f1, micro_f1


#def get_info(X_train, X_test):
#    if type(X_test) != list:
#        X_test = X_test.tolist()
#    if type(X_train) != list:
#        X_train = X_train.tolist()
#    X = X_train + X_test
#    cv = CountVectorizer()
#    cv_fit = cv.fit_transform(X)
#    word_list = cv.get_feature_names()
#    print("Vocab size: " + str(len(word_list)))
#    return word_list

def plot_cm(y_true, y_pred, figsize=(18,18), normalize=True):
    """Plot the confusion matrix."""
    labels = sorted(list(set(y_true+y_pred)))
    cm = metrics.confusion_matrix(y_true, y_pred, labels)
    fig = plt.figure(figsize=figsize)
    _plot_confusion_matrix(fig, cm = cm, classes=labels, normalize=normalize)
    plt.show()
    return fig

def _plot_confusion_matrix(
            fig, cm, classes, normalize=False, title='Confusion matrix',
            cmap=plt.cm.Blues
        ):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    ax = fig.gca()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar(fraction=0.046, pad=0.04)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    ax.tick_params(grid_alpha=0)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.xlim(-0.5, len(classes)-0.5) # ADD THIS LINE
    plt.ylim(len(classes)-0.5, -0.5) # ADD THIS LINE
    plt.ylabel('True label')
    plt.xlabel('Predicted label')