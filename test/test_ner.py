import unittest

from src.nlp.ner import NEROrderIDModel

MODEL_PATH = "../model/ner_pretrained_order"


class NERTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(NERTestCase, self).__init__(*args, **kwargs)
        self.model = NEROrderIDModel(model_name_or_path=MODEL_PATH)
        self.test_case_dict = {
            '678910': "Hi, I placed an order for a custom mechanical keyboard on your website recently, but I haven't received any updates on my order (#678910). Can you please let me know when I can expect it to be shipped out?",
        }

    def test_predict_order_id(self):
        result = self.model.predict("My order is #ABD23D")
        self.assertEqual(result, "ABD23D")

    def test_predict_order_id_double(self):
        result = self.model.predict("My order is #ABD23D. Can you BLa bla with id #1324AN")
        self.assertEqual(result, "ABD23D")s

    def test_predict_all_order_id(self):
        for actual_intent, prompt in self.test_case_dict.items():
            predict_intent = self.model.predict(prompt)
            self.assertEqual(predict_intent, actual_intent)


if __name__ == '__main__':
    unittest.main()
