from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello World!']

if __name__ == '__main__':
    srv = make_server('localhost', 5005, application)
    srv.serve_forever()
