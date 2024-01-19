from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, HttpUrl
from utils import scrape_jiji
from fastapi_pagination import Page, Params


app = FastAPI()
# add_pagination(app)

class Product(BaseModel):
    price: str
    state: str
    descr: str
    loc: str
    short_url: HttpUrl
    # price_list: dict


@app.get("/jiji-products")
async def get_products_data(
    # item: Product,
    product_name: str = Query(..., min_length=2, include_in_schema=True),
    # params: Params = Depends
    ):
    if product_name:
        return scrape_jiji(product_name=product_name)
    else:
        return None
    