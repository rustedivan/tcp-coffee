import BaseHTTPServer
import weboutput
import products

# This class handles incoming request from the web.
class CoffeeRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        route = self.path.split('/')[1:]
        functionality = route[0]    # First part of the URL is the functionality
        arguments = route[1:]       # The rest are passed to the functionality itself

        self.handle_functionality(arguments, functionality)

    # Handle different functionalities in different methods
    def handle_functionality(self, arguments, functionality):
        if functionality == 'list':
            self.write_products_list()
        elif functionality == 'coffee':
            self.handle_orders(arguments)
            self.send_to_list_page()
        else:
            weboutput.write_page_error("Unknown command.", self)

    # Perform HTTP redirect back to the first page
    def send_to_list_page(self):
        self.send_response(303) # HTTP 303 = "see other" = auto-redirects
        self.send_header("Location", "/list")   # auto-redirect to same server, '/list' URL
        self.end_headers()

    # Handles incoming orders (very important business logic!!)
    def handle_orders(self, arguments):
        if arguments[0] == 'order':
            if len(arguments) == 2: # /coffee/order/flat-black = "order one black coffee"
                # Order 1 of the product
                products.place_order(arguments[1], 1)

                if len(arguments) == 3: # /coffee/order/flat-black/5 = "order five black coffees"
                    order_count = int(arguments[2]) # Convert last argument to a count variable
                    order_name = arguments[2]
                    # Loop to order all the products
                    for i in range(0, order_count):
                        products.place_order(order_name, order_count)

    # Outputs list of all the products in the system
    def write_products_list(self):
        weboutput.write_page_start("Coffee Server Menu", self)
        weboutput.write_page_content("<h2>Coffee Menu</h2>", self)

        # Build a list of ids for all known "short names"
        list = products.id_to_shortname.values()
        weboutput.write_coffee_menu(list, self)
        weboutput.write_page_end(self)
