import pandas as pd
import numpy as np


#transformation des fichiers excel en fichiers csv
def transformation(excel_path,csv_path):
  excel_file = pd.read_excel(excel_path)
  excel_file_to_csv =excel_file.to_csv(csv_path)
  print("le fichier excel à été converti en un fichier csv qui se trouve à :",csv_path)



'''
transformation("/content/drive/MyDrive/ressources stages/COMPOSANT.xlsx","/content/drive/MyDrive/ressources stages/COMPOSANT.csv")
def nettoyage_données_composant(fichier_csv):
    composant = pd.read_csv(fichier_csv)
    composant = composant.drop("Unnamed: 0",axis=1)
    composant.rename(columns={"PN":"ID_Composant"},inplace=True)
    fichier_sortie = composant.to_csv("/content/drive/MyDrive/ressources stages/Composant_sortie.csv",index=False)
    print("le fichier à bien été nettoyé et sera renommé Composant_sortie")
nettoyage_données_composant("/content/drive/MyDrive/ressources stages/COMPOSANT.csv")



transformation("/content/drive/MyDrive/ressources stages/STOCK.xlsx","/content/drive/MyDrive/ressources stages/STOCK.csv")
def nettoyage_données_stock(fichier_csv):
    stock = pd.read_csv(fichier_csv)
    stock = stock.drop("Unnamed: 0",axis=1)
    stock.rename(columns={"N°":"NUM_STOCK","PN":"ID_COMPOSANT"},inplace=True)
    fichier_sortie = stock.to_csv("/content/drive/MyDrive/ressources stages/STOCK.csv")
    print("le fichier à bien été nettoyé et sera renommé Stock_sortie.CSV")
nettoyage_données_stock("/content/drive/MyDrive/ressources stages/STOCK.csv")
'''









