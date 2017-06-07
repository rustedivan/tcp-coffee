# This file does output to the Coffee Server web interface
import products

# Writes success code (200) and starts a bit of HTML
def write_page_start(page_title, output):
    output.send_response(200)
    output.send_header("Content-type", "text/html")
    output.end_headers()
    output.wfile.write("<html><head><title>" + page_title + "</title></head>")

# Simply writes HTML content to the page
def write_page_content(html_content, output):
    output.wfile.write(html_content)

# Writes the end of the HTML page
def write_page_end(output):
    output.wfile.write("</body></html>")

# Writes error code (404) and writes an error message
def write_page_error(error_text, output):
    output.send_response(404)
    output.send_header("Content-type", "text/html")
    output.end_headers()
    output.wfile.write("<html><head><title>ERROR</title></head><h1>" + error_text + "</h1></body></html>")

# Writes a HTML link
def make_link(url, text):
    # Outputs <a href="url">text</a>
    return "<a href=\"" + url + "\">" + text + "</a>"

# Writes the order menu
def write_coffee_menu(menu_table, output):
    output.wfile.write("<ul>")
    for id in products.get_all_products():
        shortname = products.id_to_shortname[id]
        price = products.shortname_to_price(shortname)
        name = products.id_to_fullname[id]

        text = name + ' (' + str(price) + 'kr)'
        output.wfile.write("<li>" + text + ' ' \
                           + make_link('coffee/order/' + shortname, '[Order]') \
                           + make_link('coffee/order/' + shortname + '/2', '[Double]') \
                           + "</li>")
    output.wfile.write("</ul>")

    products.place_order(products.id_to_shortname[5545], 1)  # TODO: only for testing, remove before checking in
