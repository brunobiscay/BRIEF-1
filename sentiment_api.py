# doc interessante
# https://stackoverflow.com/questions/50934876/vader-sentiment-analysis-how-are-the-individual-words-rated

# from nltk.sentiment import SentimentIntensityAnalyzer

from fastapi import FastAPI, HTTPException
from loguru import logger
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pydantic import BaseModel


class Texte(BaseModel):
    texte: str


def old_analyse_text_client(input_text: Texte, logger):
    logger.info(f"Analyse du texte: {input_text}")

    analyser = SentimentIntensityAnalyzer()
    proba_sentiment = analyser.polarity_scores(input_text.texte)
    logger.info(f"Résultats: {proba_sentiment}")

    # "Il fait beau aujourd'hui"
    # {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

    # "Il fait beau aujourd'hui, c'est cool"
    # {'neg': 0.0, 'neu': 0.685, 'pos': 0.315, 'compound': 0.3182}

    return proba_sentiment


def analyse_text_client(input_text: Texte, logger):
    logger.info(f"Analyse du texte: {input_text}")

    try:
        analyser = SentimentIntensityAnalyzer()
        proba_sentiment = analyser.polarity_scores(input_text.texte)
        logger.info(f"Résultats: {proba_sentiment}")
        return proba_sentiment
    # "Il fait beau aujourd'hui"
    # {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

    # "Il fait beau aujourd'hui, c'est cool"
    # {'neg': 0.0, 'neu': 0.685, 'pos': 0.315, 'compound': 0.3182}

    except Exception as e:
        logger.error(f"Erreur lors de l'analyse: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Configuration de Loguru
logger.add("logs/sentiment_api.log", rotation="500 MB", level="INFO")

# Configuration API coté serveur
app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


donnees = {"sentiments": ["Amour", "Haine", "Honte"]}


@app.get("/sentiments")
async def get_lieux():
    return {"donnees": donnees}


@app.post("/analyse_sentiment")
async def analyse_sentiment(texte_object: Texte):
    return analyse_text_client(texte_object, logger)

    # client = TestClient(app)
    # print(client.get("/sentiments"))

    # print(analyse_sentiment("Il fait beau aujourd'hui, c'est cool", logger))

    # def test_read_main():
    # response = client.get("/")
    # assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}


#
# try:
#    response = requests.get(url, headers=headers, timeout=0.0001)
# except requests.Timeout as error:
#    print(error)
#

# print(analyse_reponse_model_vader("Il fait vraiment beau aujourd'hui, c'est cool"))
