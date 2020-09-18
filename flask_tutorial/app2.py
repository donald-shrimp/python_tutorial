from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer


# load html file.
with open('index.html', mode='r') as f:
    index = f.read()
with open('next.html', mode='r') as f:
    next = f.read()


class HelloServerHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        _url = urlparse(self.path)
        if (_url.path == '/'):
            self.index()
        elif (_url.path == '/next'):
            self.next()
        else:
            self.error()
    
    # index action.
    def index(self):
        self.send_response(200)
        self.end_headers()
        html = index.format(
            title='Hello', 
            message='ようこそ、HTTPServerの世界へ！'
        )
        self.wfile.write(html.encode('utf-8'))
        return


    # next action.
    def next(self):
        self.send_response(200)
        self.end_headers()
        html = next.format(
            data='{\n  data:"this is data."\n}'
        )
        self.wfile.write(html.encode('utf-8'))
        return


    # error action.
    def error(self):
        self.send_error(404, "CANNOT ACCESS!!")
        return


HTTPServer(('',8000), HelloServerHandler).serve_forever()