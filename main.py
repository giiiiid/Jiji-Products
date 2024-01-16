import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()


class Product(BaseModel):
    ads: str
    prices: []
    names: []


@app.get("/trial")
async def get_products_data(
    item: Product,
    product_name: str = Query(..., min_length=2, include_in_schema=True)
    ):
    product_url = f"https://jiji.com.gh/search?query={product_name}"
    response = requests.get(product_url)
    
    soup = BeautifulSoup(response.text, "html.parser")

    # Number of ads per query
    ads_li_tag = soup.find_all("li", class_="b-breadcrumb-inner")[1]
    num_of_ads = ads_li_tag.div.span.text
    num_ads_results = num_of_ads.split(" ")


    # Prices of items
    prices = []
    product_price = soup.body.find_all("div", class_="qa-advert-price")
    for price in product_price:
        prices.append(price)
    
    
    # Names of products
    names = []
    name_of_product = soup.body.find_all("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div")
    for name in name_of_product:
        names.append(name)

    item.ads = num_ads_results[0]
    item.names = names
    item.prices = prices
    
    results = {"Product name":product_name, "item":item}
    return results