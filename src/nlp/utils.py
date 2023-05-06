import pickle

LABEL_TO_INTENT_CLASS = {
    0: 'feedback',
    1: 'general_enquiry',
    2: 'other',
    3: 'refund_question',
    4: 'spam',
    5: 'where_is_my_order',
}


def load_pickle_model(model_path: str) -> any:
    file = open(model_path, 'rb')
    model = pickle.load(file)
    file.close()
    return model


def get_order_id(ner_predictions: list[dict]) -> str:
    pre_process_str = ''
    is_order_id = True
    for ner in ner_predictions:
        # match the ORDER_ID tag with LABEL_1
        if ner['entity'] == "LABEL_1" and is_order_id:
            # concatenate thw word
            pre_process_str += ner['word']
            # keep state
            is_order_id = True
        else:
            is_order_id = False

    # replace 'R' tp empty space and return
    return pre_process_str.upper().replace('#', ''). \
        replace('(', ''). \
        replace(')', ''). \
        replace('.', '')
