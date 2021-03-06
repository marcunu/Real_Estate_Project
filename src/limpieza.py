import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def download_kaggle():
    '''
    This function downloads, unzip, delet zip file and move to data folder, a dataset from kaggle.
    Finally returns the dataset.
    Arg:
         
    '''
    #Firs of all, download the file

    os.system("kaggle datasets download -d mirbektoktogaraev/madrid-real-estate-market")
    print("Kaggle file downloaded.")

    #we need to unzip the file
    os.system("unzip madrid-real-estate-market.zip")
    print("Kaggle file unzipped.")

    #Delete the zip file and the old version
    os.system("rm -rf madrid-real-estate-market.zip")
    print("zip file deleted.")

    #Move to data folder
    os.system("mv houses_Madrid.csv data/houses_Madrid.csv")
    print("Files moved to data folder.")

    return "DataFrame downloaded correctly as madrid-real-estate-market."


def heat_map_triangle(df):
    '''
    This function creates a heat map from a selected dataframe
    '''
    sns.set_theme(style="white")

    # Compute the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    return sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5,annot=True, cbar_kws={"shrink": .5})

 