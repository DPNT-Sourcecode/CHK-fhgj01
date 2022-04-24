#from lib.solutions.CHK.data import product_data

# from fcntl import F_SEAL_SEAL
# from functools import total_ordering


from lib.solutions.CHK.data.product_data import product_data

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

        
        print('discount', discount)
        return -1*discount

def action_offers(product_data, item):
    pass

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