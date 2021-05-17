import streamlit as st
from multiapp import MultiApp
from Streamlit import Home, calculator, graphics # import your app modules here
from PIL import Image

app = MultiApp()

imagen = Image.open("Tools/Images/Logo.jpg")
st.image(imagen)

st.markdown("""
# La mejor herramienta de tasacion inmobiliaria
""")

# Add all your application here
app.add_app("Home", Home.app)
app.add_app("Calculador", calculator.app)
app.add_app("Graficos", graphics.app)


# The main app
app.run()