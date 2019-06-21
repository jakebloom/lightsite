import socketserver
from gpiozero import LED

PORT = 8080

class RequestHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(b'Hello world')

  def do_POST(self):
    if led.is_lit:
      led.off()
    else:
      led.on()

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(b'ok')


led = LED(2)
led.off()

server = socketserver.TCPServer(('', PORT), RequestHandler)
print("Starting server on port", PORT)
server.serve_forever()
