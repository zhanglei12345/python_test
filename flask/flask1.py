from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')
#flask默认的静态文件目录是static，默认的静态文件url由/static开始。
#把文件夹改成'.'(当前目录),把url前缀改成''(空),这样url就被映射到当前目录的文件index.html

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my friend: %s" % thing

app.run(port=9999, debug=True)
#flask中的dubug=True相当于bottle中的debug和reloader
#生产环境不要把debug设置为True
