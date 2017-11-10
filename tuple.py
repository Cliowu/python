Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tuple1=('a','c','e')
>>> list(tuple1)
['a', 'c', 'e']
>>> 
>>> tuple2=(123,'a','b')
>>> list(tuple2)
[123, 'a', 'b']
>>> tuple3=(1,2,3,4)
>>> list(tuple3)
[1, 2, 3, 4]
>>> tuple1=(1,2,3,4)
>>> list(tuple1)
[1, 2, 3, 4]
>>> tup1 =('physics','chemistry',1997,2000)
>>> tup1[0]
'physics'
>>> list_test =['a','b','c']
>>> list_test.append('d')
>>> list_test
['a', 'b', 'c', 'd']
>>> tup1
('physics', 'chemistry', 1997, 2000)
>>> tup1.index
<built-in method index of tuple object at 0x01E29120>
>>> tup3 ="a","b","c","d"
>>> tup3
('a', 'b', 'c', 'd')
>>> tup1 =(12,34,56):
	
SyntaxError: invalid syntax
>>> tup1 =(12,34,56)
>>> tup2 =('abc','xyz')
>>> tup3 =tup1+tup2
>>> tup3
(12, 34, 56, 'abc', 'xyz')
>>> del tup3
>>> tup3

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tup3
NameError: name 'tup3' is not defined
>>> tup1 = ('physics', 'chemistry', 1997, 2000);
>>> tup2 = (1, 2, 3, 4, 5, 6, 7 );

>>> tup1[0]
'physics'
>>> tup2[1:5]
(2, 3, 4, 5)
>>> 
