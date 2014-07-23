#!/usr/bin/python
import Settings
import tornado.web
import tornado.httpserver
import tornado.ioloop
import json
import decimal



class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)
        
class jsonHandler(tornado.web.RequestHandler):
    def get(self):
        
        import db
        c=db.mydb()
        self.write(json.dumps(c.get_list(),cls=DecimalEncoder))
       

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
	        (r"/()$", tornado.web.StaticFileHandler, {'path':'statik/index.html'}),
            (r"/json", jsonHandler),
	        (r"/statik/(.*)", tornado.web.StaticFileHandler, {"path": Settings.STATIC_PATH}),

        ]
        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
        main() 
