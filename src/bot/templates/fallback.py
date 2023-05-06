from src.bot.scheme import InputMessage


def msg_default(input_message: InputMessage):
    return f"""
    Hello {input_message.user.full_name}!
    
    I'm sorry that I couldn't assist you with your request. 
    Please hold on for a moment while I transfer you to a human representative who will be able to help you further. 
    Thank you for your patience.
    
    Best regards,
    Support Team
    """
