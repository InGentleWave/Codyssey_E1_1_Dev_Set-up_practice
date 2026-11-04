import sys
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Codyssey: Hello, World!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    # 0.0.0.0 으로 바인딩해야 Docker 포트 매핑(-p)을 통해 외부에서 접근할 수 있습니다.
    server = HTTPServer(("0.0.0.0", 80), HelloHandler)
    print("Server listening on port 80", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        # 터미널에서 직접 실행한 경우에만 Enter 입력을 기다립니다.
        if sys.stdin.isatty():
            input("에러가 발생했습니다. Enter를 누르면 종료합니다...")
        sys.exit(1)