import random

from src.bot.scheme import OrderedProduct, Tracking, InputMessage
from src.bot.templates import where_my_order_intent, fallback

list_product = [
    OrderedProduct(order_id="678910", name="custom mechanical keyboard A",
                   tracking=Tracking(name="FedEx", status="out for delivery", estimate_process_time="2")),

    OrderedProduct(order_id="YY765Z", name="mech keyboard B",
                   tracking=Tracking(name="FedEx", status="shipment information received", estimate_process_time="2")),

    OrderedProduct(order_id="33321", name="custom mechanical keyboard C",
                   tracking=Tracking(name="FedEx", status="in transit", estimate_process_time="1")),

    OrderedProduct(order_id="212223", name="custom mechanical keyboard D",
                   tracking=Tracking(name="FedEx", status="delivery exception", estimate_process_time="4")),

    OrderedProduct(order_id="BB2223", name="custom mechanical keyboard F",
                   tracking=Tracking(name="FedEx", status="delivery exception", estimate_process_time="5")),

    OrderedProduct(order_id="66604", name="custom mechanical keyboard G",
                   tracking=Tracking(name="FedEx", status="out for delivery", estimate_process_time="1")),

    OrderedProduct(order_id="123ABC", name="custom mechanical keyboard H",
                   tracking=Tracking(name="FedEx", status="delivery exception", estimate_process_time="5")),

    OrderedProduct(order_id="YY654E", name="custom mechanical keyboard I",
                   tracking=Tracking(name="FedEx", status="in local facility", estimate_process_time="4")),

    OrderedProduct(order_id="22343", name="custom mechanical keyboard J",
                   tracking=Tracking(name="FedEx", status="shipment information received", estimate_process_time="2")),

    OrderedProduct(order_id="34123", name="custom mechanical keyboard J",
                   tracking=Tracking(name="FedEx", status="delivered", estimate_process_time="0")),
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
        return list_product[random.randint(0, len(list_product)-1)]


def process_where_is_my_order_intent(input_message:InputMessage):
    match input_message.product.tracking.status:
        case "out for delivery":
            return where_my_order_intent.out_of_delivery(input_message=input_message)

        case "shipment information received":
            return where_my_order_intent.delayed_schedule(input_message=input_message)

        case "delivered":
            return where_my_order_intent.delivered(input_message=input_message)

        case "delivery exception":
            return where_my_order_intent.issue_exeception(input_message=input_message)

        case "in local facility":
            return where_my_order_intent.in_local_facility(input_message=input_message)

        case "in transit":
            return where_my_order_intent.in_transit(input_message=input_message)

        case _:
            return fallback.msg_default(input_message=input_message)