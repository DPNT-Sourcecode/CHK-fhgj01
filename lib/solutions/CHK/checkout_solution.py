#from lib.solutions.CHK.data import product_data

from functools import total_ordering


product_data = {
    "A": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 3,
                "value": 130
            },
            "offer_2": {
                "quantity": 5,
                "value": 200
            }    
        }
    },
    "B": {
        "price": 30,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 2,
                "value": 45
            }    
        }
    },
    "C": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "D": {
        "price": 15,
        "has_offer": False,
        "offers": {}
    },
    "E": {
        "price": 40,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 2,
                "value": 0,
                "has_action": True,
                "action": {
                    "action_type": "add",
                    "sku_affected": "B",
                    "number": 1
                }
            }
        }
    },    
}



#overall_total = 0

def inspect_offer(offer, sku_quantity):
    if offer["quantity"] >= sku_quantity:
        return True
    else:
        return False

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    overall_total = 0

    count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

    for item in skus:
        print(item)
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
        print(overall_total)

    return overall_total

#print(checkout("AAABBB"))