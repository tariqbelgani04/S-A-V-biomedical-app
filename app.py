import streamlit as st
import pandas as pd

st.title("Plateforme SAV Biomédical")

st.header("Ajouter une panne")

equipement = st.text_input("Type d'équipement")
panne = st.text_input("Description de la panne")
solution = st.text_input("Solution")

if st.button("Enregistrer"):
    st.success("Panne enregistrée !")

st.header("Analyse des pannes")

data = pd.DataFrame({
    "Equipement": ["Pompe A", "Pompe B"],
    "Pannes": [10, 2]
})

st.bar_chart(data.set_index("Equipement"))
