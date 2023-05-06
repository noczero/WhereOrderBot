from src.bot.scheme import InputMessage


def default_msg(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name}! Thank you for reaching out.
     
    I understand that you have questions regarding a potential refund. We would be happy to help you with this. 

    Could you please provide us relevant details about your purchase so that we can look into this further for you? 
    Once we have reviewed your purchase, we can provide you with more information regarding our refund policy and options available to you. 
    
    Thank you for your cooperation and we look forward to resolving this matter for you.
    
    Best regards,
    Support Team
    """