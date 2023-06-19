import pandas as pd

#creation des tables site et topologie
site_topo = pd.read_excel("fichier infotel\INUIT-RC20.b - Extraction des Sites RTE et Projet.xlsx",header=4,index_col=None)
les_s_topo = site_topo[["SITE_NAME","CODE_NOMENCLATURE_SOUS_PROJET"]]

for index,topo in enumerate(site_topo["CODE_NOMENCLATURE_SOUS_PROJET"].unique()) :
    site_topo.loc[site_topo["CODE_NOMENCLATURE_SOUS_PROJET"]==topo,"ID_TOPO"] = "ID" + str(index)
les_s_topo = site_topo[["SITE_NAME","ID_TOPO","CODE_NOMENCLATURE_SOUS_PROJET"]]
les_s_topo["CODE_NOMENCLATURE_SOUS_PROJET"].fillna("NON_RENSEIGNE",inplace=True)
les_s_topo = les_s_topo[~les_s_topo["CODE_NOMENCLATURE_SOUS_PROJET"].str.startswith("L6")]#enlevez les topo L6 "radio"

table_site = les_s_topo[["SITE_NAME","ID_TOPO"]]
table_topologie = les_s_topo[["ID_TOPO","CODE_NOMENCLATURE_SOUS_PROJET"]].rename(columns={"CODE_NOMENCLATURE_SOUS_PROJET":"CODE_TOPO"})
table_topologie["ID_TOPO"].fillna("ID_Manquant",inplace=True)
table_site["ID_TOPO"].fillna("ID_Manquant",inplace=True)
table_topologie["CODE_TOPO"].fillna("NON_RENSEIGNE",inplace=True)


#lié les equipements avec les topologies

eqp = pd.read_csv("EQP_sortie.CSV",index_col=0)

liste = eqp[eqp["RESERVE"].isnull()]["CODNAT"].unique()

liste2= table_site[table_site["SITE_NAME"].apply(lambda x: x in liste)]["ID_TOPO"].unique()
print(table_topologie[table_topologie["ID_TOPO"].apply(lambda x : x in liste2)]["CODE_TOPO"].unique())
print(table_site[table_topologie["ID_TOPO"] == "ID11"])

