from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 8080  # Debe coincidir con el puerto configurado en App Runner y expuesto en Docker

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en http://0.0.0.0:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
