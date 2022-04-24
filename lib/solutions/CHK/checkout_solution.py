#from lib.solutions.CHK.data import product_data

from functools import total_ordering


product_data = {
    "A": {
        "price": 50,
        "offer": {
            "is_offer": True,
            "quantity": 3,
            "value": 130
        }
    },
    "B": {
        "price": 30,
        "offer": {
            "is_offer": True,
            "quantity": 2,
            "value": 45
        }
    },
    "C": {
        "price": 20,
        "offer": {
            "is_offer": False,
            "quantity": 0,
            "value": 0
        }
    },
    "D": {
        "price": 15,
        "offer": {
            "is_offer": False,
            "quantity": 0,
            "value": 0
        }
    },
}

A_count = 0
B_count = 0
C_count = 0
D_count = 0

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for item in skus:
        if item not in list(product_data.keys()):
            return -1

        if item == "A":
            A_count += 1