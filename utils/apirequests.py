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

def get_cart():
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