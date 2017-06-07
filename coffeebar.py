import BaseHTTPServer
import webbrowser
import products
from requesthandling import CoffeeRequestHandler

if __name__ == '__main__':
    # Start a server at localhost:9090
    # Requests are handled in requesthandling.py
    port_number = 9090
    httpd = BaseHTTPServer.HTTPServer(("localhost", port_number), CoffeeRequestHandler)

    print "Coffee Server running. Open \"localhost:" + str(port_number) + "/list\" in your browser."

    try:
        webbrowser.open_new("localhost:" + str(port_number) + "/list")
        httpd.serve_forever()   # Program will stay here until exited
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "Coffee Server stopped. Reload your browser to verify."