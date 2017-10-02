from bottle import run, route

@route('/')
def index():
    return '<h1>hello, World</h1>'
@route('/bob')
def index():
    return '<h1>hello, bob</h1>'

if __name__ == '__main__':
    run()
