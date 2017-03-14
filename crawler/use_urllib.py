#import urllib.request as ur
from urllib import request

#req = request.Request('http://www.douban.com/')
#req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
#模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()    #获取网页的数据
    print('Status:', f.status, f.reason)    #响应码，说明
    for k, v in f.getheaders():     #http头信息
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))    # 将字节解码为字符串

#urllib是基于http的高层库
#request处理客户端请求，response处理服务器的响应，parse会解析url
#urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。
