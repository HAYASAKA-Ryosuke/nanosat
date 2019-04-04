from application import Application


def ham_view(request, response):
    print(request.query_params)
    return response.json('ham')


async def helloworld_view(request, response):
    return response.json('helloworld')

app = Application()
app.router.register('GET', '/ham', ham_view)
app.router.register('GET', '/', helloworld_view)
