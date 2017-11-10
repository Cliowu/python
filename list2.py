Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list = ['physics', 'chemistry', 1997, 2000];
>>> list[2]
1997
>>> list[2] = 2001
>>> list
['physics', 'chemistry', 2001, 2000]
>>> del list[2]
>>> list
['physics', 'chemistry', 2000]
>>> list1 =[2,3]
>>> list2 =[1,2,3,4,5]
>>> cmp(list1,list2)
1
>>> list1 =[0,1]
>>> cmp(list1,list2)
-1
>>> list1 =[1,2,3,4,5]
>>> cmp(list1,list2)
0
>>> list1=[789,'zzz']
>>> list2=[456,'abc']
>>> cmp(list1,list2)
1
>>> list1=[456,'zzz']
>>> cmp(list1,list2)
1
>>> list2=[789,'abc']
>>> cmp(list1,list2)
-1
>>> len(list1)
2
>>> list2=[1,2,3,4,5]
>>> max(list2)
5
>>> list2
[1, 2, 3, 4, 5]
>>> list2.reverse()
>>> list2
[5, 4, 3, 2, 1]
>>> 
