import json

class Response:
    status_code = 200
    headers = []
    body = b''

    def json(self, text, status_code=200, headers=[[b'content-type', b'application/json']]):
        self.headers = headers
        self.body = json.dumps(text).encode()
        self.status_code = status_code
        return self
