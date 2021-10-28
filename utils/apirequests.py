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
    url = f"{URL}/api/products/from_cart/{user_id}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def create_order(user_id, phone_number):
    url = f"{URL}/api/orders/{user_id}"
    response = requests.post(url, verify=False)
    if response.status_code == 200:
        return 'ok'
    else:
        return response.text


def delete_from_cart(id, user_id):
    text = [
        {
            "id": "71192dd2-726d-4cb5-8897-088659eb5555",
            "title": "Olivie",
            "category": "Salad",
            "price": 300
        },
        {
            "id": "71192dd2-726d-4cb5-8897-088659eb4f58",
            "title": "Borsch",
            "category": "First dish",
            "price": 400
        },
        {
            "id": "71192dd2-726d-4cb5-8897-088659eb4f93",
            "title": "Plov",
            "category": "Second dish",
            "price": 700
        },
        {
            "id": "3c3cc744-658b-4d09-87f5-c5794d82c567",
            "title": "Rice",
            "category": "Garnish",
            "price": 130
        }
    ]
    text[:] = [product for product in text if product.get('id') != id]
    return text
