import urllib2

def http_get():
    url='http://192.168.1.13:9999/test'
    #页面的地址
    #
    response = urllib2.urlopen(url)
    return response.read()
ret = http_get()
print("RET %r" % (ret))