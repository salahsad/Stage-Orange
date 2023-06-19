import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

from main import *

connexion1 = create_engine('mysql+mysqlconnector://root:Sani7salah9#@localhost:3306/base_orange')


def chargement_en_base(nom_du_fichier,nom_de_la_table):
    if nom_du_fichier.endswith('.xlsx') :
        excel_file = pd.read_excel(nom_du_fichier,header=4)
        excel_file.to_sql(nom_de_la_table.lower(),con=connexion1, if_exists='fail',index=False)
    if nom_du_fichier.endswith('.csv') :
        csv_file = pd.read_csv(nom_du_fichier)
        csv_file.to_sql(nom_de_la_table.lower(),con=connexion1,if_exists='fail',index=False)



#chargement_en_base("INPUT_BESOIN_PORT.xlsm","INPUT_BESOIN_PORT")
#chargement_en_base("INPUT EB_WOP.xlsm","INPUT EB_WOP")
#chargement_en_base("INPUT EB_ROOPT.xlsm","INPUT EB_ROOPT")
#chargement_en_base("INPUT EB_TAC.xlsm","INPUT EB_TAC")





