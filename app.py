from bottle import route,run, template, static_file, request, get, post, error
import datetime
from beaker.middleware import SessionMiddleware
import sqlite3
import sys
from sys import argv

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/home')
def index():
    # CONNECT DATABASE
    con = sqlite3.connect('data\\todo.dat')
    cur = con.cursor()
    rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
    return template('index.tpl', rows=rows)

@route('/item<item:re:[0-9]+>')
def show_task(item):
    todoid = item
    # CONNECT DATABASE
    con = sqlite3.connect('data\\todo.dat')
    cur = con.cursor()
    cur.execute('SELECT * FROM todo WHERE id=?', (todoid,))
    rec = cur.fetchone()
    ttitle = rec[1]
    tdesc = rec[2]
    tdate = convDate = datetime.datetime.strptime(rec[3], '%Y-%m-%d %H:%M:%S.%f').strftime('%A %d %B %Y - %I:%M %p')
    if not rec:
        return 'this item number does not exist!'
        #CLOSE DATEBASE
        con.close()
    else:
        output = template('item.tpl', ttitle=ttitle, tdesc=tdesc, tdate=tdate, todoid=todoid)
        return output
        con.close()

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

@route('/edit<no:int>', method=['GET', 'POST'])
def edit_item(no):
    todoid = no
    if request.POST.get('save','').strip():
        todotitle = request.POST.get('task')
        tododesc = request.POST.get('desc')
        tododatetime = request.POST.get('tdate')

        # CONNECT DATABASE
        con = sqlite3.connect('data\\todo.dat')
        cur = con.cursor()
        cur.execute('UPDATE todo SET title=?,desc=?,datetime=? WHERE id=?',(todotitle, tododesc, tododatetime, todoid))
        con.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
        return template('index.tpl', rows=rows)
        # CLOSE DATEBASE
        con.close()

    else:
        # CONNECT DATABASE
        con = sqlite3.connect('data\\todo.dat')
        cur = con.cursor()
        cur.execute('SELECT * FROM todo WHERE id=?', (todoid,))
        rec = cur.fetchone()
        return template('edit_task.tpl', no=no, rec=rec)
        # CLOSE DATEBASE
        con.close()


@route('/About')
def index():
    return template('about.tpl')


@error(404)#error síða 17-19
def error404(error):
    return('<h1>Við fundum ekki þessa síðu(404)</h1>')

run(host='0.0.0.0', port=argv[1])
