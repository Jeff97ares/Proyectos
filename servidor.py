import http.server
import socketserver

# Define el puerto en el que se ejecutará el servidor
PORT = 8000

# Define el manejador del servidor
Handler = http.server.SimpleHTTPRequestHandler

# Inicia el servidor en el puerto definido
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor corriendo en el puerto {PORT}")
    httpd.serve_forever()
