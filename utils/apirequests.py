import time, datetime

import requests
import json

from data.config import URL


def get_products_by_category(category):
    url = f"{URL}/api/products?ShowInactive=false&Category={category}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def get_products():
    url = f"{URL}/api/products?ShowInactive=false"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def get_product(id):
    url = f"{URL}/api/products/{id}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def add_to_cart(product_id, user_id):
    url = f"{URL}/api/products/{product_id}/cart/{user_id}"
    response = requests.post(url, verify=False)
    if response.status_code == 200:
        return 'ok'
    else:
        return response.text


def get_cart(user_id):
    print(user_id)
    url = f"{URL}/api/products/from_cart/{user_id}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)

    print(response.status_code, response.text)
    return []


def create_order(user_id, phone_number, delivery_time=int(time.mktime(datetime.datetime.now().timetuple()))):
    url = f"{URL}/api/orders/{user_id}"
    data = {
        "DeliveryTime": delivery_time,
        "PhoneNumber": phone_number
    }
    text = json.dumps(data, ensure_ascii=False).encode('utf-8')
    print(text)
    response = requests.post(url, verify=False,
                             data=text,
                             headers={
                                 "Content-Type": "application/json"
                             })
    if response.status_code == 200:
        return 'ok'
    else:
        return str(response.status_code) + ' ' + response.text


def delete_from_cart(product_id, user_id):
    url = f"{URL}/api/products/{product_id}/cart/{user_id}"
    response = requests.delete(url, verify=False)
    if response.status_code == 200:
        return 'ok'
    else:
        return response.text


def get_order_history(user_id):
    url = f"{URL}/api/orders/{user_id}"

    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def send_code(phone_number):
    return "3122"