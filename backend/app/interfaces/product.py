from typing import Literal
from pydantic import BaseModel, HttpUrl


class ProductUrl(BaseModel):
    url: HttpUrl


class Product(BaseModel):
    product_url: ProductUrl
    name: str
    price: float
    currency: Literal["USD", "ARS"]
    screenshot_url: HttpUrl