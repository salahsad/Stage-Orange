import MySQLdb as ms
from tkinter import *

import pandas as pd

#recuperer les colonnes de composant
colonne_eqp_dis = ["ID","SITE","MODELE","MARQUE","RESERVE","ITEM","PORT","MODULE","REFERENCE","QTE"
                   ,"AXE_WDM","S/N","PE","EQP","NBU","KEY","ID_COMPOSANT"]

#tester la connexion à la base de données
try:
    connexion = ms.connect(
                       host ="localhost",database="base_orange",
                       user="root",password="Sani7salah9#")
except:
    print("la connexion ne marche pas ")
def recherche():
    mon_curseur = connexion.cursor() #il me permet dinteragir avec la base de données
    s =vars.get()
    t= vart.get()
    requete_test = "SELECT tb.marque, tb.modele,tb.reserve,l.COMPOSANT, tb.item, tb.port, tb.module, tb.reference, tb.qte, tb.AXE_WDM, tb.PE " \
                   "FROM (SELECT * FROM table_eqp_dis t UNION SELECT * FROM cartes_dis) AS tb " \
                   "INNER JOIN liaison_dis_eqp l ON tb.ID_Composant = l.ID_Composant " \
                   "WHERE tb.site = %s AND l.topologie = %s " \
                   "ORDER BY MODELE"
    mon_curseur.execute(requete_test,(s,t))#il me permet d'executer une requete
    mon_retour=mon_curseur.fetchall()#fetchall me retourne toute les données
    nom_colonnes_dis = ["marque", "modele", "reserve", "composant", "item", "port", "module", "reference", "qte",
                        "AXE_WDM", "PE"]
    if len(mon_retour) > 0:
        zone_text.delete("1.0", END) #supprimer les champs de la zonz de text avant d'ajouter un par un les eqp
        for eqp in mon_retour :
            zone_text.insert("1.0", str(eqp)+"\n") #ajouter les equipement et sauter à la ligne
        dis_avant_excel = pd.DataFrame(list(mon_retour), columns=(nom_colonnes_dis))
        dis_avant_excel.to_excel("fichier_dis.xlsx", header=True, sheet_name="composant")
    else :
        zone_text.insert("1.0","le site n'existe pas")
    vars.set("")
    vart.set("")


    #creation de l'interface graphique
panneau= Tk()
panneau.geometry("600x450")
panneau.title("recuperation des informations")
panneau.resizable(width=False,height=False)
vars=StringVar()
vart=StringVar()
lab = Label(panneau,text="tapez site").place(x=10,y=30)
lab=Label(panneau,text="tapez la topologie").place(x=10,y=60)
ent1 = Entry(panneau,text="....",textvariable=vars,width=20).place(x=100,y=30)
ent2 = Entry(panneau,text="....",textvariable=vart,width=20).place(x=120,y=60)
but = Button(panneau,text="valider",command=recherche).place(x=130,y=120)

zone_text = Text(panneau,width=50,height=10)
zone_text.place(x=30,y=170)

panneau.mainloop()

connexion.commit()
connexion.close()

