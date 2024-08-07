from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en http://localhost:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
