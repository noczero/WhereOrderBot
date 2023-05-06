import pickle
from enum import Enum


class IntentCategory(Enum):
    FEEDBACK = 'feedback',
    GENERAL_ENQUIRY = 'general_enquiry',
    OTHER = 'other',
    REFUND_QUESTION = 'refund_question',
    SPAM = 'spam',
    WHERE_IS_MY_ORDER = 'where_is_my_order'


class EntityLabelNER(Enum):
    NO_ENTITY = 'LABEL_0'
    ORDER_ID = 'LABEL_1'


LABEL_TO_INTENT_CLASS = {
    0: IntentCategory.FEEDBACK.value,
    1: IntentCategory.GENERAL_ENQUIRY.value,
    2: IntentCategory.OTHER.value,
    3: IntentCategory.REFUND_QUESTION.value,
    4: IntentCategory.SPAM.value,
    5: IntentCategory.WHERE_IS_MY_ORDER.value,
}


def load_pickle_model(model_path: str) -> any:
    file = open(model_path, 'rb')
    model = pickle.load(file)
    file.close()
    return model


def get_order_id(ner_predictions: list[dict]) -> str:
    pre_process_str = ''
    prev_entity = None
    for ner in ner_predictions:

        # prevent double order id
        if prev_entity and ner['entity'] != prev_entity:
            break

        # match the ORDER_ID tag with LABEL_1
        if ner['entity'] == EntityLabelNER.ORDER_ID.value:
            # concatenate thw word
            pre_process_str += ner['word']
            # keep state
            prev_entity = EntityLabelNER.ORDER_ID.value

    # replace 'R' tp empty space and return
    return pre_process_str.upper().replace('#', ''). \
        replace('(', ''). \
        replace(')', ''). \
        replace('.', '')
