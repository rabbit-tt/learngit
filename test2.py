#-*- coding: UTF-8 -*-
#函数

#abs()绝对值，hex()整数转十六进制，bool()转布尔值
print(abs(-11),hex(22),bool('1'))

#自定义函数
def my_abs(x):
    if x<=0:
	    return -x
    else:
        return x
print(my_abs(-13))

#导入函数
#将函数保存为hanshu.py后，可在当前目录下用from hanshu import my_abs
#空函数,无意义，占位方便以后添加函数
def ops():
    pass
    
#参数类型检查,isinstance()数据类型检查函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x<=0:
        return -x
    else:
        return x

print(my_abs(-1231))

#坐标位移函数
import math #导入math包
def move(x=0,y=0,step=0,angle=0):
    nx = x + step *math.cos(angle)
    ny = y + step *math.sin(angle)
    return nx,ny
print(move())

#解方程
def quadratic(a,b,c):
    d=b*b-4*a*c
    if d<0:
        return "无实数解"
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    if d==0:
        return x1
    else:
        return x1,x2

a=float(input("请输入参数a:"))
b=float(input("请输入参数b:"))
c=float(input("请输入参数c:"))
print(quadratic(a,b,c))

#位置参数
def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s
    
x=float(input("请输入x:"))
n=float(input("请输入n:"))
print(power(x,n))

#默认参数（不想继承上次结果的可设置=None)
def add_end(L=None):
    if L==None:
        L=[]
    L.append('end')
    return L
print(add_end([1,2,3]))

#可变参数(参数前加*，参数自动组装为list列表)
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + power(n)
    return sum
num=[1,2,3,4]
print(calc(*num),calc())

#关键字参数(参数前加**，参数自动组装为dict字典)
def person(name,age,**kw):
    print('name:',name,'age:',age,'others',kw)
person('Max',22,city='newyork',job='waitress')
extra={'city':'NewYork','job':'waitress'}
person('Max',22,**extra)

#命名关键字参数(参数前加含*参数，只接收指定关键字参数)
def person2(name,age,*,city,job):
    print('name:',name,'age:',age,'city:',city,'job:',job)
person2('Max',22,city='NewYork',job='waitress')

#函数参数必须遵循，必选参数，默认参数，可变参数，命名关键字参数，关键字参数的顺序
def f1(a,b,c=0,*args,d,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'d=',d,'kw=',kw)
f1(1,2,3,'a','b',d=4,name='Max',city='NewYork')

#递归函数汉诺塔
s=[]
def move(n,a='A',b='B',c='C'):
    if n==1:
        print(a,'-->',c)
        s.append(a+'-->'+c)
        return
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

n=int(input("请输入汉诺塔层数"))
move(n)
print("汉诺塔共",n,"层，",'共需移动',len(s),'次','操作过程为',s)




