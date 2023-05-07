from config import settings
from src.bot.request_handler import WhereOrderBot
from src.nlp import NLPModels

nlp_models = NLPModels()
nlp_models.set_intent_model(model_name_or_path=settings.INTENT_MODEL_PATH)
nlp_models.set_ner_model(model_name_or_path=settings.NER_MODEL_PATH)


def get_chat_bot() -> WhereOrderBot:
    return WhereOrderBot(nlp_models=nlp_models)
