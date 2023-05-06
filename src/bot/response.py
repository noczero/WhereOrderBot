from src.bot.scheme import InputMessage
from src.bot.templates import other_intent, refund_intent, spam_intent, general_enquiry_intent, feedback_intent
from src.bot.utils import process_where_is_my_order_intent
from src.nlp.utils import IntentCategory


class BotResponse:

    def __init__(self, input_message: InputMessage):
        self.input_message = input_message

    def get(self) -> str:
        match self.input_message.intent:
            case IntentCategory.WHERE_IS_MY_ORDER.value:
                return process_where_is_my_order_intent(self.input_message)

            case IntentCategory.REFUND_QUESTION.value:
                return refund_intent.default_msg(self.input_message)

            case IntentCategory.SPAM.value:
                return spam_intent.default_msg(self.input_message)

            case IntentCategory.OTHER.value:
                return other_intent.default_msg(self.input_message)

            case IntentCategory.GENERAL_ENQUIRY.value:
                return general_enquiry_intent.default_msg(self.input_message)

            case IntentCategory.FEEDBACK:
                return feedback_intent.default_msg(self.input_message)

            case _:
                return ''
