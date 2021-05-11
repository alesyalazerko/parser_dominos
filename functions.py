import pandas as pd

def parse_cards(div):
    res = pd.DataFrame()

    title = ''
    description = ''
    price = ''
    image_link = ''
    item_link = ''

    title = div.find('div', {'class': 'product-card__title'}).text.strip()
    description = div.find('div', {'class': 'product-card__description'}).text.strip()
    price = div.find('p', {'class': 'product-card__modification-info-price'}).text.strip()
    image_link = div.find('img', {'class': 'product-card-media__element'}).get('src').strip()
    item_link = 'https://dominos.by/pizza/' + div.get('data-code').lower()

    res = res.append(pd.DataFrame([[title, description, price, image_link, item_link]],
                                  columns=['Title', 'Ingredients', 'Price', 'Image Link', 'Link to pizza']))
    return res



