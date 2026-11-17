from wsgiref.simple_server import make_server
def app(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain;charset=utf-8')
		]
	start_response(status, headers)
	return  ['hello, world']
with make_server('', 8000, app) as httpd: 
	print('Сервер запущен на http://localhost:8000')
	httpd.serve_forever()

