#-*- coding: UTF-8 -*-
#打印字符串与整数
print("100+10203+394829")
print(100+10203+394829)
#获取输入
print("please enter your name")
name=input()
print("hello,",name)
#print absolute value of an integer
print("Please enter your birth year")
a=int(input())
b=2017
print(name,"you are",b-a,"years old now!")
#绝对值计算
print("Please enter a namber")
a = int(input())
if a >=0:
    print(a)
else:
	print(-a)
#中文测试与三“表示无转译字符
print("""中文测试正常""")
#余数计算
get=1000%300
#%s字符/变量，%d整数，%f浮点数float
print('hello, %s, your %s is %d' % (name,'score',get))
s1=72
s2=85
r=(s2/s1-1)*100
print(r)
print('%.1f%%' % r)
#列表list[]与元组tuple(),长度函数len(),追加append(),插入insert(),删除pop()
friends=['Jack','Wendy','Alice']
print(friends)
c=len(friends)
print(friends[0],',',friends[2],',',friends[-2],',',c,'friends')
friends.append('Amy')
print(friends)
friends.insert(1,'MC')
friends.pop()
print(friends)
friends.pop(0)
print(friends)
roommates=('lin~',['shuang','shuang'],'qi~')
print(roommates,roommates[1],roommates[1][1])
#if判断
age=input("please enter your age:")
age=int(age)
if age>=60:
    print('老人')
elif age>=18:
    print('成年')
else:
	print('儿童')
#for循环，range()整数序列
sum=0
add=(range(101))
for x in add:
    sum=sum+x
print(sum)
#猜数字(缩进注意空格)
import random
d=random.randint(0,99)
yes=True
while yes:
    guess=int(input("猜数字\n(请输入一个整数)"))
    if guess == d:
        print('猜对啦')
        yes=False
    elif guess<d:
	    print('猜小啦')
    else:
        print('猜大啦')
else:
    print('游戏结束，答案是',d)
#字典dict {}与集合set(),in/get 判断存在,remove()删除key，extra
dict={'Bob':22,'Peter':44,'MC':77}
s1=set([3,4,1])
print(s1)
s1.remove(1)
print(s1)
print(dict.get('Thomas',-1))
print('Thomas' in dict)
print('Peter' in dict)
print(dict['MC'])
#修改列表或字典内容
dict[0]='hhhh'
print(dict)