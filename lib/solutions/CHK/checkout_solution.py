from data import product_data

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for item in skus:
        if item not in product_data.keys():
            return -1
