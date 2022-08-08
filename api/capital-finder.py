from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    country = query_dict["country"]
    capital = query_dict["capital"]

    message = f"The capital of {country} is {capital}"
    self.wfile.write(message.encode())
    return