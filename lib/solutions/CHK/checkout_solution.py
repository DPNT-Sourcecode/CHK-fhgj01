#from lib.solutions.CHK.data import product_data

# from fcntl import F_SEAL_SEAL
# from functools import total_ordering


product_data = {
    "A": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 5,
                "value": 200,
                "has_action": False
            },
            "offer_2": {
                "quantity": 3,
                "value": 130,
                "has_action": False
            }    
        }
    },
    "B": {
        "price": 30,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 2,
                "value": 45,
                "has_action": False
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
                "quantity": 1,     #quantity of 1 doesn't break the maths by not dividing by 0
                "value": 0,        #value of 0 allows for skipping of offer price reduction
                "has_action": True,
                "action": {
                    "quantity": 2,
                    "action_type": "free_item",     # one free B item won't change the value of the total
                    "sku_affected": "B",            # so this offer won't affect anything and is not needed in calculation
                    "number": 1                     # turns out this is not the case :(
                }
            }
        }
    },    
}



#overall_total = 0

def do_action(offer, count_dict, item, product_data):
    if offer["action"]["action_type"] == "free_item":
        eligable_items_number = count_dict[f'{item}'] / offer["action"]["quantity"]
        if eligable_items_number < count_dict[f'{offer["action"]["sku_affected"]}']:
            items_removed = eligable_items_number
        else:
            items_removed = count_dict[f'{offer["action"]["sku_affected"]}']
        
        print('items removed', items_removed)

        offer_count = 0
        discount = 0

        if product_data[f"{offer['action']['sku_affected']}"]["has_offer"]:
            for offer_name, offer_details in product_data[f"{offer['action']['sku_affected']}"]["offers"].items():
                offer_count += 1
                print(f"in action, count of {offer['action']['sku_affected']} is", items_removed)
                print(offer_details)
                price = product_data[f"{offer['action']['sku_affected']}"]["price"]
                quantity = offer_details["quantity"]
                value = offer_details["value"]

                item_total = value*(items_removed//quantity)
                # print('item total:', item_total)

                discount += item_total #+ price*(count[f"{item}"]%quantity)

                if quantity != 1:
                    items_removed -=  (items_removed//quantity)*quantity
                print(f"in action, count of {offer['action']['sku_affected']} is", items_removed)

                if offer_count == (len(list(product_data[f"{offer['action']['sku_affected']}"]["offers"].items()))):
                    discount += items_removed*product_data[f"{offer['action']['sku_affected']}"]["price"]
                    items_removed = 0
                    print(f"count of {offer['action']['sku_affected']} is", items_removed)

                # if offer_details["has_action"]:
                #     discount += do_action(offer_details, saved_count, item, product_data)
    
        else:
            discount += items_removed*product_data[f"{item}"]["price"]

        return -1*discount

def action_offers(product_data, item):
    pass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    overall_total = 0

    count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0
    }

    for item in skus:
        if item not in list(product_data.keys()):
            return -1

        count[f"{item}"] += 1

    saved_count = count
    print(count)

    # for item in count:
    #     if product_data[f"{item}"]["has_offer"]:
    #         for offer_name, offer_details in product_data[f"{item}"]["offers"].items():
    #             if offer_details["has_action"]:
    #                 do_action(offer_details, count)

    for item in count:
        offer_count = 0
        print(item)
        if product_data[f"{item}"]["has_offer"]:
            for offer_name, offer_details in product_data[f"{item}"]["offers"].items():
                offer_count += 1
                print(f'count of {item} is', count[f"{item}"])
                print(offer_details)
                price = product_data[f"{item}"]["price"]
                quantity = offer_details["quantity"]
                value = offer_details["value"]

                item_total = value*(count[f"{item}"]//quantity)
                # print('item total:', item_total)

                overall_total += item_total #+ price*(count[f"{item}"]%quantity)

                if quantity != 1:
                    count[f"{item}"] -=  (count[f"{item}"]//quantity)*quantity
                print(f'count of {item} is', count[f"{item}"])

                if offer_count == (len(list(product_data[f"{item}"]["offers"].items()))):
                    overall_total += count[f"{item}"]*product_data[f"{item}"]["price"]
                    count[f"{item}"] = 0
                    print(f'count of {item} is', count[f"{item}"])

                if offer_details["has_action"]:
                    overall_total += do_action(offer_details, saved_count, item, product_data)
    
        else:
            overall_total += count[f"{item}"]*product_data[f"{item}"]["price"]

        #overall_total += item_total
        print(overall_total)

    return overall_total

#print(checkout("AAABBB"))


