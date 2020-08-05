import os
import socketserver

from http.server import SimpleHTTPRequestHandler
PORT = int(os.getenv("PORT", 8000))

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.build_path()

        if path == "/":
            self.handle_root()
        elif path == "/hello/":
            self.handle_hello()
        else:
            self.handle_404()

    def handle_root(self):
        return super().do_GET()

    def handle_hello(self):
        content = f"""
        <html>
        <head><title>Hello Page</title></head>
        <body>
        <h1>Hello world!</h1>
        <p>path: {self.path}</p>
        </body>
        </html>
        """

        self.respond(content)

    def handle_404(self):
        msg = """NOT FOUND!!!!!!!!"""

        self.respond(msg, code=404, content_type="text/plain")

    def respond(self, message, code=200, content_type="text/html"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(message)))
        self.end_headers()
        self.wfile.write(message.encode())

    def build_path(self) -> str:
        result = self.path

        if result[-1] != "/":
            result = f"{result}/"

        return result

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("it" + " works")
        httpd.serve_forever(poll_interval=1)