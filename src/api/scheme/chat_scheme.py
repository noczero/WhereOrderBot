from pydantic import BaseModel


class CompletionsWebRequest(BaseModel):
    prompt: str

    class Config:
        validate_assignment = True
        schema_extra = {
            "example": {
                "prompt": "Hi, I placed an order for a custom mechanical keyboard on your website recently, "
                          "but I haven't received any updates on my order (#678910). Can you please let me know when "
                          "I can expect it to be shipped out?",
            }
        }