import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def get_products_by_category(category):
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
    text[:] = [product for product in text if product.get('category') == category]
    return text


def get_product(id):
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
    for key, product in enumerate(text):
        if id == product["id"]:
            return product


def add_to_cart(product_id, user_id):
    return True


def create_order(user_id, phone_number):
    pass


def get_cart(user_id):
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
    return text


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
