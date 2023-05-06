from setfit import SetFitModel, SetFitTrainer

from src.utils import LABEL_TO_INTENT_CLASS


class IntentModel:

    def __init__(self, model_name_or_path: str) -> None:
        self.model = SetFitModel.from_pretrained(
            model_name_or_path
        )

    def predict(self, prompt: str):
        label_prediction = self.model([prompt])
        return LABEL_TO_INTENT_CLASS[label_prediction.item()]
