import http.server
import socketserver
import socket
import webbrowser
import os
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent caching for live development/testing
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    local_ip = get_local_ip()
    
    print("=" * 60)
    print("SERVIDOR LOCAL SIGA - UPE INICIADO!")
    print("=" * 60)
    print(f"Computador (Desktop):")
    print(f"   http://localhost:{PORT}")
    print()
    print(f"iPhone (no mesmo Wi-Fi):")
    print(f"   http://{local_ip}:{PORT}")
    print("=" * 60)
    print("Pressione Ctrl + C para encerrar o servidor a qualquer momento.")
    print("=" * 60)
    
    # Auto-open on desktop browser
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado com sucesso.")
