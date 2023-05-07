from src.bot.scheme import InputMessage, OrderedProduct, User


def delayed_schedule(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name}! Thank you for providing your order number {input_message.product.name}.
    I apologize for the lack of updates on the estimated shipping date for your {input_message.product.name}.
    - https://e-commerce.example/orders/{input_message.product.order_id}
    
    Based on the current progress, we expect your {input_message.product.name} to be shipped out within the next 
    {input_message.product.tracking.estimate_process_time} business days. 
    Once it's on its way, you will receive a shipping confirmation email with the tracking details.
    Please note that actual delivery times may vary depending on the shipping method and your location.
    I genuinely appreciate your patience and understanding in this matter. 
    
    We value your business and are committed to providing you with a top-notch product. 
    If you have any further questions or concerns, please don't hesitate to let me know.
    
    Best regards,
    Support Team
    """


def out_of_delivery(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name},

    Thank you for getting in touch with us about your {input_message.product.name} order 
    with reference number {input_message.product.order_id}.
    - https://e-commerce.example/orders/{input_message.product.order_id}
    
    We're always happy to help you with any questions or concerns you might have.
    We would be happy to provide you with an update on the timeline for your order. 
    According to our records, your order is currently on {input_message.product.tracking.status} 
    and is expected to be delivered on the next {input_message.product.tracking.estimate_process_time} business days.
    
    We hope this information has been helpful. 
    If you have any further questions or concerns, please don't hesitate to reach out to us.
    
    Best regards,
    Support Team
    """


def in_transit(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name},
    
    Thank you for getting in touch with us about your {input_message.product.name} order 
    with reference number {input_message.product.order_id}. 
    - https://e-commerce.example/orders/{input_message.product.order_id}
    
    Your product is currently {input_message.product.tracking.status} and on its way to its destination. 
    It is expected to be process on the next {input_message.product.tracking.estimate_process_time} business days.
    You can check the tracking information on the shipping carrier's website for 
    more details and estimated delivery date.
    
    We hope this information has been helpful. 
    If you have any further questions or concerns, please don't hesitate to reach out to us.
    
    Best regards,
    Support Team
    """


def in_local_facility(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name},
    
    Thank you for getting in touch with us about your {input_message.product.name} order 
    with reference number {input_message.product.order_id}. 
    - https://e-commerce.example/orders/{input_message.product.order_id}
    
    Your product has arrived at a local facility and is being processed for delivery.
    It should be delivered to you soon. 
    It is expected to be process on the next {input_message.product.tracking.estimate_process_time} business days.
    You can check the tracking information on the shipping carrier's 
    website for more details and estimated delivery date.
    
    We hope this information has been helpful. 
    If you have any further questions or concerns, please don't hesitate to reach out to us.
    
    Best regards,
    Support Team
    """


def delivered(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name},
    
    Thank you for getting in touch with us about your {input_message.product.name} order 
    with reference number {input_message.product.order_id}. 
    - https://e-commerce.example/orders/{input_message.product.order_id}
    
    Great news! Your product has been delivered. Please check your delivery 
    location to confirm the package's arrival. 
    If you have any questions or concerns, don't hesitate to reach out

    Best regards,
    Support Team    
    """


def issue_exeception(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name},
    
    Thank you for getting in touch with us about your {input_message.product.name} order 
    with reference number {input_message.product.order_id}. 
    - https://e-commerce.example/orders/{input_message.product.order_id}
    
    I'm sorry to hear that there's an issue with the delivery of your product. 
    Please check the shipping carrier's website for more information on the issue and possible resolution. 
    If you need further assistance, you can contact the shipping carrier's customer service for help.
    
    Or please hold on for a moment while I transfer you to a human representative 
    who will be able to help you further. 
    Thank you for your patience.

    Best regards,
    Support Team    
    """
