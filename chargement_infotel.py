import pandas as pd

from connexion_bdd import *

#chargement_en_base("fichier infotel\INUIT-RC01 - Parc Equipement INUIT.xlsx","REF_INFOTEL_RC01")
#chargement_en_base("fichier infotel\INUIT-RC01 - Parc Equipement INUIT et HORUS WDM.xlsx","REF_INFOTEL_INUIT_HORUSWDM")
#chargement_en_base("fichier infotel\INUIT-RC02 - Extractions Circuits INUIT.xlsx","RC02_Extractions_Circtuis")
#chargement_en_base("fichier infotel\INUIT-RC02 - Extractions Circuits INUIT et HORUS WDM.xlsx","RC02_Extractions_Circtuis_INUIT_et_HorusWDM")
#chargement_en_base("fichier infotel\INUIT-RC03 - Extractions Eléments Intermédiaires Circuits INUIT.xlsx","RC03_Extractions_Elements_intermediares_Circtuis_INUIT")
#chargement_en_base("fichier infotel\INUIT-RC03 - Extractions Eléments Intermédiaires Circuits INUIT et HORUS WDM.xlsx","RC03_Extractions_Elements_intermediares_Circtuis_INUIT_HORUS_WDM")
#chargement_en_base("fichier infotel\INUIT-RC04 - Extractions Eléments Extrémités Circuits INUIT.xlsx","RC04_Extractions_Elements_Extremites_Circtuis_INUIT")
#chargement_en_base("fichier infotel\INUIT-RC05 - Extractions Signaux Applicatifs INUIT.xlsx","RC05_Extractions_Signaux_Applicatifs")
#chargement_en_base("fichier infotel\INUIT-RC06 - Extractions Eléments Intermédiaires Itinéraire Signaux Applicatifs INUIT.xlsx","RC06_Extractions_Signaux_Applicatifs")
#chargement_en_base("fichier infotel\INUIT-RC06 - Extractions Eléments Intermédiaires Itinéraire Signaux Applicatifs INUIT-EVOLUTION.xlsx","RC06_Extractions_Signaux_Applicatifs-EVOLUTION")
#chargement_en_base("fichier infotel\INUIT-RC07 - Extractions Eléments Extrémité Itinéraire Signaux Applicatifs INUIT.xlsx","RC07_Extractions_Itineraire_Signaux_Applicatifs")
#chargement_en_base("fichier infotel\INUIT-RC07 - Extractions Eléments Extrémité Itinéraire Signaux Applicatifs INUIT-EVOLUTION.xls","RC07_Extractions_Itineraire_Signaux_Applicatifs-EVOLUTION")
#chargement_en_base("fichier infotel\INUIT-RC08 - Extractions Services INUIT.xlsx","RC08_EXTRACTIONS_SERVICES_INUIT")
#chargement_en_base("fichier infotel\INUIT-RC09 - Extractions Services INUIT - Services Métier.xlsx","RC09_EXTRACTIONS_SERVICES_Metier")
#chargement_en_base("fichier infotel\INUIT-RC10 - Points d'Accès INUIT.xlsx","RC10 - Points d'Accès INUIT")
#chargement_en_base("fichier infotel\INUIT-RC11 - Eléments de Réseau WDM.xlsx","RC11 - Elements de Réseau WDM")
#chargement_en_base("fichier infotel\INUIT-RC11 - Eléments de Réseau WDM INUIT et HORUS WDM.xlsx","RC11 - Elements de Réseau WDM_HORUS")
#chargement_en_base("fichier infotel\INUIT-RC12 - Extraction Supports de Transmission Optique.xlsx","RC12 - Elements de Réseau WDM_HORUS")
#chargement_en_base("fichier infotel\INUIT-RC13.a - Extraction Cartes INUIT.xlsx","RC13.a_Cartes_Inuit")
#chargement_en_base("fichier infotel\INUIT-RC13.b - Extraction Cartes INUIT.xlsx","RC13.b_Cartes_Inuit")
#chargement_en_base("fichier infotel\INUIT-RC13.b - Extraction Cartes INUIT et HORUS WDM.xlsx","RC13.b_Cartes_Inuit_HorusWDM")
#chargement_en_base("fichier infotel\INUIT-RC14 - Extraction Baies.xlsx","RC14_Extraction_Baies")
#chargement_en_base("fichier infotel\INUIT-RC15 - Extraction Cordons de Câble.xlsx","RC15_Extraction_Cordons_Cable")
#chargement_en_base("fichier infotel\INUIT-RC16 - Extraction des Services Métier portés par SA INUIT-Description KO.xlsx","RC16_Extraction_Services_Metier_Description_KO")
#chargement_en_base("fichier infotel\INUIT-RC17 - Extraction WDM ROSE.xlsx","RC17_Extraction_WDM_ROSE")
#chargement_en_base("fichier infotel\INUIT-RC18 - Extraction des Slots Equipements et Cartes.xlsx","RC18_Extraction_Slots_Equipement_Cartes")
#chargement_en_base("fichier infotel\INUIT-RC19 - Extraction des Versions Equipements et Cartes.xlsx","RC19_Versions_Slots_Equipement_Cartes")
#chargement_en_base("fichier infotel\INUIT-RC20.b - Extraction des Sites RTE et Projet.xlsx","RC20.b_Extraction_Sites_RTE_Projet")
#chargement_en_base("fichier infotel\INUIT-RC20 - Extraction des Sites RTE.xlsx","RC20_Extraction_Sites_RTE")
#chargement_en_base("fichier infotel\INUIT-RC21 - Extraction OMS et Lambda WDM.xlsx","RC21_Extraction_OMS_Lambda_Wdm")
#chargement_en_base("fichier infotel\INUIT-RC22 - Extraction ELTEK.xlsx","RC22_Extraction_ELTEK")
#chargement_en_base("fichier infotel\INUIT-RC23 - Extraction Répartiteur Cuivre, Réglettes et D.I.G.xlsx","RC23_Extraction_Répartiteur_Cuivre_reglettes_dig")
#chargement_en_base("fichier infotel\INUIT-RC24 - Extraction Supports de Transmission Cuivre.xlsx","RC24_Extraction_Supports_Transmission_Cuivre")
#chargement_en_base("fichier infotel\INUIT-RC25.b - Support de Transmission et TCAB.xlsx","RC25.b_Extraction_Supports_Transmission_TCAB")
#chargement_en_base("fichier infotel\INUIT-RC25 - Support de Transmission et TCAB.xlsx","RC25_Supports_Transmission_TCAB")
#chargement_en_base("fichier infotel\INUIT-RC26 - Porteurs des Liens INUIT-WDM et INUIT-IP.xlsx","RC26_Porteur_Liens_WDM_IP")
#chargement_en_base("fichier infotel\INUIT-RC27 - Liens INUI-IP WDM.xlsx","RC27 - Liens INUI-IP WDM.xlsx")
#chargement_en_base("fichier infotel\INUIT-RC28 - Extractions Eléments Extrémités Porteurs et Ressources.xlsx","RC28 - Liens INUI-IP WDM.xlsx")
#chargement_en_base("fichier infotel\INUIT-RC29 - Extraction des Ports, Ressources et Liens TCM.xlsx","RC29_Extraction_Ports_Ressources_Liens")
#chargement_en_base("fichier infotel\INUIT-RC30 - Extraction des Circuits Fictifs.xlsx","RC30_Extractions_Circuits_Fictifs")



#union des tables RC01 et RC22
rc01 = pd.read_excel("fichier infotel\INUIT-RC01 - Parc Equipement INUIT.xlsx",header=4)
rc22 = pd.read_excel("fichier infotel\INUIT-RC22 - Extraction ELTEK.xlsx",header=4)
for i in rc01.columns :
    se_trouve=False
    for j in rc22.columns:
        if i==j :
            se_trouve=True
            break
    if se_trouve==False:
        print("les colonnes de rc01 qui ne se trouvent pas dans rc02 sont {}".format(i))
rc01 = rc01.drop(["REF_EXT_SS_PROJET","PART_NUMBER_NOUVEAU","N° de catalogue"],axis=1)
#rc01.to_sql("RC01_REF_INFOTEL".lower(),con=connexion,if_exists='fail',index=False)
#rc22.to_sql("RC22_REF_INFOTEL".lower(),con=connexion,if_exists='fail',index=False)
table_jointe = pd.concat([rc01,rc22]).drop_duplicates()
table_jointe.to_sql('RC01_RC22_union'.lower(),con=connexion,if_exists='fail',index=False)
print(table_jointe.count())




