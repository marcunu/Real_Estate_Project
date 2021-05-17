# Import libraries

import streamlit as st
from PIL import Image
import pickle 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import src.manage_data as dat


#Wide confuguration
st.set_page_config(layout="wide")

# Front Page

imagen = Image.open("Tools/Images/Portada2.jpg")
st.image(imagen)

st.title("""
How much is your house worth?
Have you ever wondered what the **`current value`** of your home is?

Are you interested in buying a new property but don't know if its value is in line with the **`market value`**?

Here we help you to check it, please enter the desired information in the boxes.
""")

st.write("""
# Real estate market
After the brick crisis of 2008 the real estate market suffered a very sharp fall, but nowadays prices are increasing.
""")

st.image(Image.open("Tools/Images/Madrid-overall-property-prices.png"))

st.write("""
## Here we help you to check it, please enter the desired information in the boxes.
""")

m2 = st.text_input("""
Introduce los metros cuadrados de tu vivienda
""")

habit = st.text_input("""
¿Cuantas habitaciones tiene tu vivienda?
""")

banos = st.text_input("""
¿Cuantas baños tiene tu vivienda?
""")

piso = st.text_input("""
¿En que piso esta tu vivienda?
""")

nueva = dat.sn_bool(st.selectbox("""
¿Es de obra nueva?
""", dat.si_no()))

reforma = dat.sn_bool(st.selectbox("""
¿Necesita reforma?
""", dat.si_no()))

park = dat.sn_bool(st.selectbox("""
¿Tiene plaza de garaje?
""", dat.si_no()))

exter = dat.sn_bool(st.selectbox("""
¿Es exterior?
""", dat.si_no()))

tipo= dat.ht_value(st.selectbox("""
¿Que tipo de vivienda es?
""", dat.ht_keys()))

distr = st.selectbox("""
Selecciona un distrito
""", dat.d_keys())


barr = dat.b_values(distr, st.selectbox("""
Selecciona un barrio
""", dat.b_keys(distr)))


cert = dat.ec_value(st.selectbox("""
¿Que tipo de certificado energetico tiene?
""", dat.ec_keys()))



market = {
    "sq_mt_built": [m2],
    "n_rooms": [habit],
    "n_bathrooms" : [banos], 
    "floor" : [piso],
    "is_new_development" : [nueva],
    "is_renewal_needed" : [reforma],
    "has_parking": [park],
    "is_exterior" : [exter],
    "tipo" : [tipo],
    "barrio_pm2" : [barr], 
    "e_certificate" : [cert],
    #"rent_price" : [1800]
    
}

market_test = pd.DataFrame(market)
ren_tree = pickle.load(open("Tools/parameters/rent_price/rp_rfr_md9_mf075_ms2", 'rb'))
precio = ren_tree.predict(market_test)
#st.write(precio)

market["rent_price"] = [precio]
market_test = pd.DataFrame(market)
best_tree = pickle.load(open("Tools/parameters/rfr_md8_mf08_ms3_fun", 'rb'))

valoracion = best_tree.predict(market_test)

st.write("""El precio de mercado de tu vivienda es: """, round(valoracion[0],-4))