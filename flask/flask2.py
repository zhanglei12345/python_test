from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)
#thing=thing这个参数的意识就是把名为thing的变量传入模板，它的值是变量thing中的字符串

app.run(port=9999, debug=True)
