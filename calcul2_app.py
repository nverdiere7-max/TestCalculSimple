import streamlit as st
from calcul2 import multiplier_par_deux

st.title("× 2")

valeur = st.number_input("Valeur 1", value=0.0, key="val1")
st.write("Résultat :", multiplier_par_deux(valeur))

valeur2 = st.number_input("Valeur 2", value=0.0, key="val2")
st.write("Résultat :", multiplier_par_deux(valeur2))

valeur3 = st.slider("Valeur 3", min_value=0.0, max_value=100.0, value=0.0, step=1.0, key="val3")
st.write("Résultat :", multiplier_par_deux(valeur3))


# tableau de valeur
donnees = [
    {"Entrée": "Valeur 1", "Valeur": valeur, "Résultat (× 2)": multiplier_par_deux(valeur)},
    {"Entrée": "Valeur 2", "Valeur": valeur2, "Résultat (× 2)": multiplier_par_deux(valeur2)},
    {"Entrée": "Valeur 3", "Valeur": valeur3, "Résultat (× 2)": multiplier_par_deux(valeur3)},
]

st.subheader("Récapitulatif")
st.table(donnees)


# Génération du contenu CSV en mémoire (utf-8-sig pour une ouverture propre dans Excel)
import csv
import io

buffer = io.StringIO()
writer = csv.DictWriter(buffer, fieldnames=["Entrée", "Valeur", "Résultat (× 2)"])
writer.writeheader()
writer.writerows(donnees)

st.download_button(
    label="📥 Télécharger en CSV (.csv)",
    data=buffer.getvalue().encode("utf-8-sig"),
    file_name="resultats_calculs.csv",
    mime="text/csv",
)