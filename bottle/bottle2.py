from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='.')    #指定的是root目录(.表示当前目录)

run(host='localhost', port=9999)
