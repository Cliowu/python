Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values={}
>>> values['username'] ="2872730389@qq.com"
>>> values['password']="lhynhdgrx0619."
>>> data = urllib.urlencode(values)
>>> url = "http://passport.csdn.net/account/login"
>>> geturl = url +"?"+data
>>> request = urllib2.Re

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    request = urllib2.Re
AttributeError: 'module' object has no attribute 'Re'
>>> request = urllib2.Request(geturl)
>>> response = urllib2.urlopen(request)
>>> print response.geturl()
http://passport.csdn.net/account/login?username=2872730389%40qq.com&password=lhynhdgrx0619.
>>> 
