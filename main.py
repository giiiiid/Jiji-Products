import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from pydantic import BaseModel
# from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()
# add_pagination(app)


class Product(BaseModel):
    ads: str
    prices: list
    names: list
    # price_list: dict


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

    locs = []
    location = soup.body.find_all("div", class_="b-list-advert__region")
    for i in location:
        locs.append(i.span.text.strip())

    descs = []
    desc_tag = soup.body.find_all("div", class_="b-list-advert-base__description-text")
    for i in desc_tag:
        descs.append(i.text.strip().replace("\n", "").replace("*", "").replace("...", ""))


    state = []
    state_tags = soup.body.find_all("div", class_="b-list-advert-base__item-attr")
    for state_tag in state_tags:
        state.append(state_tag.text.strip())

    new_dict = {names: [prices, state, descs, locs,] 
                for names,prices,state,descs,locs, in zip(names, prices, state, descs, locs)}


    # print(results)
    
    final_results.update({"Products stats": new_dict})

    return final_results
