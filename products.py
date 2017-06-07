import time
import os
import transactionlog

# These are the products we sell

# Converting between "product id" and "product shortname"
id_to_shortname = {
    1827: 'flat-black',
    1248: 'latte',
    9019: 'shock',
    5545: 'caramel',
    9989: 'crazy',
    6737: 'espresso',
    6738: 'espresso',
    3333: 'palazzo',
    4142: 'mazagran',
    2131: "ccb"
}

# Converting between product id and full, human-readable name
id_to_fullname = {
    1248: 'Caffe Latte',
    1827: 'Regular black coffee',
    9019: 'Caffeine System Shock',
    5545: 'Caramelatte',
    2131: 'Cold Cream Brew',
    9989: 'Craziest Cappu',
    6737: 'Espresso',
    6738: '2-Shot Espresso',
    4142: 'Summer Mazagran',
    3333: 'Palazzo'
}

# Converting between product id and price (stored as string for convenience)
id_to_price = {
    9019: '78',
    1827: '28',
    1248: '48',
    5545: '49',
    2131: '47',
    4241: '75',
    6737: '36',
    6738: '45',
    9989: '99',
    3333: '66'
}

# Get all product ids in database as an array
def get_all_products():
    return id_to_fullname.keys()

# Reverse lookup (have shortname, get id)
found_product_id = 0
def shortname_to_id(shortname):
    global found_product_id
    # Look up
    for (id, found_name) in id_to_shortname.iteritems():
        if found_name == shortname:
            found_product_id = id
    return found_product_id

# Reverse lookup (have shortname, get price)
found_product_price = 0
def shortname_to_price(shortname):
    global found_product_price
    id = shortname_to_id(shortname)
    if id_to_price.has_key(id):
        found_product_price = id_to_price[id]
    return found_product_price

# Reverse lookup (have shortname, get full name)
def shortname_to_fullname(shortname):
    id = shortname_to_id(shortname)
    return id_to_fullname[id]

# Places order into transaction file
def place_order(shortname, order_count):
    global found_product_price

    order_id = shortname_to_id(shortname)
    price = shortname_to_price(shortname)
    # Save the order so baristas can work
    transactionlog.write_transaction_log(found_product_price, order_count, order_id)