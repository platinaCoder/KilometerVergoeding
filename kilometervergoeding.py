import streamlit as st

# import pandas as pd

chaufeur = ""
vergoeding_per_km = 0.21
conn = st.connection("vergoeding_db", type="sql")

with conn.session as s:
    s.execute(
        "CREATE TABLE IF NOT EXISTS km_vergoeding (medewerker TEXT, kilometers TEXT, vergoeding TEXT);"
    )
    s.execute("DELETE FROM km_vergoeding;")
    km_vergoeding = {"Chariesa": "0", "Kevin": "0", "Jurre": "0"}
    for k in km_vergoeding:
        s.execute(
            "INSERT INTO km_vergoeding (medewerker, kilometers, vergoeding) VALUES (:medewerker, :kilometers, :vergoeding);",
            params=dict(
                medewerker=k, kilometers=km_vergoeding[k], vergoeding=km_vergoeding[k]
            ),
        )
        s.commit()

km_vergoeding = conn.query("select * from km_vergoeding")
st.dataframe(km_vergoeding)

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
