import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()


class Product(BaseModel):
    ads: str
    prices: list
    names: list


@app.get("/trial")
async def get_products_data(
    # item: Product,
    product_name: str = Query(..., min_length=2, include_in_schema=True)
    ):

    final_results = {"Product Name": product_name.title()}

    product_url = f"https://jiji.com.gh/search?query={product_name}"
    response = requests.get(product_url)
    
    soup = BeautifulSoup(response.text, "html.parser")

    # Number of ads per query
    ads_li_tag = soup.find_all("li", class_="b-breadcrumb-inner")[1]
    num_of_ads = ads_li_tag.div.span.text
    num_ads_results = num_of_ads.split(" ")
    final_results.update({"Number of ads": num_ads_results[0]})

    # Prices of items
    prices = []
    product_price = soup.body.find_all("div", class_="qa-advert-price")
    for price in product_price:
        prices.append(price.text.strip())
    
    
    # Names of products
    names = []
    name_of_product = soup.body.find_all("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div")
    for name in name_of_product:
        names.append(name.text.strip())

    # item.ads = num_ads_results[0]
    # item.names = names
    # item.prices = prices
    
    # results = {"Product name":product_name, "item":item}
    # results = zip(names, prices)
    new_dict = {names: prices for names,prices in zip(names, prices)}
    final_results.update({"Products with Prices": new_dict})
    return final_results