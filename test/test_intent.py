from unittest import TestCase
import logging
from src.intent import IntentModel

# Set log level
loglevel = logging.DEBUG
logging.basicConfig(level=loglevel)
log = logging.getLogger(__name__)


def test_intent():
    my_model = IntentModel(model_name_or_path="lewtun/my-awesome-setfit-model")
    result = my_model.predict("Hello world!")
    assert result == "feedback"