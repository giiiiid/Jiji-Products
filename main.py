from fastapi import FastAPI, Query
from pydantic import BaseModel
from utils import scrape_jiji
# from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()
# add_pagination(app)

class Product(BaseModel):
    ads: str
    prices: list
    names: list
    # price_list: dict


@app.get("/jiji-products")
async def get_products_data(
    # item: Product,
    product_name: str = Query(..., min_length=2, include_in_schema=True)
    ):
    if product_name:
        return scrape_jiji(product_name=product_name)
    else:
        return None
    