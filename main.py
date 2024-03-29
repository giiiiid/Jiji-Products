from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, HttpUrl
from scrape import get_jiji_products
from fastapi_pagination import Page, Params


app = FastAPI()
# add_pagination(app)




@app.get("/jiji-products")
async def get_products_data(
    # item: Product,
    product_name: str = Query(..., min_length=2, include_in_schema=True),
    # params: Params = Depends
    ):
    if product_name:
        return get_jiji_products(product_name=product_name)
    else:
        return None
    