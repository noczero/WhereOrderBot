from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.logger import logger

from src.api.scheme.chat_scheme import CompletionsWebRequest
from src.bot import get_chat_bot
from src.bot.request_handler import WhereOrderBot

router = APIRouter()

ChatBot = Annotated[WhereOrderBot, Depends(get_chat_bot)]


@router.post("/completions", summary="Answer chat with bot that implements NLP")
async def completions(request: CompletionsWebRequest, chatbot: ChatBot):
    result = chatbot.understanding(request.prompt)
    logger.debug(result)

    web_response = {
        "status": "OK",
        "data": result
    }
    return web_response
