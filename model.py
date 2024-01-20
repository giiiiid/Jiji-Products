from pydantic import BaseModel, HttpUrl


class Product(BaseModel):
    product_name: str
    num_of_ads: str
    stats: list
    
    # price_list: dict