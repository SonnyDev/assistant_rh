import streamlit as st

st.write("Bonjour le monde !")

with st.form("inscription"):
    st.text_input("Votre nom")

    st.text_area("Commentaire")

    age = st.slider("Votre age", 0, 130, 30)

    st.write("Vous avez", age, " ans")

    st.selectbox("Votre ville", ["Paris", "Marseille", "Lille"])

    st.multiselect("Vos couleurs préférées", ["Bleu", "Orange", "Jaune"])

    st.form_submit_button("S'inscrire")