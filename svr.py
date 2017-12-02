from bottle import route,run, template, static_file, request, get, post
import datetime
import sqlite3
import sys

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def index():
    # CONNECT DATABASE
    con = sqlite3.connect('data\\todo.dat')
    cur = con.cursor()
    rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
    return template('index.tpl', rows=rows)


@route('/new', method=['GET', 'POST'])
def new_task():
    if request.POST.get('save', '').strip():
        todotitle = request.POST.get('task')
        tododesc = request.POST.get('desc')
        tododatetime = datetime.datetime.now()

        #CONNECT DATABASE
        con = sqlite3.connect('data\\todo.dat')
        cur = con.cursor()                        #(null,?,?,?)(id,name,desc,datetime)
        rec = cur.execute('INSERT INTO todo VALUES (null,?,?,?)', (todotitle,tododesc,tododatetime))
        con.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')

        return template('index.tpl', rows=rows)

    else:
        return template('newtask.tpl')


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
