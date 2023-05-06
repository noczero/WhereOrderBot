import unittest

from src.bot.request_handler import WhereOrderBot
from src.bot.scheme import InputMessage, OrderedProduct, Tracking, User
from src.bot.templates import where_my_order_intent
from src.nlp import NLPModels
from test.test_intent import INTENT_MODEL_PATH
from test.test_ner import NER_MODEL_PATH


class BotTestCase(unittest.TestCase):
    def test_response(self):
        nlp_models = NLPModels()
        nlp_models.set_intent_model(model_name_or_path=INTENT_MODEL_PATH)
        nlp_models.set_ner_model(model_name_or_path=NER_MODEL_PATH)

        my_bot = WhereOrderBot(nlp_models=nlp_models)
        result = my_bot.understanding(
            prompt="Hi, I placed an order for a custom mechanical keyboard on your website recently, "
                   "but I haven't received any updates on my order (#678910). Can you please let me know "
                   "when I can expect it to be shipped out?")

        expected_result = where_my_order_intent.out_of_delivery(
            input_message=InputMessage(intent="where_is_my_order",
                                       user=User("Satrya Budi Pratama"),
                                       product=OrderedProduct(order_id="678910", name="custom mechanical keyboard",
                                                              tracking=Tracking(name="FedEx", status="out for delivery",
                                                                                estimate_process_time="3"))
                                       ))

        self.assertEqual(result, expected_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
