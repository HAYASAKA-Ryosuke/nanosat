import asyncio
from router import Router
from request import Request
from response import Response
from view import View


class Application:

    def __init__(self):
        self.router = Router()

    async def __call__(self, scope, receive, send):

        view, action = self.router.search(scope['method'], scope['path'])
        if asyncio.iscoroutinefunction(view):
            response = await view(Request(scope, receive, action), Response())
        else:
            response = view(Request(scope, receive, action), Response())

        await send({
            'type': 'http.response.start',
            'status': response.status_code,
            'headers': response.headers
        })

        await send({
            'type': 'http.response.body',
            'body': response.body
        })
