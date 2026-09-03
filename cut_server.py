#!/usr/bin/env python3
# Serves the cut app and relays /wos requests to the Clarivate WoS Starter API
# (browsers can't call it directly - no CORS). The key never leaves this machine.
import functools
import http.server
import json
import os
import urllib.error
import urllib.parse
import urllib.request

WOS_BASE = "https://api.clarivate.com/apis/wos-starter/v1/documents"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/wos"):
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            key = params.pop("key", [""])[0]
            target = WOS_BASE + "?" + urllib.parse.urlencode({k: v[0] for k, v in params.items()})
            req = urllib.request.Request(target, headers={"X-ApiKey": key})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    body, code = r.read(), r.status
            except urllib.error.HTTPError as e:
                body, code = e.read(), e.code
            except Exception as e:
                body, code = json.dumps({"error": str(e)}).encode(), 502
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    http.server.ThreadingHTTPServer(
        ("127.0.0.1", 8734), functools.partial(Handler, directory=here)
    ).serve_forever()
