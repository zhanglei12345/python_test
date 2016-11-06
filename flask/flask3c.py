from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing']= request.args.get('thing')
    kwargs['place']= request.args.get('place')
    return render_template('flask3.html', **kwargs)
#传入模板的参数较多时，可以使用字典的**操作符
app.run(port=9999, debug=True)
