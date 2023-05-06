import logging

from src.bot.response import BotResponse
from src.bot.scheme import InputMessage, OrderedProduct, User
from src.bot.utils import get_ordered_product
from src.nlp import NLPModels

log = logging.getLogger(__name__)


class WhereOrderBot:

    def __init__(self, nlp_models: NLPModels):
        self.intent_model = nlp_models.get_intent_model()
        self.ner_model = nlp_models.get_ner_model()

    def understanding(self, prompt: str) -> str:
        if not self.intent_model:
            log.error("Intent model not set yet. Please set intent model.")
            return ''

        if not self.ner_model:
            log.error("NER model not set yet. Please set ner model.")
            return ''

        intent = self.intent_model.predict(prompt)
        order_id = self.ner_model.predict(prompt)

        # get product by order id
        ordered_product = get_ordered_product(order_id=order_id)

        # make input message
        input_msg = InputMessage(intent=intent,
                                 product=ordered_product,
                                 user=User(full_name="Satrya Budi Pratama"))

        return BotResponse(input_msg).get()
