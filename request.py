import urllib


class Request:

    def __init__(self, scope, receive, action):
        self.META = scope
        self.receive = receive
        self.action = action

    @property
    def query_params(self):
        if self.META.get('method') == 'GET':
            if isinstance(self.META['query_string'], str):
                return urllib.parse.parse_qs(self.META['query_string'])
            elif isinstance(self.META['query_string'], bytes):
                return urllib.parse.parse_qs(self.META['query_string'].decode('latin-1'))
            else:
                return dict()

    @property
    async def data(self):
        body = b''
        if self.META.get('method') in ['POST', 'PUT', 'DELETE', 'PATCH']:
            content_length = int(self.META.get('CONTENT_LENGTH'))
            while True:
                message = await self.receive()
                if message['type'] == 'http.request':
                    body += message.get('body', b'')
                    if not message.get('more_body', False):
                        break
        return body
