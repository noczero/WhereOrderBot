from pydantic import BaseModel


class StandardResponse:

    def __init__(self, code: int = None, status: str = None, data: any = None, **kwargs):
        self.code = code
        self.status = status
        self.data = data

        # accept any dict with kwargs
        self.__dict__.update(kwargs)
