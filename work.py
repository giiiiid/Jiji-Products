import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from pydantic import BaseModel
import random
import string
# app = FastAPI()


# class Product(BaseModel):
#     name: str
#     price: float
#     state: str
#     gen: str
#     loc: str



# product_url = f"https://jiji.com.gh/search?query=razor%blade"
# response = requests.get(product_url)

# soup = BeautifulSoup(response.text, "html.parser")
# main_div = soup.body.find_all("div", class_="qa-advert-price")

# ads_li_tag = soup.find_all("li", class_="b-breadcrumb-inner")[1]
# num_of_ads = ads_li_tag.div.span.text
# num_ads_results = num_of_ads.split(" ")

# # names = soup.body.find_all("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div")

# prices = []
# product_price = soup.body.find_all("div", class_="qa-advert-price")
# for price in product_price:
#     prices.append(price.text.strip())

# names = []
# name_of_product = soup.body.find_all("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div")
# for name in name_of_product:
#     names.append(name.text.strip())

# # for i in names:
# #     print(i.text.strip())
# # print(names)
# # print(prices)

# new_dict = {names: prices for names,
#             prices in zip(names, prices)}
# # print(new_dict)
# # print("---------------------------------------------------------")
# results = {
#     "Number of ads": num_ads_results[0],
#     "Item with Prices": new_dict
# }
# descs = []
# desc_tag = soup.body.find_all("div", class_="b-list-advert-base__description-text")
# for i in desc_tag:
#     descs.append(i.text.strip())

# # print(results)
# location = soup.body.find_all("div", class_="b-list-advert__region")
# for i in location:
#     print(i.span.text.strip())

# for i in descs:
#     print(i)
# print(descs)

# generate random letters

# letters = random.choices(string.ascii_lowercase, k=3)
# let = "".join(letters)
# print(let)

import pyshorteners

def short_url(url: str) -> str:
    s_url = pyshorteners.Shortener()
    print( s_url.tinyurl.short(url))

short_url("https://www.google.com")