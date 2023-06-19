import pandas as pd
from connexion_bdd import  *
import MySQLdb as ms
import os


try:
    connexion = ms.connect(
                       host ="localhost",database="base_orange",
                       user="root",password="Sani7salah9#")
except:
    print("la connexion ne marche pas ")

#ici je prend les fichiers qui se trouve dans le dossier DIS et je recupere leurs nom
dossier_path = "C:/Users/LFMT9066/PycharmProjects/nettoyage_de_données/DIS/"
liste_des_fichiers=[]
for fichier in os.listdir(dossier_path): #parcourir le dossier et trouver le fichier
  if fichier not in (liste_des_fichiers):
    liste_des_fichiers.append(dossier_path+fichier)

#j'importe la liste des topologie
les_topologie = ["T301","L601T","L601R","L601I","L601D",
                 "L601C","L520","L502A","L502","L421","L411","L310","L302","L301","L220","L211","L202","L120B","L120A","L112","L111","L103","L102","L002B",
                 "L002A","F520","E520","E310","E202","E120B","E120A","DI",
                 "B502","A502A","A301","A120B","A120A","A102"]

nom_site=[]
nom_site1=[]
data_frames = {}
data_frames1= {}
for file in liste_des_fichiers:
  nom=file.split('/')[-1].split('_')[0]
  if nom not in nom_site:
    nom_site.append(nom) #ajouter les noms des sites qui sont pas dans nom_site
    data_frame = pd.read_excel(file,sheet_name="COMPOSANT",header=1)
    data_frames[nom] = data_frame #ici on donnee a la clé nom le dataframe de file

#ici on ajoute chaque nom du site à un dataframe
for key in data_frames.keys() :
  for i in nom_site :
    if key == i:
      data_frames[key]["site"] = i #ajout a la colonne'site' du dataframe le nom du site

#ici pour ajouter les topologie au dataframes
for file in liste_des_fichiers:
    nom = file.split('/')[-1].split('_')[0]
    if nom not in nom_site1:
        nom_site.append(nom)  # ajouter les noms des sites qui sont pas dans nom_site
        data_frame1 = pd.read_excel(file, sheet_name="INDEX", header=1)
        data_frames1[nom] = data_frame1  # ici on donner a la clé nom le dataframe de file
for clé in data_frames1.keys():
    for j in data_frames1[clé]["Unnamed: 43"].str.upper().values:
        for i in les_topologie:
            if j == i:
                data_frames[clé]["topologie"] = i


print(data_frames)
'''
#la fonction duplicated me permet de trouver les colonnes dupliquées et de garder les
#premiere
table_eqp = test[test.duplicated("MODELE")==False]

#recuperer l'index des composant
les_index = table_eqp.index.tolist()
carte = test.drop(index=les_index)

#creation de la table c
table_carte = carte[["ID",'SITE','MODELE','MARQUE', 'RESERVE',"COMPOSANT","ITEM","PORT",
                     "MODULE","REFERENCE","QTE","AXE_WDM","S/N",'PE', 'EQP', 'NBU','KEY']]
#supprimer les enregistrement qui contiennet libre panneaux et cable
table_carte = table_carte.drop(index = table_carte.loc[
(table_carte["MODULE"].str.contains("PANNEAU"))|
(table_carte["MODULE"].str.contains("CABLE"))|
(table_carte["MODULE"].str.contains("Libre"))].index)



#lié grace a des identifiants
#d'abord créer une table liaisons
table_liaison = table_eqp[["COMPOSANT","ITEM"]]
table_liaison.insert(0,"ID_Composant",range(1,1+len(table_liaison)))
table_liaison = table_liaison.drop("ITEM",axis=1)

table_eqp = table_eqp[['ID', 'SITE','MODELE', 'MARQUE', 'RESERVE', 'COMPOSANT', 'ITEM', 'PORT',
       'MODULE', 'REFERENCE', 'QTE', 'AXE_WDM', 'S/N', 'PE', 'EQP', 'NBU',
       'KEY']]
#lié la table eqp avec la table liaison #jointure
table_eqp = table_eqp.merge(table_liaison, on="COMPOSANT",how="left")
table_eqp =  table_eqp.drop("COMPOSANT",axis=1)

#lié la table carte avec la table liaison

table_carte = table_carte.merge(table_liaison , on="COMPOSANT",how="left")
table_carte = table_carte.drop("COMPOSANT",axis=1)

#chargement en base de données

#table_liaison.to_sql('liaison_DIS_eqp'.lower(),con=connexion,if_exists='fail',index=False)
#table_carte.to_sql('CARTES_DIS'.lower(),con=connexion1,if_exists='fail',index=False)
#table_eqp.to_sql('Table_eqp_DIS'.lower(),con=connexion,if_exists='fail',index=False)

#ajouter la topologie à la table




connexion.commit()
connexion.close()
'''