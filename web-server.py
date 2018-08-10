from http.server import HTTPServer, BaseHTTPRequestHandler

class WebServ(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            open_file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            open_file = "File not found ------ Server Running"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(open_file, 'utf-8'))

httpd = HTTPServer(('localhost', 8000), WebServ)
httpd.serve_forever()
