from src.bot.scheme import InputMessage, OrderedProduct, User


def delayed_schedule(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name}! Thank you for providing your order number {input_message.product.name}.
    I apologize for the lack of updates on the estimated shipping date for your {input_message.product.name}.
    
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

    Thank you for getting in touch with us about your {input_message.product.name} order with reference number {input_message.product.order_id}. 
    We're always happy to help you with any questions or concerns you might have.

    We would be happy to provide you with an update on the timeline for your order. 
    According to our records, your order is currently on {input_message.product.tracking.status} 
    and is expected to be delivered on the next {input_message.product.tracking.estimate_process_time}.
    
    We hope this information has been helpful. If you have any further questions or concerns, please don't hesitate to reach out to us.
    
    Best regards,
    Support Team
    """
