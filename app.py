import requests
import streamlit as st
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Mes items", page_icon="📦")
st.title("📦 Gestion des items")

# --- Formulaire d'ajout ---
st.subheader("Ajouter un item")
with st.form("nouvel_item", clear_on_submit=True):
    nom = st.text_input("Nom")
    prix = st.number_input("Prix (€)", min_value=0.0, step=0.5)
    en_stock = st.checkbox("En stock", value=True)
    envoye = st.form_submit_button("Ajouter")

if envoye:
    if not nom.strip():
        st.warning("Le nom est obligatoire.")
    else:
        try:
            reponse = requests.post(
                f"{API_URL}/items",
                json={"nom": nom, "prix": prix, "en_stock": en_stock},
                timeout=5,
            )
            reponse.raise_for_status()
            st.success(f"« {nom} » a été ajouté.")
        except requests.RequestException as e:
            st.error(f"Erreur lors de l'ajout : {e}")

# --- Liste des items ---
st.subheader("Items existants")
try:
    reponse = requests.get(f"{API_URL}/items", timeout=5)
    reponse.raise_for_status()
    items = reponse.json()
except requests.RequestException:
    st.error("Impossible de joindre l'API. Est-elle bien lancée ?")
    st.stop()

if items:
    st.dataframe(items, use_container_width=True)
else:
    st.info("Aucun item pour le moment.")