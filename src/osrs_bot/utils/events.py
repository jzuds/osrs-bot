from http.server import BaseHTTPRequestHandler, HTTPServer
import simplejson
import logging

logger = logging.getLogger(__name__)
LOGFILE = "D:\Logs\osrs-bot-events.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOGFILE), logging.StreamHandler()],
)


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        print("in post method")
        self.data_string = self.rfile.read(int(self.headers["Content-Length"]))

        self.send_response(200)
        self.end_headers()

        data = simplejson.loads(self.data_string)
        logger.info(data)


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd...")
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
