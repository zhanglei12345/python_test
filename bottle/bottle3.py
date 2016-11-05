from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing
#route中的thing表示URL中/echo/之后的内容都会被赋值给字符串参数thing，然后被传入echo函数

run(host='localhost', port=9999, debug=True, reloader=True)
#debug=True,如果出现http错误，会创建一个调试页面
#reloader=True,如果你修改了任何python代码，浏览器中的页面会重新载入
