import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from pydantic import BaseModel


# app = FastAPI()


# class Product(BaseModel):
#     name: str
#     price: float
#     state: str
#     gen: str
#     loc: str



product_url = f"https://jiji.com.gh/search?query=razor%blade"
response = requests.get(product_url)

soup = BeautifulSoup(response.text, "html.parser")
main_div = soup.body.find_all("div", class_="qa-advert-price")

names = soup.body.find_all("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div")

for i in main_div:
    print(i.text)
for i in names:
    print(i.text)
