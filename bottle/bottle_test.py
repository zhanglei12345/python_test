import requests

resp = requests.get('http://localhost:9999/echo/zhang')
if resp.status_code == 200 and \
  resp.text == 'Say hello to my little friend: zhang!':
    print('It worked! That almost never happens!')
else:
    print('Argh, got this:', resp.text)

#客户端测试代码
#保持bottle3.py处于运行状态
