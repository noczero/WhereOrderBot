from src.nlp.intent import IntentModel
from src.nlp.ner import NEROrderIDModel


class NLPModels:
    def __init__(self):
        self._intent_model = None
        self._ner_model = None

    def set_intent_model(self, model_name_or_path: str) -> any:
        self._intent_model = IntentModel(model_name_or_path)

    def set_ner_model(self, model_name_or_path: str) -> any:
        self._ner_model = NEROrderIDModel(model_name_or_path)

    def get_intent_model(self):
        return self._intent_model

    def get_ner_model(self) -> any:
        return self._ner_model
