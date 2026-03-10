# Fonction pour ajouter une citation
import requests
import streamlit as st
from loguru import logger

logger.add("logs/sentiment_streamlit.log", rotation="500 MB", level="INFO")

API_URL = "http://127.0.0.1:9000/"


def old_ok_add_citation(citation, url_api):
    try:
        response = requests.post(
            f"{url_api}/analyse_sentiment/", json={"texte": citation}
        )
        response.raise_for_status()
        logger.info(response)
        # p = response.content

    except requests.exceptions.RequestException as e:
        raise SystemExit(e) from None

    return response.json()


def add_citation(citation, url_api):
    try:
        response = requests.post(
            f"{url_api}/analyse_sentiment/", json={"texte": citation}
        )
        response.raise_for_status()
        logger.info(response)
        # p = response.content

    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion à l'API : {e}")
        logger.error(f"Erreur de connexion à l'API : {e}")

        raise SystemExit(e) from None
    except Exception as e:
        st.error(f"Une erreur est survenue: {e}")
        logger.error(f"Une erreur est survenue: {e}")

    return response.json()


st.title("App title: sentiment analyzer")
# st.header("This is the header")
# st.markdown("This is the markdown")
# st.subheader("This is the subheader")
# st.caption("This is the caption")
# st.code("x = 2021")
# st.latex(r""" a+a r^1+a r^2+a r^3 """)
# st.number_input("Pick a number", 0, 10)
# st.text_input("Email address")
# st.date_input("Traveling date")
# st.time_input("School time")
# st.text_area("Description")
# st.file_uploader("Upload a photo")
# st.color_picker("Choose your favorite color")

st.header("Ajouter vos impressions")
with st.form("add_impression_form"):
    citation = st.text_area("Entrez votre phrase")

    submitted = st.form_submit_button("Convertisseur de sentiment")
    if submitted:
        result = add_citation(citation, API_URL)
        # st.write(result)
        st.write("Résultats de l'analyse :")
        st.write(
            f"Polarité négative : {result['neg']}",
            f"Polarité neutre : {result['neu']}",
            f"Polarité positive : {result['pos']}",
            f"Score composé : {result['compound']}",
        )
        if result["compound"] >= 0.05:
            st.write("Sentiment global : Positif 😀")
        elif result["compound"] <= -0.05:
            st.write("Sentiment global : Négatif 🙁")
        else:
            st.write("Sentiment global : Neutre 😐")

        logger.info(f"Résultats affichés: {result}")
