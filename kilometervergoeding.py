import streamlit as st

chaufeur = ""
vergoeding_per_km = 0.21
conn = st.connection("vergoeding_db", type="sql")
km_vergoeding = conn.query("select * from km_vergoeding")


def reset_db():
    with conn.session as s:
        s.execute(
            "CREATE TABLE IF NOT EXISTS km_vergoeding (medewerker TEXT, kilometers REAL, vergoeding REAL);"
        )
        s.execute("DELETE FROM km_vergoeding;")
        km_vergoeding = {"Chariesa": "0", "Kevin": "0", "Jurre": "0"}
        for k in km_vergoeding:
            s.execute(
                "INSERT INTO km_vergoeding (medewerker, kilometers, vergoeding) VALUES (:medewerker, :kilometers, :vergoeding);",
                params=dict(
                    medewerker=k,
                    kilometers=km_vergoeding[k],
                    vergoeding=km_vergoeding[k],
                ),
            )
            s.commit()


def query_db(medewerker, km, kosten):
    data_query = conn.query(
        "SELECT * FROM km_vergoeding WHERE medewerker = :medewerker",
        ttl=3600,
        params=dict({"medewerker": medewerker}),
    )
    query_filter_km = data_query["kilometers"]
    km_to_float = float(query_filter_km)
    query_filter_kosten = data_query["vergoeding"]
    kosten_to_float = float(query_filter_kosten)
    value_sum_km = str(km + km_to_float)
    value_sum_vergoeding = str(kosten + kosten_to_float)
    print("kilometers: ", km_to_float)
    print("vergoeding: ", kosten_to_float)
    print(value_sum_km, value_sum_vergoeding)
    print("\n")
    st.dataframe(data_query, hide_index=True)
    st.write(medewerker, km, kosten)
    with conn.session as s:
        s.execute(
            "UPDATE km_vergoeding SET kilometers = :kilometers WHERE medewerker = :medewerker",
            {
                "kilometers": value_sum_km,
                "medewerker": medewerker,
            },
        )
        s.execute(
            "UPDATE km_vergoeding SET vergoeding = :vergoeding WHERE medewerker = :medewerker",
            {
                "vergoeding": value_sum_vergoeding,
                "medewerker": medewerker,
            },
        )
        s.commit()


st.dataframe(km_vergoeding, hide_index=True)

if st.button("Reset Database!"):
    reset_db()
    st.cache_data.clear()
    st.rerun()

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
    if st.button(label="Submit"):
        query_db(chaufeur, km, kosten)
        st.rerun()
    st.write(kosten)
if chaufeur == "Kevin" and passagier == ["Geen"]:
    km = 70.50
    kosten = round(km * vergoeding_per_km, 2)
    if st.button(label="Submit"):
        query_db(chaufeur, km, kosten)
        st.rerun()
    st.write(kosten)
if chaufeur == "Chariesa" and passagier == ["Kevin"]:
    km = 83.60
    kosten = round(km * vergoeding_per_km, 2)
    if st.button(label="Submit"):
        query_db(chaufeur, km, kosten)
        st.rerun()
    st.write(kosten)
if chaufeur == "Kevin" and passagier == ["Chariesa"]:
    km = 79.80
    kosten = round(km * vergoeding_per_km, 2)
    if st.button(label="Submit"):
        query_db(chaufeur, km, kosten)
        st.rerun()
    st.write(kosten)
if (
    chaufeur == "Kevin"
    and passagier == ["Jurre", "Chariesa"]
    or passagier == ["Chariesa", "Jurre"]
):
    km = 82.10
    kosten = round(km * vergoeding_per_km, 2)
    if st.button(label="Submit"):
        query_db(chaufeur, km, kosten)
        st.rerun()
    st.write(kosten)
if (
    chaufeur == "Chariesa"
    and passagier == ["Jurre", "Kevin"]
    or passagier == ["Kevin", "Jurre"]
):
    km = 85.80
    kosten = round(km * vergoeding_per_km, 2)
    if st.button(label="Submit"):
        query_db(chaufeur, km, kosten)
        st.rerun()
    st.write(kosten)
if chaufeur == "Jurre":
    st.write("Jurre rijd op kosten van de zaak!")
