from Service import Service
from tornado.web import RequestHandler


class HandledTextRequestHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = Service()

    async def get(self):
        try:
            text = self.get_argument('text', None)
            print(text)
            result = await self.service.get_text(text)
            if result:
                self.set_status(200)
            else:
                self.set_status(204)
            # self.write({'message': 'hello world'})
            self.finish(result)
        except KeyError as e:
            raise tornado.web.HTTPError(404, reason=str(e))
