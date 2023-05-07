from src.bot.scheme import InputMessage


def default_msg(input_message:InputMessage):
    return f"""
    Hello {input_message.user.full_name}!

    I apologize, but I'm not programmed to handle those similar question yet. 
    Could you please ask me another question?
    """