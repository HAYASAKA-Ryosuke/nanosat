class View:
    def __init__(self, view, request, response):
        self._view = view
        self._request = request
        self._response = response

    @property
    async def response(self):
        return self._view(self._request, self._response)
