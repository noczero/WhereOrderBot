import random

from src.bot.scheme import OrderedProduct, Tracking, InputMessage
from src.bot.templates import where_my_order_intent

list_product = [
    OrderedProduct(order_id="678910", name="custom mechanical keyboard",
                   tracking=Tracking(name="FedEx", status="out for delivery", estimate_process_time="3")),
    OrderedProduct(order_id="123AVS", name="product B",
                   tracking=Tracking(name="DHL", status="shipment information received", estimate_process_time="1"))

]


def get_ordered_product(order_id: str) -> OrderedProduct:
    if order_id != '':
        # search on list
        for product in list_product:
            if product.order_id == order_id:
                # found
                return product

        # not found, return dummy product
        return OrderedProduct(order_id=order_id, name="product A",
                              tracking=Tracking(name="FedEx", status="in transit", estimate_process_time="1"))
    else:
        # get random, assume its latest order id
        return list_product[random.randint(0, len(list_product))]


def process_where_is_my_order_intent(input_message:InputMessage):
    match input_message.product.tracking.status:
        case "out for delivery":
            return where_my_order_intent.out_of_delivery(input_message=input_message)
