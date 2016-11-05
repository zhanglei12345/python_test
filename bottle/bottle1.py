from bottle import route, run

#bottle 使用route装饰器来关联URL和函数
@route('/')
def home():
    return "It isn't fancy, but it's my home page"

run(host='localhost', port=9999)
#run()函数会执行bottle内置的python测试用web服务器
