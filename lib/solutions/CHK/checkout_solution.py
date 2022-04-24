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

count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

#overall_total = 0

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    overall_total = 0

    for item in skus:
        if item not in list(product_data.keys()):
            return -1

        count[f"{item}"] += 1

    for item in count:
        if product_data[f"{item}"]["offer"]["is_offer"]:
            price = product_data[f"{item}"]["price"]
            quantity = product_data[f"{item}"]["offer"]["quantity"]
            value = product_data[f"{item}"]["offer"]["value"]

            item_total = value*(count[f"{item}"]//quantity) + price*(count[f"{item}"]%quantity)
        
        else:
            item_total = count[f"{item}"]*product_data[f"{item}"]["price"]

        overall_total += item_total

    return overall_total
