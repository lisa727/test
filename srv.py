
import settings

from http.server import SimpleHTTPRequestHandler

from utils import normalize_path, to_bytes


class MyHttp(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = normalize_path(self.path)

        if path == "/":
            self.handle_root()
        elif path == "/hello/":
            self.handle_hello()
        elif path == "/style/":
            self.handle_style()
        elif path == "/image/":
            self.handle_image()
        else:
            self.handle_404()

    def handle_root(self):
        return super().do_GET()

    def handle_style(self):
        css_file = settings.PROJECT_DIR / "style.css"
        if not css_file.exists():
            return self.handle_404()

        with css_file.open("r") as fp:
            css = fp.read()

        self.respond(css, content_type="text/css")

    def handle_image(self):
        image_file = settings.PROJECT_DIR / "pictures" / "kit.jpg"
        if not image_file.exists():
            return self.handle_404()
        with image_file.open("rb") as fp:
            img = fp.read()

        self.respond(img, content_type="image/jpg")

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

        payload = to_bytes(message)

        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(payload)))
        self.end_headers()

        self.wfile.write(payload)
