import pandas as pd

data = pd.read_csv("data/casas_limpio.csv")
data.drop("Unnamed: 0", axis=1, inplace=True)

#-------------------------------------------------
#Yes/No
#-------------------------------------------------

def si_no():
    sn = ["No", "Si"]
    return sn

def sn_bool(resp):
    if resp == "No":
        return 0
    if resp == "Si":
        return 1

#-------------------------------------------------
#House Type
#-------------------------------------------------

ht_dicc = {
    "Piso":0,
    "Dúplex":1,
    "Ático":2,
    "Chalet":3}

def ht_keys():
    return list(ht_dicc.keys())

def ht_value(key):
    return ht_dicc[key]

#-------------------------------------------------
#Neighborhood
#-------------------------------------------------

barrio = data.loc[:,["barrio","distr","barrio_pm2","neighborhood_id"]].groupby("barrio").max()
barrio.reset_index(inplace=True)
dis = list(barrio.distr.unique())

#Create a dictionary with districts as keys and neighborhoods as values. (The values are also dict with the numerical value for each nhood)
d_dicc = {}
for ele in dis:
    df = barrio[barrio["distr"] == ele]
    b_dicc = pd.Series(df.barrio_pm2.values,index=df.barrio).to_dict()
    d_dicc[ele] = b_dicc

def d_keys():
    return sorted(list(d_dicc.keys()))

def b_keys(distr):
    return sorted(list(d_dicc[distr].keys()))

def b_values(distr, nhood):
    return d_dicc[distr][nhood]


#-------------------------------------------------
#Energy efficiency
#-------------------------------------------------

ec_dicc = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 1,
    'En trámite': 0,
    'No indicado': 0,
    'inmueble exento': 0}

def ec_keys():
    return list(ec_dicc.keys())

def ec_value(key):
    return ec_dicc[key]

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Graphics
#---------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------
#Graphics
#-------------------------------------------------

def carga_data():
    data = pd.read_csv("data/casas_limpio.csv")
    return data


def lista_barrios():
    return sorted(list(d_dicc.keys()))

def grafico(distrito):
    data = carga_data()
    data = data[(data["distr"]== f"{distrito}")]
    return data


col_dicc = {
 'm2 Built' : 'sq_mt_built',
 'm2 Usefull' : 'sq_mt_useful',
 'Number of rooms' : 'n_rooms',
 'Number of bathrooms' : 'n_bathrooms',
 'Floor' : 'floor',
 'Rent price' : 'rent_price',
 'Buy price' : 'buy_price',
 'House Type' : 'house_type_id',
 'Prices per m2' : 'barrio_pm2'}

def col_keys():
    return list(col_dicc.keys())

def col_value(key):
    return col_dicc[key]