import requests
from bs4 import BeautifulSoup
from utils import create_short_url


def get_jiji_products(product_name: str):
    final_results = {"Product Name": product_name.title()}

    product_url = f"https://jiji.com.gh/search?query={product_name}"
    response = requests.get(product_url)
    
    if response.status_code == 200:
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


        # Location of products
        locs = []
        location = soup.body.find_all("div", class_="b-list-advert__region")
        for i in location:
            locs.append(i.span.text.strip())


        # Products description
        descs = []
        desc_tag = soup.body.find_all("div", class_="b-list-advert-base__description-text")
        for i in desc_tag:
            descs.append(i.text.strip().replace("\n", "").replace("*", "").replace("...", ""))


        # Product state...Used or Brand new
        state = []
        state_tags = soup.body.find_all("div", class_="b-list-advert-base__item-attr")
        for state_tag in state_tags:
            state.append(state_tag.text.strip())


        # Product url
        url_div_tag = soup.body.find_all("div", class_="b-list-advert__gallery__item js-advert-list-item")
        prefix = "https://jiji.com.gh"
        urls = [create_short_url(f"{prefix}{i.a.get("href")}") for i in url_div_tag]     
        

        # Dict to handle all key, value
        new_dict = {names: [prices, state, descs, locs, urls] 
                    for names,prices,state,descs,locs,urls in zip(names, prices, state, descs, locs, urls)}

        # print(new_dict[prices])
        # final results
        final_results.update({"Products stats": new_dict})
        return final_results
    
    else:
        return None
