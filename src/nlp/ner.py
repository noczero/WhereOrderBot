from transformers import pipeline
from src.nlp.utils import get_order_id


class NEROrderIDModel:

    def __init__(self, model_name_or_path: str) -> None:
        self.model = pipeline(task="ner", model=model_name_or_path)

    def predict(self, prompt: str) -> str:
        # give a list of token classification in dict.
        ner_predictions = self.model(prompt)
        return get_order_id(ner_predictions)
