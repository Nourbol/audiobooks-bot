import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def get_products():
    text = [
        {
            "id": "71192dd2-726d-4cb5-8897-088659eb4f93",
            "title": "Potato",
            "details": "A main dish",
            "price": 200
        },
        {
            "id": "3c3cc744-658b-4d09-87f5-c5794d82c567",
            "title": "Bread",
            "details": "Additional",
            "price": 50
        },
        {
            "id": "863d3df4-4397-4de1-8282-8080bc20395b",
            "title": "Salt",
            "details": "Additional",
            "price": 200
        }
    ]
    return text

def get_product(id):
    text = [
        {
            "id": "71192dd2-726d-4cb5-8897-088659eb4f93",
            "title": "Potato",
            "details": "A main dish",
            "price": 200
        },
        {
            "id": "3c3cc744-658b-4d09-87f5-c5794d82c567",
            "title": "Bread",
            "details": "Additional",
            "price": 50
        },
        {
            "id": "863d3df4-4397-4de1-8282-8080bc20395b",
            "title": "Salt",
            "details": "Additional",
            "price": 200
        }
    ]
    for key, product in enumerate(text):
        if id == product["title"]:
            return product
