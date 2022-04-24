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
                    "action_type": "add",   # one free B item won't change the value of the total
                    "sku_affected": "B",    # so this offer won't affect anything and is not needed in calculation
                    "number": 1
                }
            }
        }
    },    
}



#overall_total = 0

def do_action(offer, count_dict):
    if offer["action"]["action_type"] == "add":
        count_dict[f'{offer["action"]["sku_affected"]}'] += offer["action"]["number"]

def inspect_offer(offer, sku_quantity):
    if offer["quantity"] >= sku_quantity:
        return True
    else:
        return False

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

    print(count)

    # for item in count:
    #     if product_data[f"{item}"]["has_offer"]:
    #         for offer_name, offer_details in product_data[f"{item}"]["offers"].items():
    #             if offer_details["has_action"]:
    #                 do_action(offer_details, count)

    for item in count:
        item_total = 0
        print(item)
        if product_data[f"{item}"]["has_offer"]:
            #print(item)
            #for offer_name, offer_details in product_data[f"{item}"]["offers"].items():
                # #print(offer_name)
                # print(offer_details)
                # price = product_data[f"{item}"]["price"]
                # quantity = offer_details["quantity"]
                # value = offer_details["value"]

                # item_total = value*(count[f"{item}"]//quantity) + price*(count[f"{item}"]%quantity)
                # print(item_total)

            while count[f"{item}"] > 0:
                print('starting while loop')
                for offer_name, offer_details in product_data[f"{item}"]["offers"].items():
                    print(offer_details)
                    if offer_details["quantity"] > count[f"{item}"]:
                        print(count[f"{item}"])
                        floor_div = count[f"{item}"] // offer_details["quantity"]
                        item_total += offer_details["value"]*floor_div
                        count[f"{item}"] = count[f"{item}"] - offer_details["quantity"]*floor_div
                        print(count[f"{item}"])

                        print(item_total)
                    
                        break #breaking for loop, back to top of while loop
                    
                item_total += count[f"{item}"]*product_data[f"{item}"]["price"]
                print(item_total)
                item_total = 0
                
        
        # else:
        #     item_total = count[f"{item}"]*product_data[f"{item}"]["price"]

        overall_total += item_total
        #print(overall_total)

    return overall_total

#print(checkout("AAABBB"))
