from bottle import route,run, template, static_file

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def index():
    return template('index.tpl')

@route('/test')
def index():
    output ='<b>It works</b>!'
    return output

'''
@error(404)#error síða 17-19
def error404(error):
    return('<h1>Við fundum ekki þessa síðu(404)</h1>')
'''

run(host='localhost',port=8080, debug='True', reloader='True')