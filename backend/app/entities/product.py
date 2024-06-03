from pydantic import BaseModel, HttpUrl


class ProductInputUrl(BaseModel):
    url: HttpUrl
