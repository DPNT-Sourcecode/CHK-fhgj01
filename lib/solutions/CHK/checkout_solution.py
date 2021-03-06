import operator

#from lib.solutions.CHK.data import product_data

#The import below worked in personal testing, but lib wasn't recognised by the send_command_to_server.py file.
#from lib.solutions.CHK.data.product_data import product_data



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
    "F": {
        "price": 10,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 3,
                    "action_type": "free_item",     
                    "sku_affected": "F",            
                    "number": 1                     
                }
            }
        }
    },
    "G": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "H": {
        "price": 10,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 10,
                "value": 80,
                "has_action": False
            },
            "offer_2": {
                "quantity": 5,
                "value": 45,
                "has_action": False
            }    
        }
    },
    "I": {
        "price": 35,
        "has_offer": False,
        "offers":{}
    },
    "J": {
        "price": 60,
        "has_offer": False,
        "offers":{}
    }, 
    "K": {
        "price": 70,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 2,
                "value": 120,
                "has_action": False
            }    
        }
    },
    "L": {
        "price": 90,
        "has_offer": False,
        "offers":{}
    },
    "M": {
        "price": 15,
        "has_offer": False,
        "offers":{}
    },
    "N": {
        "price": 40,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 3,
                    "action_type": "free_item",     
                    "sku_affected": "M",            
                    "number": 1                     
                }
            }
        }
    },
    "O": {
        "price": 10,
        "has_offer": False,
        "offers":{}
    },
    "P": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 5,
                "value": 200,
                "has_action": False
            }    
        }
    },
    "Q": {
        "price": 30,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 3,
                "value": 80,
                "has_action": False
            }    
        }
    },
    "R": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 3,
                    "action_type": "free_item",     
                    "sku_affected": "Q",            
                    "number": 1                     
                }
            }
        }
    },
    "S": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "T": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "U": {
        "price": 40,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 4,
                    "action_type": "free_item",     
                    "sku_affected": "U",            
                    "number": 1                     
                }
            }
        }
    },
    "V": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 3,
                "value": 130,
                "has_action": False
            },
            "offer_2": {
                "quantity": 2,
                "value": 90,
                "has_action": False
            }    
        }
    },
    "W": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "X": {
        "price": 17,
        "has_offer": False,
        "offers":{}
    },
    "Y": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "Z": {
        "price": 21,
        "has_offer": False,
        "offers":{}
    },
}

special_offers = {
    "stxyz_group": {
        "sku_included": ["Z","S","T","Y","X"],    #ordered bprice value from product_data
        "quantity": 3,
        "value": 45
    }
}

#overall_total = 0

def do_action(offer, count_dict, item, product_data):
    print('entering do action')
    print(offer, count_dict, item)
    if offer["action"]["action_type"] == "free_item":
        eligable_items_number = count_dict[f'{item}'] // offer["action"]["quantity"]
        print('eligable_items_number', eligable_items_number)
        if eligable_items_number < count_dict[f'{offer["action"]["sku_affected"]}']:
            items_removed = eligable_items_number
        else:
            items_removed = count_dict[f'{offer["action"]["sku_affected"]}']
        
        print('items removed', items_removed)

        offer_count = 0
        discount = 0

        if items_removed%2 !=0 and count_dict[f'{offer["action"]["sku_affected"]}']%2 == 0 and offer["action"]["sku_affected"] == "B":
            discount -= 15

        if offer["action"]["sku_affected"] == "Q" and items_removed%2 !=0 and count_dict[f'{offer["action"]["sku_affected"]}']%3 == 0:
            discount -= 10

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
                    discount += items_removed*price
                    items_removed = 0
                    print(f"count of {offer['action']['sku_affected']} is", items_removed)

                # if offer_details["has_action"]:
                #     discount += do_action(offer_details, saved_count, item, product_data)
    
        else:
            discount += items_removed*product_data[f"{offer['action']['sku_affected']}"]["price"]
        
        print('discount', discount)
        return -1*discount

def check_special_offers(count, special_offers, overall_total):
    group_count = {}
    #ordered_by_value = sorted(list(count), key=operator.itemgetter('price')) 

    for sku in special_offers["stxyz_group"]["sku_included"]:
        group_count[f'{sku}'] = count[f'{sku}']
    print(group_count)
    total = 0
    
    for item in group_count:
        total += group_count[f'{item}']
    
    print('total', total)
    print('value from offer', special_offers["stxyz_group"]["value"])

    value = (special_offers["stxyz_group"]["value"])
    quantity = (special_offers["stxyz_group"]["quantity"])

    print('value', value, 'quantity', quantity)
    
    overall_total = (total//quantity) * value
    removal_number = (total//quantity) * quantity

    print('overall total', overall_total, 'removal number', removal_number)


    for item in group_count:
        print('removal loop', item, group_count[f'{item}'], removal_number)
        group_count_intermediary = group_count[f'{item}']
        group_count[f'{item}'] -= removal_number 
        if group_count[f'{item}'] < 0:
            group_count[f'{item}'] = 0
            removal_number -= group_count_intermediary
        else:
            removal_number = 0

        print('end of removal loop', item, group_count[f'{item}'], removal_number)

        
            # else:
            #     group_count[f'{item}'] -= removal_number
            #     removal_number = 0

    for sku in group_count:
        count[f'{sku}'] = group_count[f'{sku}']

    print('overall_total', overall_total, 'group_count' , group_count)

    return overall_total, count

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    overall_total = 0

    count = {}
    saved_count = {}

    for item in product_data:
        count[f"{item}"] = 0
        saved_count[f"{item}"] = 0

    for item in skus:
        if item not in list(product_data.keys()):
            return -1

        count[f"{item}"] += 1
        saved_count[f"{item}"] += 1

    print('pre group discount ',count, ' ',overall_total)
    overall_total, count = check_special_offers(count, special_offers, overall_total)
    print('post group discount ',count, ' ',overall_total)

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