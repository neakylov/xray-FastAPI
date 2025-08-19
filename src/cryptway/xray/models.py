from pydantic import BaseModel

class Client(BaseModel):
    uuid: str
    flow: str