def startServer(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    print("Start server")
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class datum:


        def addInput(datum):


