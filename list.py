Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var = '1'
>>> print type(var)
<type 'str'>
>>> new_var = int(var) + 1
>>> print new_var
2
>>> page_num = 1
>>> print "第", page_num, "页"
第 1 页
>>> print type(page_num)
<type 'int'>
>>> print "第" + str(page_num) + "页"
第1页
>>> import random
>>> test_list = ['a', 'b', 'c']
>>> random.choice(test_list)
'a'
>>> random.choice(['a', 'b', 'c'])
'a'
>>> random.choice(['a', 'b', 'c'])
'a'
>>> random.choice(['a', 'b', 'c'])
'c'
>>> random.choice(['a', 'b', 'c'])
'c'
>>> random.choice(['a', 'b', 'c'])
'a'
>>> random.choice(['a', 'b', 'c'])
'a'
>>> random.choice(['a', 'b', 'c'])
'a'
>>> random.choice(['a', 'b', 'c'])
'c'
>>> list1 = ['physics', 'chemistry', 1997, 2000];
>>> list1[0]
'physics'
>>> list1[1]
'chemistry'
>>> list1[0:2]
['physics', 'chemistry']
>>> list1[1:3]
['chemistry', 1997]
>>> list2 = [1, 2, 3, 4, 5 ];
>>> list1 + list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
>>> list1 =[1,2,3]
>>> list1 * 2
[1, 2, 3, 1, 2, 3]
>>> 3 in [1,2,3]:
	
SyntaxError: invalid syntax
>>> 3 in [1,2,3]
True
>>> if 3 in [1,2,3]:
	print "OK"

	
OK
>>> list = []
>>> list.append("a")
>>> list
['a']
>>> 
