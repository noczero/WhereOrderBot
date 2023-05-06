from src.nlp.utils import LABEL_TO_INTENT_CLASS, load_pickle_model


class IntentModel:

    def __init__(self, model_name_or_path: str) -> None:
        self.model = load_pickle_model(model_name_or_path)

    def predict(self, prompt: str):
        label_prediction = self.model([prompt])
        return LABEL_TO_INTENT_CLASS[label_prediction.item()]
