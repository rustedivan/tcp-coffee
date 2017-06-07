import os
import time
import products

# Save to tcp-coffee-orders.txt
def write_transaction_log(found_product_price, order_count, order_id):
    # Saves orders to the program's directory
    orderfilename = os.getcwd() + "/tcp-coffee-orders.txt"
    orderfile = open(orderfilename, 'a')  # 'a' opens in "append mode" so writes go to the end of file
    # Calculate full price and save order
    orderline = compose_order_line(found_product_price, order_count, order_id)
    orderfile.write(orderline)
    orderfile.close()

# Function contains the format of an order
def compose_order_line(found_product_price, order_count, order_id):
    orderline = str(order_count) + " \"" + products.shortname_to_fullname(order_id) + "\"" \
                + " (" + found_product_price * order_count + " kr)" \
                + " ordered at " + time.ctime() + "\n"
    return orderline