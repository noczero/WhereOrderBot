import unittest

from src.nlp.intent import IntentModel

INTENT_MODEL_PATH = "../model/setfit_model_finetuned.pickle"


class IntentTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(IntentTestCase, self).__init__(*args, **kwargs)
        self.model = IntentModel(model_name_or_path=INTENT_MODEL_PATH)
        self.test_case_dict = {
            'where_is_my_order': "Hello Support Team,\nCan you give me a better idea of where we're at regarding the delivery status timeline of order ref# 55503?\nAlso really interested about keycap types; how different does using PBT material make compared to ABS when typing over longer periods?",
            'feedback': "I'm not satisfied with the build quality of the keyboard I purchased. It feels cheap and flimsy.",
            'other': 'Hello, I was wondering if you sell any other computer peripherals, such as gaming mice or headsets. If so, could you direct me to your website where I can browse your selection? Thank you.',
            'refund_question': "Hi there, I received my custom mechanical keyboard yesterday, but unfortunately, it's not what I expected. Can you please guide me on how to initiate a refund for this order? Thank you.",
            'general_enquiry': "Hi, I am interested in purchasing a custom mechanical keyboard and was wondering if you have any information on the noise levels of the various switches you offer. Can you please provide me with some guidance? Thanks!",
            'spam': "Congratulations! You have won a free iPhone! Click the link below to claim your prize now!"
        }

    def test_predict_where_is_my_order(self):
        result = self.model.predict("Where is my order?")
        self.assertEqual(result, "where_is_my_order")

    def test_predict_all_category(self):
        for actual_intent, prompt in self.test_case_dict.items():
            predict_intent = self.model.predict(prompt)
            self.assertEqual(predict_intent, actual_intent)


if __name__ == '__main__':
    unittest.main()
