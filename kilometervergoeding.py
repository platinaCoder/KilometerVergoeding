import streamlit as st

# import pandas as pd

chaufeur = ""
vergoeding_per_km = 0.21
# vergoeding_chariesa = 0
# vergoeding_kevin = 0
# vergoeding_jurre = 0


# st.write("Reiskostenvergoeding overzicht")
# df = pd.DataFrame([["Chariesa", "Kevin", "Jurre"], ["0", "0", "0"]])
# st.dataframe(df, hide_index=True)

dag = st.selectbox(
    "Kies een dag:", ("Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag")
)

match dag:
    case "Dinsdag":
        chaufeur = st.selectbox("Kies de chaufeur:", ("Chariesa", "Kevin"))
    case "Woensdag":
        chaufeur = st.selectbox("Kies de chaufeur:", ("Chariesa", "Kevin"))
    case "Donderdag":
        chaufeur = st.selectbox("Kies de chaufeur:", ("Chariesa", "Kevin"))
    case "Vrijdag":
        chaufeur = st.selectbox("Kies de chaufeur:", ("Chariesa",))
    case "Zaterdag":
        chaufeur = st.selectbox("Kies de chaufeur:", ("Chariesa", "Kevin", "Jurre"))

passagier = st.multiselect(
    "Kies passagier (meerdere opties selecteerbaar):",
    ["Geen", "Chariesa", "Kevin", "Jurre"],
)

if chaufeur == "Chariesa" and passagier == ["Geen"]:
    km = 70.40
    kosten = round(km * vergoeding_per_km, 2)
    st.write(kosten)
if chaufeur == "Kevin" and passagier == ["Geen"]:
    km = 70.50
    kosten = round(km * vergoeding_per_km, 2)
    st.write(kosten)
if chaufeur == "Chariesa" and passagier == ["Kevin"]:
    km = 83.60
    kosten = round(km * vergoeding_per_km, 2)
    st.write(kosten)
if chaufeur == "Kevin" and passagier == ["Chariesa"]:
    km = 79.80
    kosten = round(km * vergoeding_per_km, 2)
    st.write(kosten)
if chaufeur == "Kevin" and passagier == ["Jurre", "Chariesa"]:
    km = 82.10
    kosten = round(km * vergoeding_per_km, 2)
    st.write(kosten)
if chaufeur == "Chariesa" and passagier == ["Jurre", "Kevin"]:
    km = 85.80
    kosten = round(km * vergoeding_per_km, 2)
    st.write(kosten)
if chaufeur == "Jurre":
    st.write("Jurre rijd op kosten van de zaak!")
