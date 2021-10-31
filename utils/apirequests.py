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
    pass


def get_order_history():
    text = [
        {
            "orderId": "90da4da1-2077-487a-b2be-ca2aac5455a2",
            "orderCode": 0,
            "phoneNumber": 87771990938,
            "deliveryTime": "0001-01-01T00:00:00",
            "orderStatus": 0,
            "products": [
                {
                    "id": "34337a0c-faab-4a55-8681-e9fde49feac8",
                    "title": "Olivie",
                    "details": "string",
                    "price": 110,
                    "category": "Salads 🥗",
                    "isActive": True,
                    "isDeleted": False
                }
            ]
        },
        {
            "orderId": "90da4da1-2077-487a-b2be-ca2aac547777",
            "orderCode": 1,
            "phoneNumber": 87771990938,
            "deliveryTime": "0001-01-01T00:00:00",
            "orderStatus": 3,
            "products": [
                {
                    "id": "34337a0c-faab-4a55-8681-e9fde49feac8",
                    "title": "Olivie",
                    "details": "string",
                    "price": 110,
                    "category": "Salads 🥗",
                    "isActive": True,
                    "isDeleted": False
                },
                {
                    "id": "71192dd2-726d-4cb5-8897-088659eb4f58",
                    "title": "Borsch",
                    "details": "string",
                    "price": 400,
                    "category": "First dish",
                    "isActive": True,
                    "isDeleted": False
                }
            ]
        }
    ]

    return text
