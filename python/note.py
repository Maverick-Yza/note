# 一、 python是什么
#    python是面向对象的高级解释型编程语言
#    python是强类型的动态脚本语言


# 二、 编写第一个程序
print("Hello SixStar")    # 注意：print要顶格写，否则就会报错
# 运行py文件的推荐方式：右键点击文件空白处，选择Run"文件名"


# 三、 常见的bug
# 1. 输入错误
# 2. 缩进错误
# 3. 语法错误
# 4. 命名错误


# 四、 Debug
# 1.设置断点
print(123)
print(123)
print(123)
print(123)
print(123)
print(123)
print(123)
# 总结：可以通过debug调试看到程序执行的顺序


# 五、注释
# 1.单行注释
# 用 井号   加在要注释内容的前面
# 2.多行注释
# 用 三引号 来将要注释的内容扩住 （注意：可以是三对单引号也可以是三对双引号）
# Ctrl + /    添加或注销单行注释
# Ctrl + z    撤销
# Ctrl + c    复制
# Ctrl + v    粘贴
# Ctrl + f    查找
# Ctrl + d    复制到下一行

# 六、 输出函数（print）
#    *values值，表示可以一次输出多个对象。输出多个对象时要用 ， 将其隔开
# sep    用来间隔多个对象，默认值是一个空格
print("哈哈哈", "笑嘻嘻", "乐呵呵")            # 若不加 ， 则会将三个词当作一个整体来打印
print("哈哈哈", "笑嘻嘻", "乐呵呵", sep='*')    # 次行代码打出来的三个词中间会用 * 来隔开
# end    用来设定以什么来结尾，默认值是换行符 \n ，我们可以换成其他的字符串
print("Hello",end="!")
print("World")             # 上面两行代码打出来的是：Hello!World
#    *注意：print(字符串,end="后面拼接的值") 最后输出的值为：第一个print中的字符串 + 后面拼接的值 + 第二个print中的字符串

# 七、变量
# 1.变量的作用
# 是计算机中的储存空间，用来保存数据
# 2.定义变量的格式
num1 = 10
print(num1)    # print后面的括号里没有引号就会被识别成变量名，打印的是变量的值，如果变量没有被赋值，则会报错
# 注意：变量只有在被赋值后才会被创建，所以使用变量前必须赋值
# 注意：首次使用变量会在内存中划分空间，并初始化。再次使用变量不会再划分空间，只会修改原空间的值
a = 6
# 解释器做了两件事
# 1.在内存中创建了一个6的数据
# 2.创建了一个变量a，把6这个数据保存到a变量中
a = 6.6
print(a)
a = "黄昏"
print (a)
#    *注意：同一个变量可以被多次赋值，并且可以是不同的数据类型

# 八、标识符
# 1.含义：程序员定义的变量名和函数名
# 2.标识符规定
#   只能由数字，字母，_(下划线)组成     // *注意：Python3可以用中文命名，但是不推荐，因为不符合代码的规范性
#   不能以数字开头
#   不能是关键字(python中已经使用了的标识符，具有特殊的功能和含义)
#   严格区分大小写
(num1) = 1
print((num1))
print(num1)
# *注意：上面两种打印方式的结果都一样
# 3.命名规范
#   见名知意
#   下划线分割法 —— 多个单词组成的名称，单词和单词之间用下划线分开
#   大驼峰命名法 —— 多个单词组成的名称，每个单词的首字母大写
#   小驼峰命名法 —— 第一个单词首字母小写，后面单词首字母大写


# 九、数值类型
#  整型   —— int
#  浮点型 —— float
#  布尔型 —— bool    (True / False) *首字母必须大写
#  复数   —— complex    固定写法：z = a + bj, j为虚数单位(不能写成i)
print(1 + 2j)

# 布尔值可以当作整型来对待，True为1，False为0

#    *检测数据类型的方法：type()
num = 1
print(type(num))


# 十、字符串
# 符号：str
# 特点：需要加上引号，单双引号都可以，包含了多行内容时也可以使用三引号
name1 = """hello world"""
name2 = """sixstar
哈哈哈
"""
print(name2)     # 此时打出的 sixstar 和 哈哈哈 之间会换行


# 十一、格式化输出
# 占位符
# 作用：生成一定格式的字符串
# 占位符的三种方式：

# A. %(后面可加c/s/d/u/o/x/X/f/e/E/g/G/p/%)
# %s —— 字符串
# %d —— 整型
name = 'bingbing'
age = 18
print("My Name: %s, My Age: %d" % (name,age))
# %4d —— 数字设置位数，不足前面补空白 (4可以替换成任何数字)
a = 123
print("%6d" % a)    # 打出:   123(前面有三个空格)
print("%06d" % a)   # 打出:000123(即会用0来补齐前面的空格)  只有前面加0才是用0来补空，只有0管用其它的数字都会与后面的数字看作一个整体
b = 123456
print("%3d" % b)    # 打出:123456
c = 3
print("%001d" % c)  # 打出:3
# %f —— 浮点型(默认打印小数点后六位，不足则补0，遵循四舍五入原则)
d = 3.1415926
print("%.4f" % d)    # 打出:3.1416(数字设置小数位数，遵循四舍五入原则)
#    **注意：% 与 4f 之间要加 " . "
# %%
print("我是%%的1%%" % ())    # 打出:我是%的1%

# B. format()
#   1.用{}当占位符，按顺序输入值
test = "my name is {}，my age is {}".format("小明",18)
print(test)
test = "my name is {1}，my age is {0}".format(18," 小明")    # 与上面的代码打印内容相同，括号里的数字代表后面括号里元素的下标
test = "my name is {name}，my age is {age}".format(name = "小明",age = 18 )    # 通过 {key} 指定名称，参数用键值对传入
#   2.格式化数字（指定数字的显示格式）
rate = 75
print("{:.0%}".format(rate))    # 括号里是打印的格式，注意要加 “:”

# *C. 格式化 f
# 格式：f"{表达式}"
name = "bingbing"
age = 18
print(f"Name:{name},Age:{age}")    # 打出:Name:bingbing,Age:18


# 十二、运算符
# 1.算数运算符
#    *注意：使用算数运算符时若存在浮点数，则结果也会用浮点数表示
#    *注意：使用运算符 " / "，商一定是浮点数
# // —— 取整除(舍弃小数部分，不用进行四舍五入)
# %  —— 取余数
# ** —— 幂
#  优先级排序：幂 > 乘、除、取余、取整 > 加减

# 2.赋值运算符
n = 10
n += 5    # 等同于：n = n + 5(加号可以换成其他的算数运算符)    **注意：必须提前定义n
print(10 += 2)    # 会报错，因为赋值运算符是针对变量存在的

# 3.比较运算符（==/!=/>/</>=/<=）   （*注意：会返回布尔值）

# 4.逻辑运算符
#   and(与) —— 两边都为真则为真
#   or(或)  —— 一边为真则为真
#** not(非) —— 表示相反的结果
print(not 3>9)    # 打出：True

# 5.三目运算符（三元表达式）
# 格式：为真输出的内容 if 条件 else 为假输出的内容
x = 7
result = "Even" if x % 2 == 0 else "Odd"    # 功能：判断x是否为偶数


# 十三、输入函数（ input ）
name = input("请输入名字：")
pwd = input("请输入密码：")
print(name,pwd)
#    **注意python不需要规定输入的类型，默认输入的是字符串类型


# 十四、转义字符（ \ ）
# \t —— 制表符（通常表示空四个字符，也称为缩进）
print("hello\tworld")    # 打出：hello    world（中间空四格）
# \n —— 换行符
# \r —— 回车（表示将当前位置移到本行开头）
print("hello\rworld")    # 打出：world
# \\ —— 反斜杠符号
print("sixs\\tar")       # 打出：sixs\tar
print(r"s\i\x\s\t\a\r")  # 打出：s\i\x\s\t\a\r    （**注意：r原生字符串，默认取消转义）


# 十五、if判断语句
# 1.if判断（满足条件则执行下面的内容）
age = 20
if age < 18:
    print("未满十八岁")

# 2.if-else
# if 条件:
#     满足条件执行的内容
# else:
#     不满足条件执行的内容

# 3.if-elif-else
# if 条件:
#     内容1
# elif:
#      内容2
# else:
#     不满足条件执行的内容

# 4.if-elif
# if 条件:
#      内容1
# elif:
#      内容2
# elif:
#     内容3

# 5.if嵌套（*注意要缩进）
# if 条件1:
#     内容1
#     if 条件2:
#         内容2
#     else:
#         内容3
# else:
#     内容4


# 十六、循环语句

# 1.while循环
# while条件:
#     循环体（条件满足时做的事）
#     改变变量

# **2.for循环（迭代循环）
# for 临时变量 in 可迭代对象：
#     条件满足时执行的代码
# *注意：可迭代对象就是要去遍历取值的整体（如字符串）
s1 = "HelloWorld"
for i in s1:
    print(i)    # 会将 s1 中的每个字母每行依次打出一个

# **3.range()
# 用来记录循环的次数，相当于一个计数器
for i in range(1,6):
    print("hh")    # 会打出五行 hh
# 当range()的括号里有两个数时，第一个代表开始位置，第二个代表结束位置（不包含在内，即只会循环到结束位置的前一个数）
# *注意：若range()的括号里只有一个数时，则代表循环的次数

# 4.break 和 continue （注意：都是专门在循环中使用的关键字）
# break —— 结束循环
# continue —— 结束当前循环进入下一循环（即跳过循环中的某一次）
# ** 注意：在continue之前一定要修改计数器，否则会陷入死循环
i = 1
while i <= 5:
    print(f"小明在吃第{i}个苹果")
    if i == 3:
        print(f"吃到了一条虫子，第{i}个苹果不吃了")
        i += 1
        continue
    i += 1


# 十七、字符串&列表

# 1.字符串编码
#     其本质是二进制数据与语言文字的一一对应关系
#   常用编码
#   A. ASCLL      所占空间为 8bit / 1bytes
#   B. Unicode    所有字符都是2个字节
#       优点：字符与数字的转换速度更快一点
#       缺点：占用空间大
#   C. UFT-8      （精准，对不同的字符用不同的长度表示）
#       优点：节省空间
#       缺点：字符与数字的转换速度较慢，每次都要计算字符要用多少个字节来表示
#   字符串编码转换
a = "hello"
print(a,type(a))                # str，字符串是以字符为单位进行处理的
a1 = a.encode()     # 编码
print("编码后：",a1,type(a1))    # bytes，以字节为单位处理的
a2 = a1.decode()    # 解码
print(a2,type(a2))              # str
# 注意：对于bytes，只需要知道它和字符串之间的转换即可

st = "这里是六星教育"
st1 = st.encode("utf-8")
print(st1,type(st1))
st2 = st1.decode("utf-8")
print(st2,type(st2))
# encode 和 decode 后面的括号里可以加上编码方式

# 2.字符串的运算

#     +        字符串连接
a = 'Hello'
b = 'World'
print(a + b)   # HelloWorld

#     *        字符串重复输出
c = 'haha'
print(c*5)

#     []       通过索引获取字符串中的字符
d = 'abcdefg'
print(d[5])    # f      (**注意字符串中字符的下标从0开始)（若从右往左数的话则下标从-1开始递减）
print(d[-1])   # g

# **  [:]      截取字符串中的一部分    （[开始:结束:步长]）
e = 'loveyou'
# 从左往右切
print(e[1:4])      # ove   （**注意方括号中的两个数字分别代表开始和结束的字符串下标，包含开头但不包含结尾）
print(e[4:])       # you    (只在冒号前面写一个数字代表截取从它开始到最后的字符串部分)
print(e[:4])       # love   (只在冒号后面写一个数字代表截取从开始到它前一位的字符串部分)
# 从右往左切
print(e[-1:])      # u
print(e[:-1])      # loveyo
print(e[-7:-3])    # love    (*注意：同样不包括结束下标的字符，只到它的左一位)
print(e[-1:-5])    # **注意：此时不会打任何内容但是也不会报错，因为默认步长为1，即从左往右取
print(e[-1:-5:-1]) # uoye
# **步长：表示选取间隔，若不写则默认为1
#     步长的绝对值大小决定切取的 间隔，正负号决定切取的方向，正号表示从左往右取，负号表示从右往左取
# **技巧：步长的正号需要下标从小到大，负号需要下标从大到小
print(e[0::2])     # lvyu    (即从头开始隔一位取一个直到最后)
print(e[0:5:2])    # lvy
print(e[0:4:2])    # lv
print(e[0:3:2])    # lv

#     in       成员运算符，如果字符串中包含给定的字符或字符串则返回True
f = 'music'
print('m' in f)      # True
print('muc' in f)    # False
#     not in   如果字符串中不包含给定的字符或字符串则返回True
g = '一二三四'
print('二四' not in g)    # True
print('一二' not in g)    # False

# 3.字符串常见操作
# A.查找

# find —— 检测某个子 字符/字符串 在当前字符串里是否存在，若存在则返回其下标，否则就返回-1
# 语法：find(子字符串,开始下标,结束下标)        （若不写开始和结束的下标则默认在整个字符串中查找）
name = 'HelloWorld'
print(name.find('o'))      # 4
print(name.find('llo'))    # 2
print(name.find('o',5))    # 6
print(name.find('o',,4))   # 报错，可以只写开始下标，但是不能只写结束下标
print(name.find('o',0,4))  # -1

# index —— 与find一样的作用和用法，区别是index没找到子字符串时会报错

# count —— 返回某个子字符串出现的次数，若没有出现过则返回0
# 语法：count(子字符串,开始下标,结束下标)
name = 'loveyouloveme'
print(name.count('o'))      # 3
print(name.count('o',5))    # 2
print(name.count('o',5,8))  # 1
print(name.count('love'))   # 2

# B.判断
# startswith —— 是否以某个子字符串开头
# 语法：startswith(子字符串,开始下标,结束下标)
name = 'sixstar'
print(name.startswith('s'))         # True
print(name.startswith('six'))       # True
print(name.startswith('s',2))       # False
print(name.startswith('s',3))       # True
print(name.startswith('star',3))    # True
# endswith —— 是否以某个子字符串结尾
# 语法：endswith(子字符串,开始下标,结束下标)
name = 'sixstar'
print(name.endswith('ar'))       # True
print(name.endswith('er'))       # false
print(name.endswith('st',0,4))   # False
print(name.endswith('st',0,5))   # True
# isupper() —— 判断字符串中的所有字符是否为大写
name = 'sixstar'
print(name.isupper())     # False
print('SIX'.isupper())    # True

# C.修改元素
# replace —— 替换
# 语法：replace(旧内容,新内容,替换次数)    *注意：替换次数可以省略，默认全部替换
name = 'good good study'
print(name.replace('good','bad',0))    # good good study
print(name.replace('good','bad',1))    # bad good study
print(name.replace('good','bad',2))    # bad bad study
print(name.replace('good','bad'))      # bad bad study
# split() —— 指定分隔符来切字符串（将其切成列表的形式）
# 语法：split(分隔符,分割次数)
a = 'Hello,Python'
print(a.split(','))    # ['Hello', 'Python']
# 注意：若字符串中不包含指定的分隔符，就不进行分割，直接输出原内容
print(a.split('o',1))  # ['Hell' , ',Python']
print(a.split('o',2))  # ['Hell' , ',Pyth' , 'n']
# capitalize():第一个字符大写，其余字符全部小写
a = 'helloWorld'
print(a.capitalize())    # Helloworld
# upper() —— 字符全部大写
# lower() —— 字符全部小写


# 十八、列表（list）
# 语法：列表名 = [元素1, 元素2, 元素3, 元素4...]
# *注意：元素之间的数据类型可以不一样，且列表也是可迭代对象，可以用for循环
l = [1, 'a', '一', 3.14]
print(l)         # [1, 'a', '一', 3.14]
print(l[2])      # 一
print(l[1:3])    # ['a', '一']
for i in l:
    print(i)

# 5.列表相关操作
# A.添加元素
# append() —— 整体添加
l = ['one', 'two', 'three']
print(l.append('four'))      # None    (**注意：append会在列表尾部添加元素 'four'，但没有返回任何值（返回 None）)
l.append('four')
print(l)                     # ['one', 'two', 'three', 'four']
# extend() —— 分散添加（将字符串中的每个元素逐个添加）    （**注意：extend里面只能写可迭代对象）
print(l.extend('four'))      # None    (和append同理)
l.extend('four')
print(l)                     # ['one', 'two', 'three', 'f', 'o', 'u', 'r']
l.extend(4)                  # 报错
# insert() —— 在指定位置整体添加
l.insert(3,'four')           # ['one', 'two', 'three', 'four']     若指定位置没有元素则直接插在该位置
l.insert(0,'four')           # ['four', 'one', 'two', 'three']     若指定位置有元素，则插在它前面
l.insert('four')             # 会报错，必须添加要插入的位置

# B.修改元素
# 之间通过下标修改
l = ['one', 'two', 'three']
l[2] = 3    # ['one', 'two', 3]
print(l)

# C.查找元素
# in
# not in
# index
# count
# **注意：没有find

# D.删除元素
# del
l = ['a', 'b', 'c', 'd', 'e']
del l[2]
print(l)    # ['a', 'b', 'd', 'e']
del l       # 删除整个列表，打印会报错
# pop() —— 删除指定下标的元素，python3默认删除最后一个元素
l = ['a', 'b', 'c', 'd', 'e']
l.pop(2)
print(l)    # ['a', 'b', 'd', 'e']
l.pop()
print(l)    # ['a', 'b', 'd']
# remove() —— 删除指定的元素，默认只删除第一个
l = ['a', 'b', 'c', 'd', 'c']
l.remove('b')
print(l)    # ['a', 'c', 'd', 'c']
l.remove('c')
print(l)    # ['a', 'd', 'c']

# 5.排序
# sort —— 将列表按顺序排列，默认从小到大
l = [1, 3, 2, 6, 4, 5]
l.sort()
print(l)
# reverse —— 将列表倒置(不会按大小排序)

# 6.列表推导式
# 写法1：[表达式 for 变量 in 列表]
# *注意：in后面既可以放列表，也可以放 range() 和 可迭代对象
l = [1, 2, 3, 4, 5]
[print(i) for i in l]    # 依次打出l中的每个元素
l = []
[l.append(i) for i in range(1,6)]
print(l)                 # 同样打出1到5的列表
# 写法2：[表达式 for 变量 in 列表 if 条件]
l = []
[l.append(i) for i in range(1,11) if i % 2 == 1]
print(l)                 # 打出1到10的奇数列表

# 7.列表嵌套
l = [1, 2, 3, [4, 5, 6]]
print(l[3])      # [4, 5, 6]
print(l[3][0])    # 4


# 十九、元组
# 语法：tua = (1, 2, 3)
# **注意：定义元组时，若只有一个元素，则要在末尾加上逗号,否则只会打出唯一的元素而不是整个元组
tua = ()    # 定义一个空元组
tua = (1)      # 1
tua = (1,)     # (1,)
# *元组与列表的区别：
#     1.只有一个元素时，元组必须加逗号
#     2.元组只支持查询操作，不支持增删该操作

# *元组的应用场景：
#     1.函数的参数和返回值
#     2.格式化输出的后面的()本质上就是一个元组
print("%s的年龄是：%d" % (name, age))      # 这里的(name, age)就是一个元组
#     3.防止数据被修改，保护数据的安全


# 二十、字典
# 以 键值对 的形式保存，键和值之间用 : 隔开，每个键值对之间用 , 隔开
# 语法：字典名 = {键1:值1，键2:值2，... }
# **注意：键名不能相同，但是值名可以相同
dic = {}    # 定义空字典
dic1 = {'name' : 'a', 'name' : 'b'}      # {'name': 'b'}   如果键名一样，则后面的键值对会取代前面的
dic2 = {'name1' : 'a', 'name2' : 'a'}    # {'name1' : 'a', 'name2' : 'a'}

# 字典的常见操作

# 1.查看元素
# A.字典名[键名]
dic = {'name':'yang', 'age':18}
print(dic[2])         # 报错    （**字典不能根据下标来打印对应的元素）
print(dic['name'])    # yang
print(dic['age'])     # 18
# 字典只能根据键名来打出对应的值，若键名不存在则会报错
# B.变量名.get(键名)
dic = {'name':'yang', 'age':18}
print(dic.get('name'))           # yang
print(dic.get('tel'))            # None     当不存在键名时会返回None
print(dic.get('tel','不存在'))    # 不存在     （**注意：可以通过在键名后面加个元素，使得当找不到键名时返回该元素）

# 2.修改元素
# 字典名[键名] = 新值

# 3.添加元素
# 字典名[新键名] = 值

# 4.删除元素
# A.del
dic = {'name':'yang', 'age':18}
del dic           # 删除整个字典，且找不到该字典了
del dic['age']    # 将该键名及其值删除
# B.claer —— 将字典清空，但是还能找到该字典
# C.pop —— 删除指定键值对，不存在时会报错
dic = {'name':'yang', 'age':18}
dic.pop()        # 报错
dic.popitem()    # python3.7之后的版本默认删除最后一组键值对

# 5.len()求长度
dic = {'name':'yang', 'age':18, 'tel':12345}
print(len(dic))    # 3     返回的是字典里 键值对 的个数

# 6.keys() —— 获取字典里的所有键名
dic = {'name':'yang', 'age':18, 'tel':12345}
print(dic.keys())    # dict_keys(['name', 'age', 'tel'])
for i in dic.keys():
    print(i)            # name     只返回键名
                        # age
                        # tel

# 7.values() —— 返回字典里的所有值
dic = {'name':'yang', 'age':18, 'tel':12345}
print(dic.values())    # dict_values(['yang', 18, 12345])
for i in dic.values():
    print(i)            # yang
                        # 18
                        # 12345

# 8.items() —— 以 元组 的形式返回字典里的键值对
dic = {'name':'yang', 'age':18, 'tel':12345}
print(dic.items())      # dict_items([('name', 'yang'), ('age', 18), ('tel', 12345)])
for i in dic.items():
    print(i)            # ('name', 'yang')
                        # ('age', 18)
                        # ('tel', 12345)

# 字典的应用场景：使用键值对储存描述一个物体的相关信息


# 二十一、集合（set）
# 语法：集合名 = {元素1,元素2,元素3,...}
s1 = set()    # **定义空集合的方式

# **集合具有无序性
s1 = {'a','b','c','d','e'}     # 每次打出来的结果都不一样
s2 = {1,2,3,4,5}               # 打出的结果一样

# **集合具有唯一性，可以自动去重
s = {1,2,3,4,5,1,2,3,4,5}
print(s)    # {1, 2, 3, 4, 5}

# 集合的常见操作

# 1.添加元素
# A.add —— 添加的是一个整体
s1 = {1,2,3,4}
s1.add(4)         # 由于唯一性，不会有变化
s1.add(5)         # {1,2,3,4,5}
s1.add(5,6)       # 报错    **注意：一次只能添加一个元素或元组

# B.update —— 把传入的元素拆分，逐个添加
s1 = {1,2,3,4}
s1.update('567')  # **注意update的括号里只能放可迭代对象

# 2.删除元素
# A.remove —— 选择要删除的元素，有则删除，没有则报错
# B.pop —— 对集合进行无序排序，并删除第一个元素
# C.discard —— 选择要删除的元素，有则删除，没有不会报错

# 交集 &
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1 & s2)    # {3, 4}    *注意：当交集为空时返回 set()

# 并级 ｜
# *注意：当并集为空时会报错


# 二十二、类型转换
# 常见转换语句: int(x)    ——  将（纯数字组成的字符串）转换成整型
a = 1.2
b = int(a)
print(b,type(b))    # 1 <class 'int'>    注意：浮点型转换成整型会直接去掉小数点及后面的数

c = "123"
print(int(c))       # 123
d = "hello"
print(int(d))       # 报错    *注意：只能转换由数字和 正负号 组成的字符串

e = input("请输入年龄：")
if e <= 18
    print("未成年")  # 报错，因为input获取的数据类型默认为字符串类型

#             float(x)  ——  将x转换成浮点型
a = 1
print(float(a))     # 1.0
b = 1.23
print(float(b))     # 1.23
c = '1'
print(float(c))     # 1.0
d = '-1'
print(float(d))     # -1.0

#             str(x)    ——  将x转换成字符串(任何类型都可以转换成字符串类型)
a = 1
print(str(a))       # 1    *注意：此时已经转变成字符串类型了
b = -1.10
print(str(b))       # -1.1    **注意：浮点型转换成字符串时，除了小数点后都为0时会保留一个0，其余情况下都会将末尾的所有0删除

# **          eval(str) ——  计算在 字符串 中的 有效Python表达式，并返回一个对象
print('10+10')          # 10+10
print(eval('10+10'))    # 20

# **注意：eval可以实现 列表、字典、元组和字符串之间的转换
s = '[[1,2],[3,4],[5,6]]'
print(s,type(s))      # [[1,2],[3,4],[5,6]] <class 'str'>
l = eval(s)
print(l,type(l))      # [[1, 2], [3, 4], [5, 6]] <class 'list'>

s2 = "{'name':'yang','age':18}"
print(s2,type(s2))    # {'name':'yang','age':18} <class 'str'>
d = eval(s2)
print(d,type(d))      # {'name': 'yang', 'age': 18} <class 'dict'>
# **注意：eval非常强大，但是不够安全，容易被修改数据，因此不推荐使用

#             tuple(s)  ——  将 序列s 转换成一个 元组
print(tuple('abcde'))                     # ('a', 'b', 'c', 'd', 'e')
print(tuple(12345))                       # 报错,因为tuple()函数需要一个可迭代对象作为参数，而12345是一个整数，不是可迭代对象。

print(tuple((1,2,3,4)))                   # (1, 2, 3, 4)

print(tuple([1,2,3,4]))                   # (1, 2, 3, 4)

print(tuple({'name':'yang','age':18}))    # ('name', 'age'), 只会将键当元素转换成元组

print(tuple({'a','b','c','a'}))           # ('c', 'a', 'b')

#             list(s)   ——  将 序列s 转换成一个 列表
print(list('abcde'))    # ['a', 'b', 'c', 'd', 'e']
print(list(12345))      # 报错    **注意：list后面必须加可迭代对象（str、tuple、dict、set）

print(list((1,2,3,4)))  # [1, 2, 3, 4]

print(list({'name':'yang','age':18}))    # ['name', 'age']    **注意：字典转换成列表只会取其中的 键名 作为列表的元素

print(list({'a','b','c','a'}))           # ['b', 'a', 'c']

#             chr(x)    ——  用于将 字符 转换为对应的 ASCII 码或反之
print(chr(65))     # A
#             ord()     ——  用于将ASCII 码转换为对应的 字符 或反之
print(ord('a'))    # 97


# 二十三、深浅拷贝

# 1.赋值：会随着原对象一起改变（等于完全共享资源，一个值的改变会完全被另一个值共享）
l1 = [1,2,3,4]
l2 = l1
print(l1)    # [1, 2, 3, 4]
print(l2)    # [1, 2, 3, 4]
l1.append(5)    # 给列表1新增元素
print(l1)    # [1, 2, 3, 4, 5]
print(l2)    # [1, 2, 3, 4, 5]

# 2.浅拷贝（数据半共享）
# 会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
# 优点：拷贝速度快，占用空间少，拷贝效率高
import copy    # **注意：要用到深/浅拷贝时要先导入copy模块
l1 = [1,2,3,[4,5,6]]
l2 = copy.copy(l1)  # 浅拷贝的语法：copy.copy(要拷贝的内容)
print(l1,id(l1))    # [1, 2, 3, [4, 5, 6]] 4332674048
print(l2,id(l2))    # [1, 2, 3, [4, 5, 6]] 4332673792    （l1和l2的内存地址不同，说明不是同一个对象）
# **查看内存地址：id()
l1.append(0)
print(l1)           # [1, 2, 3, [4, 5, 6], 0]
print(l2)           # [1, 2, 3, [4, 5, 6]]
l1[3].append(7)
print(l1)           # [1, 2, 3, [4, 5, 6, 7], 0]
print(l2)           # [1, 2, 3, [4, 5, 6, 7]]
# **解释：列表浅拷贝时只有最外层的数据在拷贝后会固定，其余嵌套的列表都会随原拷贝对象的改变而改变
print(id(l1[3]))    # 4300228224
print(id(l2[3]))    # 4300228224    （嵌套的列表的内存地址是一样的）

# 3.深拷贝（数据完全不共享）
# 外层的对象和内部的元素都拷贝了一份
import copy    # **注意：要用到深/浅拷贝时要先导入copy模块
l1 = [1,2,3,[4,5,6]]
l2 = copy.deepcopy(l1)  # 深拷贝的语法：copy.deepcopy(要拷贝的内容)
print(l1,id(l1))    # [1, 2, 3, [4, 5, 6]] 4299086720
print(l2,id(l2))    # [1, 2, 3, [4, 5, 6]] 4299086464
# **查看内存地址：id()
l1.append(0)
print(l1)           # [1, 2, 3, [4, 5, 6], 0]
print(l2)           # [1, 2, 3, [4, 5, 6]]
l1[3].append(7)
print(l1)           # [1, 2, 3, [4, 5, 6, 7], 0]
print(l2)           # [1, 2, 3, [4, 5, 6]]
# **解释：深拷贝数据变化只影响自己本身，跟原来的对象没有一点关系
print(id(l1[3]))    # 4299097472
print(id(l2[3]))    # 4299087424

# 4.可变对象：储存空间保存的数据允许被修改,但是内存地址不会改变
# 常见的可变对象：list,dict,set
# **注意：深/浅拷贝只针对可变对象
d = {'name':'yang','age':18}
print(id(d))    # 4371855040
d['name'] = 'ziang'
print(id(d))    # 4371855040    (地址没有改变)

s = {1,2,3,4,5}
print(id(s))    # 4299289984
s.remove(3)
print(id(s))    # 4299289984    (地址没有改变)

# 5.不可变对象：储存空间保存的数据不允许被修改,如果修改就会生成一个新的值从而分配新的内存空间
# 常见的不可变对象：int,bool,float,complex,str,tuple
i = 1
print(id(i))
i = 0
print(id(i))

s = 'yang'
print(id(s))
s = 'ziang'
print(id(s))

t = (1,2,3)
print(id(t))
t = (4,5,6)
print(id(t))
# 上面三组代码打出的每组地址都不一样


# 二十四、函数基础
# 1.语法：
# def 函数名():    # 函数的定义
#     函数体
# 函数名()         # 函数的调用
# 注意：调用函数前必须保证函数已经存在。函数调用几次就会执行几次，且每次都会从头开始执行
def login():
    print('输入函数')
login()

# 2.返回值(return):函数执行结束后给调用者的一个值
# 注意：函数中遇到return，表示此函数结束，不会继续往下执行
def buy():
    return 'phone'
    return 18
print(buy())    # phone
# 返回值的三种情况：
#    A.一个返回值也没有，返回None
#    B.有一个返回值，返回该值
#  **C.返回多个值，以元组的形式
def mulreturn():
    return 'age',18
print(mulreturn())    # ('age', 18)

# 3.参数
# A.语法：
# def 函数名(形参1，形参2):    # 定义函数
#     函数体
# 函数名(实参a，实参b)         # 调用函数

# B.默认参数：为参数提供默认值，调用函数时可以不传递该默认参数的值
# *注意：所有默认参数都必须放在位置参数（需要传入值）的后面
def fun(a,b,c=18):
    return a,b,c
print(fun(1,2,3))    # (1, 2, 3)    *注意：当默认参数的位置上有传入值时，会用传入的值代替默认值

# C.可变参数：传入的值的数量任意，可以传多个，也可以不传
# 语法：def fun(*args):     **注意：可以把args换成其他的名字，但是args更符合代码的规范性
def fun(*args):
    print(args)    # **注意：在打印的时候用的是“*”后面的参数名
fun()          # ()
fun(1,2,3)     # (1, 2, 3)
# **注意：可变参数是以 元组 的形式接收参数的

# 关键字参数（作用：可以拓展函数的功能）
# 语法：def fun(**kwargs):
def fun(**kwargs):
    print(kwargs)    # **注意：在打印的时候用的是“**”后面的参数名
fun()                           # {}
fun(name = 'yang', age = 18)    # {'name': 'yang', 'age': 18}
# **注意：关键字参数是以 字典 的形式接收参数的，所以在传值的时候也该用字典的方式传,且在函数调用中使用关键字参数时，参数名（关键字）是标识符，不能用引号括起来

# 4.函数嵌套
#  嵌套定义
def study():            # 外函数
    print('study')
    def sleep():        # 内函数
        print('sleep')
    sleep()             # **注意：定义和调用是同级的，因此要缩进。且如果调用在定义里面则永远调用不到
study()


# 二十五、函数进阶

# 1.作用域
# 含义：指的是变量生效的范围，分为全局变量和局部变量

# 全局变量：在函数外部定义的变量，在整个文件中都是有效的
a = 100
def test1():
    print('a in test1:', a)
def test2():
    a = 200
    print('a in test2:', a)
print("调用函数前a的值：", a)    # 100
test1()                       # 100
test2()                       # 200
print("调用函数后a的值：", a)   # 100    *注意：a的值没有被覆盖是因为"函数内部如果要使用变量，会先从函数内部找，有的话直接使用，没有则会到函数外面去找

# 局部变量：函数内部定义的变量，从定义位置开始到函数定义结束位置有效
# 作用：在函数体内部临时保存数据，当函数调用完成之后就销毁局部变量
def fun():
    num = 10
    print('num:', num)
fun()
print('num:', num)    # 报错，局部变量只能在被定义的函数中使用，函数外部不能使用

# 在函数内部定义全局变量（global）
def fun():
    global n
    n = 0
fun()    # 注意：必须先调用函数才能创建全局变量
print('n:',n)

# nonlocal —— 用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数中先进行声明，内部函数进行nonlocal声明（只能对上一级函数进行影响）
def outer():
    a = 10
    def inner():
        nonlocal a
        a = 20
        def inner2():
            nonlocal a    # 将上一级的函数中的a的值变成这一级函数定义的a的值
            a = 30
            print("inner2中a的值：", a)
        inner2()
        print("inner中a的值：", a)
    inner()
    print("outer中a的值：", a)
outer()
# 此时打出来的三个a的值都是30

# 2.*匿名函数
# 语法：函数名 = lambda 形参:返回值
# 调用：结果 = 函数名 (实参)
# 注意：lambda是定义匿名函数的关键字，相当于定义函数时的def
# A.没有参数
funa = lambda : "水果茶"
print(funa())
# B.一个参数
funb = lambda name:name
print(funb("冰冰"))
# C.默认参数
func = lambda name,age=18:(name,age)    # *注意：要以元组的形式返回参数
print(func("冰冰"))
# *注意：默认参数必须写在非默认参数后面
# D.关键字参数
fund = lambda **kwargs:kwargs
print(fund(name = 'bingbing', age = 18))

# lambda结合if判断
com = lambda a,b:"a比b小" if a<b else "a大于等于b"
print(com(5,8))

# *注意：lambda只能实现简单的逻辑，如果逻辑复杂且代码量较大，则不建议使用lambda，否则会降低代码的可读性，为后期的代码维护增加困难

# 3.内置函数
# 查看所有的内置函数：
import builtins
print(dir(builtins))    # 注意：打出来的内容里，大写字母开头一般是内置常量名，小写字母开头一般是内置函数名

# abs() —— 返回绝对值
print(abs(-5))

# sum() —— 求和    （注意只能放可迭代对象，且不能是字符串和字典）
print(sum({1.5,2.5,3}))    # 7.0    注意：只要有一个浮点数，那么结果也为浮点数

# min() —— 求最小值
# max() —— 求最大值
print(min(1,3,5))
print(max([2,4,6]))    # 可以直接放要比较的数字，也可以放可迭代对象

# 求最 大/小 绝对值
print(min(-8,6,key=abs))    # key 参数的作用是指定一个「转换函数」，告诉 min()（或 max()）在比较前先对数据做一次转换

# zip() —— 将多个可迭代对象作为参数，将对象中对应的元素打包成一个个的元组
li1 = [1,2,3]
li2 = ['a','b']
print(zip(li1,li2))    # <zip object at 0x104d6db40>
# 第一种打印方式（for循环）：
for i in zip(li1,li2):
    print(i)
    print(type(i))
# (1, 'a')
# <class 'tuple'>
# (2, 'b')
# <class 'tuple'>
# 注意：当两个可迭代对象的个数不同时，会按照最少的进行配对
# 第二种打印方式（列表）：
print(list(zip(li1,li2)))    # [(1, 'a'), (2, 'b')], 注意：必须是可迭代对象才能这么打印

# map() —— 将可迭代对象中的每个元素依次代入函数中执行程序
# 语法：map(func,iter1)     func —— 自定义函数，iter1 —— 可迭代对象
li = [1,2,3]
def func(x):
    return x * 5
func = lambda x:x * 5    # 定义匿名函数
mp = map(func,li)
print(mp)    # <map object at 0x100dc7940>
for i in mp:
    print(i)
# 5
# 10
# 15

# reduce()  —— 先将可迭代对象中的前两个元素代入函数中计算，再用结果与下一个对象进行计算，以此类推直到所有的元素都代入计算
# 注意：要用reduce函数需要先导包
from functools import reduce
# 语法：reduce(func,sequence)    func —— 自定义函数，且必须有两个参数，sequence —— 可迭代对象
li = [1,2,3,4]
def add(x,y):
    return x+y
add = lambda x,y:x+y
r = reduce(add,li)
print(r)    # 10

# 4.拆包 —— 对于函数中的多个返回值，去掉元组、列表或者字典，直接获取里面的数据的过程
tua = (1,2,3,4)
print(tua)    # (1, 2, 3, 4)
# 拆包方法一：(一般在获取元素值的时候使用)
a,b,c,d = tua    # 将tua里的每个元素依次赋值给a,b,c,d
print(a,b,c,d)    # 1 2 3 4
# 注意：要求可迭代对象中的元素个数与创建的变量个数必须一致
a,b = tua    # 报错（值错误，要拆包的值过多）
# 拆包方法二：（一般在函数调用时使用）
a,*b = tua
print(a,b)    # 1 [2, 3, 4]
def funa(a,b,*args):
    print(a,b)
    print(args,type(args))
funa(1,2,3,4,5,6,7)
# 1 2
# (3, 4, 5, 6, 7) <class 'tuple'>


# 二十六.异常（即bug）

# A.异常的捕获
# 作用：提前假设某处会出现异常，做好提前准备，当出现异常后可以有后续手段
# 语法：
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码

# a.捕获常规异常
try:
    f = open("D:/abc.txt", "r", encoding="UFT-8")
except:
    print("出现异常了，因为文件不存在，我将open的模式改为w模式去打开")
    f = open("D:/abc.txt", "w", encoding="UFT-8")
# b.捕获指定异常：
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)    # name 'name' is not defined
# c.捕获多个异常
try:
    print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义 或 除以0的异常错误")
# d.捕获全部异常
try:

except Exception as e:
    print("出现了异常")

# 异常的else用法:(即没有出现异常时执行的代码)
try:
    print("Hello")
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
# 异常的finally用法：(即不管是否出现异常都会执行的代码)
try:
    print("Hello")
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
finally:
    print("捕获异常结束")

# B.抛出异常raise
# 步骤：
# 1：创建一个Exception('xxx')对象，xxx —— 异常提示信息
# 2：raise抛出这个对象(异常对象)
# 语法：raise Exception("抛出了一个异常")
def funa():
    raise Exception("抛出了一个异常")    # 抛出了一个异常
    print('hh')    # 执行了raise语法就不会执行后面的内容了
funa()

# eg:当输入的密码长度不够时会报的异常
def login():
    pwd = input("请输入密码：")
    if len(pwd) >= 6:
        return "密码输入成功"
    raise Exception("长度不足六位，密码输入失败")
try:
    print(login())
except Exception as e:
    print(e)


# 二十七、模块
# 含义：一个py文件就是一个模块，导入一个模块本质上就是执行一个py文件
# 分类：
# 1.内置模块(eg:random、time、os、logging)
# 2.第三方模块(第三方库)
# 下载第三方模块的方法：cmd窗口输入pip install 模块名
# 3.自定义模块
# **注意：模块命名要遵循标识符规定以及变量的命名规范，并且不要与内置模块起冲突，否则会导致模块功能无法使用

# 导入模块
# 1.import 模块名                       # 可以导入多个模块,但一般只导入一个
# 调用功能：模块名.功能名
# 2.from 模块名 import 功能1,功能2...    # 从指定模块中导入指定部分    # *注意：导入函数时只用写函数名，不用加括号
# 调用功能：直接输入功能即可
# 3.from 模块名 import *                # 导入模块中的全部功能

# as起别名
# 1.模块起别名
# 语法：import 模块名 as 别名
# 2.功能起别名
# 语法：from 模块名 import 功能名 as 别名

# 内置全局变量 __name__
# 语法：if __name__ == "__main__":
# 作用：用来控制py文件在不同的应用场景执行不同的逻辑，在文件中的该if语句里的内容在文件被其他文件导入时不会执行
# 文件在当前程序执行：__name__ == "__main__"
# 文件被当作模块被其他文件导入：__name__ == 模块名


# 二十八、包
# 概念：包就是项目结构中的文件夹/目录
# *注意：与普通文件夹的区别：包含有一个名为__init__.py文件夹
# 作用：将有联系的模块放到同一个文件夹下，有效避免模块名称冲突问题，让结构更清晰
# *注意：import导入包时，首先执行__init__.py文件里的代码
# *注意：不建议在__init__.py文件中写过多代码，要尽量保证该文件的内容简洁
# __all__ :本质上是一个列表，列表里的元素就代表要导入的模块
# 当在__init__.py文件中写到 __all__ = ['模块名']    代表导入包时只导入该模块
# *注意：包的本质依然是模块，包可以包含包


# 二十九、递归函数
# 含义：如果一个函数在内部不调用其他的函数，只调用它本身的话，这个函数就是递归函数
# 条件：
# 1.必须有一个明确的结束条件（递归出口）
# 2.每进行更深一层的递归，问题规模相比上次递归都要有所减少
# 3.相连两次重复调用之间有紧密的联系
# 优点：简洁，逻辑清晰，解题更具有思路
# 缺点：使用递归函数时，需要反复调用函数，耗内存，运行效率低
# 普通函数实现1-100累加
def add1():
    s = 0
    for i in range(1,101):
        s += i
    print(s)
# 递归函数实现1-100累加
def add2(n):
    if n ==1:
        return 1
    return n + add2(n-1)
print(100)

# 递归函数实现求斐波那契数列(1,1,2,3,5,8,13...)的第n项
def func(n):
    if n<=1:
        return n
    return func(n-1) + func(n-2)
print(func(5))


# 三十、闭包&装饰器

# 闭包 —— 特殊的函数
# 条件：
# 1.函数嵌套
# 2.内层函数使用外层函数的局部变量
# 3.外层函数的返回值是内层函数的函数名     *注意：返回函数名而不加括号，因为当内函数里面参数比较多时或受到限制时，写法不太规范
def outer():
    n = 10
    def inner():
        print(n)
    return inner
print(outer())    # 返回的是内部函数的内层地址
# 调用写法一：
outer()()       # 调用内函数
# 调用写法二：
ot = outer()    # 调用外函数
ot()            # 调用内函数

def outer(m):
    n = 10
    def inner(o):
        print(m+n+o)
    return inner
outer(20)(20)

# 函数引用（地址）
def funa():
    print(1)
print(funa)    # 函数名里面保存的是函数所在位置的引用（地址）
# id() —— 获取变量的引用（地址）
# *注意：当变量的值发生改变时，变量的引用（地址）也会发生改变

# 每次开启内函数都在使用同一份闭包变量
def outer(m):
    print(m)
    def inner(n):
        print(n)
        return m+n
    return inner
ot = outer(10)
print(ot(10))
print(ot(50))
print(ot(80))

# 总结：使用闭包的过程中，一旦外函数被调用一次，返回了内函数的引用，虽然每次调用内函数会开启一个函数，执行后消亡，但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量


# 装饰器
# 原理：将原有的函数名重新定义为以原函数为参数的闭包
# 作用：在不改变原有代码的情况下添加新功能
# 条件：
# 1.不修改原函数或程序的代码
# 2.不改变函数或程序的调用方法

# 普通装饰器
def send():       #  被装饰的函数
    print("发送消息")
def outer(fn):    # 装饰器函数
    def inner():
        print("登陆")
        fn()
    return inner
print(outer(send))
ot = outer(send)
ot()

# 语法糖
# 语法：@装饰器名称（即闭包函数名）
def outer(fn):     # 装饰器函数
    def inner():
        print("登陆")
        fn()
    return inner
@outer
def send():        # 被装饰的函数
    print("发送消息")
send()

# A.被装饰的函数有参数
def outer(fn):
    def inner(name):    # name是内函数的参数
        print(f"{name}是inner函数中的参数")
        fn(name)
    return inner
@outer
def func(name):
    print("这是被装饰的函数")
func("bingbing")
# **注意：当以语法糖的形式定义装饰器时，当内函数需要传参时，要给被装饰的函数传同样的参

def func():
    print("这是被装饰的函数")
ot = outer(func)
ot("bingbing")
# **注意：当装饰器以普通形式定义时，此时即使内函数需要传参，被装饰的函数不需要传同样的参数

def outer(fn):
    def inner(*arg,**kwargs):
        print("登录")
        fn(*arg,**kwargs)
    return inner
@outer
def func(*arg,**kwargs):
    print(arg)
    print(kwargs)
func("abc","123",name = "bingbing",age = 18)
# 登录
# ('abc', '123')
# {'name': 'bingbing', 'age': 18}

# B.多个装饰器
# 第一个装饰器
def outer1(fn):
    def inner():
        return "0" + fn() +  "1"
    return inner
# 第二个装饰器
def outer2(fn):
    def inner():
        return "A" + fn() +  "B"
    return inner
# 被装饰函数
@outer1
@outer2
def func():
    return "python"
print(func())    # 0ApythonB1
# **注意：多个语法糖装饰时，由内到外依次执行，即先执行靠下的装饰器


# 一、面向对象基础
# 面向过程和面向对象
# a.面向过程（C）：先分析出解决问题的步骤，然后将每个步骤拆分成一个个方法，通过一个个方法的执行来解决问题
# b.面向对象（Java,Python）：核心是把现实中的事物抽象成 “对象”，每个对象包含描述自身的 “属性”和能做的 “行为”，
#                          再通过对象间的交互来实现功能，让代码更贴近现实、易维护。

# 1.类和对象

# A.类
# a.类的三要素：类名、属性（特征）、方法（功能）
# b.类的基本格式：
# class 类名:
#     代码块
class Washer:
    height = 100
# c.查看类的属性：类名.属性名
print(Washer.height)
# d.新增类的属性：类名. 新属性名 = 值
Washer.width = 500

# B.对象
# 创建一个对象（创建对象的过程也叫实例化对象）
# 实例化对象的格式：对象名 = 类名()
ws1 = Washer()
print(ws1)    # 此时打印出来的是该对象在内存中的地址

# 实例化方法和属性
# a.实例方法:
# 由对象调用，至少有一个 self参数 ，**执行实例方法的时候自动将调用该方法的对象赋值给 self（即self指代该对象）
class Washer:
    height = 100
    def wash(self):    # self代表当前调用该方法的对象
        print("我会洗衣服")
        print("方法中的self：",self)
wa = Washer()
print(wa)    # 此处打出来的内容和上面打印self的内容一样，
wa.wash()    # 对象调用类中的方法

# b.实例属性
class Person:
    name = "bingbing"       # 类属性
    def introduce(self):    # 实例方法
        print(f"my name is:{Person.name},my age is:{self.age}")    # self.age 是个实例属性
p = Person()
p.age = 18
p.introduce()
#  类属性和实例属性的区别：类属性既可以通过类访问到，也可以通过实例对象访问到，而实例属性只能由对象访问到

# 2.构造函数 __init__()
# *作用：通常用来做属性初始化或赋值操作
# 注意：在类实例化对象的时候会自动调用
class Person:
    def __init__(self, name, age, height):    # 该构造函数在对象创建时会自动调用
        self.name = name
        self.age = age
        self.height = height
    def introduce(self):
        print(f"{self.name}的年龄是{self.age},身高是{self.height}")
p1 = Person("bingbing", 18, 160)
p1.introduce()
p1 = Person("ziang", 21, 183)
p1.introduce()

# 3.析构函数 __del__()
# 作用：对象在被垃圾回收的时候起作用，它的执行意味着对象不能继续引用，收回内存
# 删除对象的时候解释器会自动调用__del__()方法
class Person():
    def __init__(self):
        print("这是__init__()")
    def __del__(self):
        print("被销毁了")
p1 = Person()
print("这是最后一行代码")
# 这是__init__()
# 这是最后一行代码
# 被销毁了    -- 对象执行结束后，系统会自动调用__del__()
p2 = Person()
del p2
print("这是最后第二行代码")
# 这是__init__()
# 被销毁了    -- del p语句执行的时候，内存会立即被回收，会调用对象本身的__del__()
# 这是最后第二行代码


# 二、封装
# 封装指的是隐藏对象中的一些不希望被外部所访问到的属性或方法

# 1. xxx   : 普通属性/方法，如果定义在类中，则可以在任何地方使用
# 2. _xxx  : 私有属性/方法，如果定义在类中，外部依然可以使用，子类也可以继承，但是在另一个.py文件中通过from xxx import *导入的时候无法导入
#            一般是为了与Python关键字冲突而采用的命名方式
# 3. __xxx : 隐藏属性/方法，如果定义在类中，则无法在外部直接访问，且子类不会继承，要访问只能通过间接的方式，在另一个.py文件中通过from xxx import *导入的时候也无法导入
#            一般是Python中的魔术方法或属性，都是有特殊含义或者功能的，自己不要轻易定义

# 隐藏属性/方法（私有权限）：只允许在类的内部使用，无法通过对象访问
# 语法：在要隐藏的属性或方法前加两个下划线__
class Person:
    name = "bingbing"       # 类属性
    __age = 18              # 隐藏属性
    def introduce(self):    # 实例方法
        print(f"{Person.name}的年龄是{Person.__age}")
        __age = 100
        print(f"{Person.name}的年龄是{Person.__age}")
p = Person()
print(p.name)
print(p.age)    # 此时会报错
# 第一种类外访问隐藏属性的方法：（知道就行）
# 隐藏属性的本质是将属性名改为：_类名__属性名
print(p._Person__age)    # 此时能打出18
p._Person__age = 100
print(p._Person__age)
# 第二种类外访问隐藏属性的方法：（主要访问方法）
# 在类的内部访问
p.introduce()

# 私有属性/方法
class Person:
    name = "bingbing"    # 普通属性
    __age = 18           # 隐藏属性
    _sex = "gay"         # 私有属性
    def __play(self):        # 隐藏方法
        print("玩手机")
    def _sleep(self):
        print("从早睡到晚")    # 私有方法
    def func(self):          # 普通方法
        print("普通方法")
        Person.__play(self)    # 在实例方法中调用隐藏方法1，（不推荐该方法）
        self.__play()          # 在实例方法中调用隐藏方法2，（推荐该方法）

p = Person()
print(p.sex)    # 报错
# 正确的访问私有属性的方法：对象名._属性名
print(p._sex)
p.__play()    # 报错
p._sleep()


# 三、继承
# 就是让类与类之间转换成父子关系，子类继承父类里的属性和方法
# 语法：
#class 子类名(父类名):
#   代码块

# 1.单继承
class Person:
    def sleep(self):
        print("sleep")
class Man(Person):
    pass    # 占位符，若不写代码且没有占位符会报错
m = Man()
m.sleep()

# 继承的传递（套娃）
class Father:
    def sleep(self):
        print("sleep")
class Son(Father):
    pass
class Dog(Son):
    pass
d = Dog()
d.sleep()

# 方法的重写
#   a.覆盖父类的方法
class Father:
    def money(self):
        print("一百万")
class Son(Father):
    def money(self):
        print("挣一千万")
s = Son()
s.money()

#   b.对父类的方法进行扩展
#       i. 父类名.方法名(self)
class Father:
    def money(self):
        print("一百万")
class Son(Father):
    def money(self):
        Father.money(self)
        print("挣一千万")
s = Son()
s.money()

#       ii. super().方法名()    -- 推荐使用（*注意：方法名后面的括号里不用加self）
# super在Python中是个特殊的类，super()是使用super类实例化的对象，可以调用父类的方法
class Father:
    def money(self):
        print("一百万")
class Son(Father):
    def money(self):
        super().money()
        print("挣一千万")
s = Son()
s.money()

#       iii. super(子类名, self).方法名()    -- 是第二种方法的展开写法
class Father:
    def money(self):
        print("一百万")
class Son(Father):
    def money(self):
        super(Son,self).money()
        print("挣一千万")
s = Son()
s.money()

# 新式类：继承了object类或者其子类的类都是新式类  -- 推荐使用
# 语法：class 类名(object)
# object -- 对象，Python为所有类提供的基类（顶级父类），提供了一些内置属性和方法，可以使用dir()来查看
print(dir(object))
# *注意：在Python3中，当一个类没有继承任何类时，会默认继承object类，所以在Python3中都是新式类

# 2.多继承
# 子类可以有多个父类，并继承所有父类的属性和方法
# *多继承的弊端：容易引发冲突，使得代码设计的复杂度增加
class Father(object):
    def money(self):
        print("一百万")
class Mother(object):
    def money(self):
        print("二百万")
    def appearance(self):
        print("美貌")
class Child(Father, Mother):
    pass
c = Child()
c.money()    # *注意：当多个父类有同名属性或方法时，遵循就近调用原则，即写在前面的父类被调用
c.appearance()

# 方法的搜索顺序:(仅供了解)
# Python3中可以使用内置属性__mro__查看方法搜索顺序,其结果表示会按照从左到右的顺序查找
print(Child.__mro__)


# 四、多态
# 指同一种行为具有不同的表现形式
# *多态的前提：继承、重写

# 多态的例子
print(10 + 10)        # 20      -- 加号作为算数运算符
print("10" + "10")    # 1010    -- 加号用作字符串拼接

class Animal(object):
    '''父类：动物类'''    # 对类和函数进行描述时推荐使用这种注释方式
    def shout(self):
        print("动物叫声")
class Cat(Animal):
    '''子类1：猫类'''
    def shout(self):
        print("喵喵叫")
class Dog(Animal):
    '''子类2：狗类'''
    def shout(self):
        print("汪汪叫")
cat = Cat()
cat.shout()
dog = Dog()
dog.shout()

# 多态性：定义一个统一的接口，一个接口多种实现（一种调用方式有不同的执行结果）
class Animal(object):
    def eat(self):
        print("food")
class Pig(object):
    def eat(self):
        print("猪饲料")
class Dog(Pig):
    def eat(self):
        print("狗粮")

def test(obj):
    obj.eat()
dog = Dog()
dog.eat()
test(dog)
pig = Pig()
pig.eat()
test(pig)
# test函数传入不同的对象，执行不同对象的eat方法

# 静态方法： @staticmethod
# 使用@staticmethod进行修饰，静态方法没有self、cls参数的限制
# 静态方法与类无关，可以被转换成函数使用
# 静态方法的优势：取消不必要的参数传递，减少不必要的内存占用和性能消耗
class Person(object):
    @staticmethod
    def func():
        print("func")
# 静态方法既可以使用对象调用，也可以使用类访问
Person.func()
p = Person()
p.func()

# 类方法:  @classmethod
# 使用装饰器@classmethod来标识其为类方法，*注意：第一个参数必须是类对象，一般是以cls作为第一个参数
# 类方法内部可以访问类属性，或者调用其他的类方法
# 当方法中需要使用到类对象（如访问私有类属性等），则定义类方法
# 类方法一般配合类属性使用
class Person(object):
    name = "bingbing"
    @classmethod
    def sleep(cls):
        print(cls)    # <class '__main__.Person'>    -- 其和 print(Person) 所打出来的内容一样，所以cls就代表类本身，类本质上就是一个对象
        print("sleep")
        print(cls.name)
Person.sleep()

# 三种方法的区别
# 实例方法：在方法内部访问实例属性和类属性
# 静态方法：方法内部不需要访问实例属性和类属性（注意：其不能访问实例属性）
# 类方法：方法内部只需要访问类属性，
class Person(object):
    name = "bingbing"
    def __init__(self):
        self.age = 18
    def play(self):
        print(f"{Person.name}在玩游戏")
        print(self.age)
    @staticmethod
    def introduce():
        print(f"我的名字是{Person.name}")
        print(self.age)    # 此时会报错
    @classmethod
    def sleep(cls):
        print(f"{cls.name}在睡觉")
        print(cls.age)    # 此时也会报错
p = Person()
p.play()
p.introduce()
p.sleep()
# 类属性是公共的，所有的方法都能访问到（但静态方法不需要访问类属性，其和类和对象没有关联），而实例属性是私有的，只有实例方法内部才能够访问到


# 五、单例模式
# 可以理解成一个特殊的类，其只存在一个对象（如一个号不能在多个设备上同时登录）
# 优势：节省内存空间，减少了不必要的资源浪费
# 缺点：多线程访问的时候容易引发线程安全问题

# __init__()和__new__():
# __init__() -- 初始化对象
class Test(object):
    def __init__(self):
        print("这是__init__()")
    def __new__(cls, *args, **kwargs):
        print("这是__new__()")
        res = super().__new__(cls)    # 方法重写，res里面保存的是实例对象的引用
        return res
        # **注意：重写__new__()时，一定要return super().__new__(cls)，否则Python解释器得不到分配空间的对象引用，就不会调用__init__()
t = Test()
# __new__() -- 是object提供的内置的静态方法（其调用在__init__()之前）
# 作用：1.在内存中开辟空间。2.返回对象的引用（将其作为self）
# 总结：
#       1. __new__()是创建对象，__init__()是初始化对象
#       2. __new__()是返回对象引用，__init__()是定义实例属性
#       3. __new__()是类方法，__init__()是实例方法

# 实现单例模式的方式：
#   1. 通过 @classmethod
#   2. 通过 装饰器
#   3. 通过 重写__new__()    （*重点*）
#   4. 通过 导入模块

class A(object):
    pass
a1 = A()
a2 = A()
print(a1)
print(a2)
# 上面打出来的两个地址不一样，说明是不同的对象
# 为了实现单例模式，需要对象的内存地址都一样，即只有一个对象

#   3. 通过重写__new__()实现单例模式
# 设计流程：
#   1. 定义一个类属性，其初始值为None，用来记录单例对象的引用
#   2. 重写__new__()方法
#   3. 进行判断，如果类属性为None，把__new__()返回的对象引用保存进去
#   4. 返回类属性中记录的对象的引用
class Singleton(object):
    obj = None
    def __new__(cls, *args, **kwargs):
        print("这是__new__()")
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj
    def __init__(self):
        print("这是__init__()")
s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)

#   4. 通过导入模块实现单例模式
#在test.py文件中写：
class Test(object):
    def func(self):
        print("这是test")
t = Test()
#回到现在的py文件中：
from test import t as t1
from test import t as t2
print(t1)
print(t2)
# 导入后创建新变量的本质是给原变量起别名，所以上面两个打出来的地址一样


# 六、魔法（魔术）方法&属性

# 常见的魔法方法&属性：
# __new__():在内存中为对象分配空间并返回对象的引用
# __init__():初始化对象或给属性赋值（构造函数）
# __doc__:类的描述信息
# __module__:表示当前操作对象所在的模块
# __class__:表示当前操作对象所在的类
# __str__():对象的描述信息（*注意：必须要有返回值，且一定是字符串类型）
class A(object):
    def __str__(self):
        return "这是str的返回值"
a = A()
print(a)
# __del__():删除对象（析构函数）
# __call__():使一个实例对象成为一个可调用对象，就像函数一样可以调用（callable -- 判断一个对象是否是可调用对象）
class A(object):
    def __call__(self):
        print("这是__call__()")
a = A()
a()    # **调用一个可调用的实例对象，其实就是在调用它的__call__()方法
# __dict__():返回对象具有的属性和方法


# 七、文件
# 文件就是储存在某种长期储存设备上的一段代码
# 文件操作： 打开文件 --> 读、写文件 --> 保存文件

#   1.文件读写
#        a.文件对象的方法：
#   open():创建一个 file对象，默认是以只读对象创建
#   read(n):读取文件，n表示从文件中读取数据的长度，不写或传入负值则默认读取全部的文件
#   readline(): 一次读取一行内容，方法执行完会把文件指针移动到下一行，等待继续读取
#   readlines():按照行的方式一次性读取文件的全部内容
#   write():将指定内容写入文件
#   close():关闭文件

#       b.属性：
# 文件名.name:返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode:返回文件的访问模式
# 文件名.closed:检测文件是否关闭，关闭则返回True

# 在当前PyCharm文件夹创建一个名为 test.txt 的普通文件，写了：
bingbing18
# 在桌面创建一个同样名为 test.txt 的文件，写了：
hahaha
# 返回现在的文件：
f = open("text.txt")
print(f.read())      # bingbing18
print(f.read(-1))    # bingbing18
print(f.read(4))     # bing
print(f.name)      # text.txt
print(f.mode)      # r    -- 表示只读模式
print(f.closed)    # False
f.close()          # *注意：必须打开文件后必须有关闭文件操作
print(f.closed)    # True

f2 = open(r"桌面test.txt文件的路径\test.txt")    # 引号前面的r使括号内的符号转义，注意在文件路径后面要加上 “\文件名”
print(f2.name)       # 文件路径\文件名    即文件的具体路径（绝对路径）
print(f2.read())     # hahaha
f2.close()

# 在PyCharm文件夹的test.txt文件中增加内容为：
bingbing18
susu18
ziyi18
# 回到现在的文件中写：
f3 = open("text.txt")
print(f3.readline())
print(f3.readline())
print(f3.readline())
# 上面的三行代码会将上面test.txt文件中的三行内容依次打出来，但是中间会空一行
while True:
    text = f3.readline()
    if not test:
        break
    print(test)
f3.close()

f4 = open("text.txt")
text = f4.readlines()
print(text)    # ['bingbing18\n' 'susu18\n' 'ziyi18']    -- 以列表的形式打印
for i in text:
    print(i)    # 此次打出来的文件中的三行内容之间依然有换行
f4.close()

#   2.访问模式
# r : 只读模式（默认模式），当文件不存在时会报错
# w : 只写模式，若文件存在会先清空文件的内容再写入新内容，文件不存在则会创建文件
f = open("test.txt", "r")
f.write("hahaha")    # 报错
f.close()
f = open("test01.txt", "w")
f.write("hahaha")    # 会先创建文件然后写入内容
f.write("123456")    # hahaha123456    -- 会接在上面的内容后面
f.close()

# 若想要可读可写则需要用到 + （**注意：使用“+”会影响文件的读写效率，因此开发过程中更多时候以只读、只写的方式来操作文件）
# r+ : 可读写文件，文件不存在时会报错
# w+ : 先写再读文件，文件存在就重新编辑文件，不存在就创建文件
f = open("test.txt", "w+")
f.write("hahaha")
print(f.read())    # 此时不会打印任何内容，因为在执行完上面的写入操作后，文件指针位于编写内容后面，在执行该读取操作时会从文件指针的位置往后读取
f.close()

# 文件指针：标记从哪个位置开始读取数据

# a : 追加模式，不存在文件就创建文件进行写入，存在文件就在原内容的基础上写入新内容（*注意：不能进行读取操作）
# a+ :
f = open("test.txt", "a")
print(f.read())      # 报错
f.write("ABCDE")     # 会直接接在原文件的内容后面（不会换行）
f.write("\nABCDE")   # 此时会换行写入新内容
f.close()

#   文件定位操作：
# tell(): 显示文件内当前位置，即文件指针的当前位置
# seek(offset, whence): 移动文件指针到指定位置（offset -- 偏移量，表示要移动的字节数；whence -- 起始位置，表示移动字节的参考位置，默认为0，0代表文件开头作为参考位置，1代表当前位置作为参考位置，2代表文件结尾作为参考位置）
# seek(0, 0)会将文件指针移动到文件开头
f = open("test.txt", "w+")
f.write("hello python")
t = f.tell()
print(t)      # 12  -- 文件内容长度
f.seek(0,0)
t2 = f.tell()
print(t2)     # 0   -- 将指针移动到了开头
print(f.read())
f.close()

#   with open : 代码执行完后自动调用close()方法，可以省略关闭文件步骤
with open("test.txt","w") as f:
    f.write("hello python")
print(f.closed)    # True

#   3.编码格式
# 文件对象的 encoding参数 的默认值与平台有关（如：Windows系统上默认字符编码为 gbk）
with open("test.txt", "w") as f:
    f.write("冰冰18岁")    # 此时在test.txt文件中会出现乱码，不会将文字打进去，因为在写入中文时文件编码格式是gbk -- PyCharm将中文显示为16进制的数
with open("test.txt", "w", encoding = "utf-8") as f:    # encoding表示编码集，根据文件的实际保存编码进行获取数据，对于我们而言最常用的是 utf-8
    f.write("冰冰18岁")
with open("test.txt", "r", encoding = "utf-8") as f:
    print(f.read())    # 要想读取中文也需要写入： encoding = "utf-8"

# 案例：图片复制（要用到"rb"/"wb"）
# 找到电脑中的一个图片获取其地址和名字
# 1.读取图片（图片是个二进制文件，想要写入必须先拿到）
with open(r"图片地址\图片名字", "rb") as f:
    print(f.read())     # 此时打出来的是一些二进制数
# 2.写入图片
# 将读取到的内容写入到当前的文件夹中
with open(r"图片地址\图片名字", "wb") as f:
    f.write(f.read())

#   4.目录常用操作
# *在使用之前要先导入模块
import os

#       a.文件重命名:os.rename(旧文件名, 新文件名)
#       b.删除文件:os.remove(目标文件名)
#       c.创建文件夹:os.mkdir(文件夹名)
#       d.获取当前目录（当前文件夹路径）:os.getcwd()
#       e.获取目录列表:os.listdir(目录)    默认获取当前目录列表
print(os.listdir("../../"))    # 获取上一级目录列表
#       f.删除文件夹:os.rmdir(文件夹名)


# 八、迭代器&生成器

# 可迭代对象(Iterable):可以放入for···in···这类语句遍历读取数据的对象 （eg：str、list、tuple、dict、set···）
# 迭代(遍历)：依次从对象中把一个个元素取出来的过程
# 可迭代对象的条件：对象实现了__iter__()方法，且__iter__()方法返回了迭代器对象

# for循环的工作原理：
# 1.先通过__iter__()获取可迭代对象的迭代器
# 2.对获取到的迭代器不断调用__next__()方法来获取下一个值并将其赋值给临时变量（eg：i）

# isinstance(o, t):判断一个对象是否是可迭代对象，或者是一个已知的数据类型    (o -- 对象，t -- 数据类型（可以是直接或间接类名、基本类型、元组）)
# 使用前需要导入模块：
from collections.abc import Iterable
print(isinstance(1234, str))    # False
print(isinstance("123", Iterable))     # True
print(isinstance("123", (int, str)))    # True    (对象只要满足括号里的一个类型就返回True)

# 迭代器(Iterator)：是一个可以记住遍历位置的对象，在上一次停留的位置继续去做一些事情
# iter()：获取可迭代对象的迭代器对象    （iter()本质上会调用对象的__iter__()方法，并把__iter__()方法的返回结果作为自己的返回值）
# next()：一个个去取元素，取完元素后会引发StopIteration异常    （**注意：括号里需要放入一个迭代器对象）    （next()本质上也会调用对象的__next__()方法）
li = [1, 2, 3, 4, 5]
li2 = iter(li)      # 创建迭代器对象
# li2 = li.__iter__()    # 作用与上面一行的代码相同
print(li2)          # <list_iterator object at 0x0000013EFAA7E488>
print(next(li2))    # 1
# print(li2.__next__())    # 作用与上面一行的代码相同
print(next(li2))    # 2
print(next(li2))    # 3
print(next(li2))    # 4
print(next(li2))    # 5
print(next(li2))    # 出现StopIteration异常

# 迭代器协议：对象必须提供一个next方法，执行该方法 要么就返回迭代中的下一项，要么就引发StopIteration异常来终止迭代

# 自定义迭代器类：
class MyIterator(object):
    def __init__(self):
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num == 100:
            raise StopIteration("终止迭代，数据已经被取完了")
        self.num += 1
        return self.num
mi = MyIterator()
print(next(mi))
for i in mi:
    print(i)
print(isinstance(mi, Iterable))

# 生成器（generator） -- Python中一边循环一边计算的机制，能让我们自己写出迭代器

# 列表推导式：
li = [i*5 for i in range(5)]
print(li)    # [0, 5, 10, 15, 20]

# 生成器表达式：
gen = (i*5 for i in range(5))
print(gen)     # 此时打出来的是生成器的地址
print(next(gen))     # 0
print(next(gen))     # 5
print(next(gen))     # 10
print(next(gen))     # 15
print(next(gen))     # 20
print(next(gen))     # 引发StopIteration错误

# 生成器函数：Python中使用了yield关键字的函数
# yield的作用：（函数中断并保存中断的状态）
# 1. 类似return，将一个或多个值返回给调用者
# 2. yield语句一次返回一个结果，在每个结果中间，挂起函数，执行__next()__，再重新从挂起点继续往下执行
def gen():
    print("开始")
    yield "a"    # 返回一个a并暂停函数，在此处挂起，下一次从此处继续执行
    yield "b"
    yield "c"
gen1 = gen()
print(gen1)    # <generator object gen at 0x0000026922CC11C8>
print(next(gen1))    # 开始
                     # a
print(next(gen1))    # b
print(next(gen1))    # c
print(next(gen1))    # 引发StopIteration错误

def gen2(n):
    li = []
    for i in range(n):
        li.append(i)
        yield i
    print("li:", li)
print(gen2(5))    # <generator object gen2 at 0x000002858A0811C8>
for i in gen2(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
# li: [0, 1, 2, 3, 4]


# 九、线程

import time
def dance():
    print("开始跳舞")
    time.sleep(2)    # 睡眠操作，以秒为单位
    print("结束跳舞")
def sining():
    print("开始唱歌")
    time.sleep(2)    # 睡眠操作，以秒为单位
    print("结束唱歌")
dance()
sining()
# 上面两个函数是依次进行的，而不是同时进行的

# 进程和线程
# 进程：是操作系统进行资源分配的基本单位，每打开一个程序就至少就会有一个进程
# 线程：是cpu调度的基本单位，每一个进程至少会有一个线程，这个线程通常就是我们所说的主线程
# 关系：一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程

# 多线程：同时运行多个线程
# 使用前需要导入线程模块：
import threading
# Thread: 线程类参数
# target: 执行的任务名
# args: 以元组的形式给任务传参
# kwargs: 以字典的形式给任务传参

def dance(name):
    print(f"{name}开始跳舞")
    time.sleep(2)    # 睡眠操作，以秒为单位
    print("结束跳舞")
def sining(name):
    print(f"{name}开始唱歌")
    time.sleep(2)    # 睡眠操作，以秒为单位
    print("结束唱歌")

# 主程序入口    （为了代码规范建议写上以下的if判断句）
# 写入if判断句的用处：
# 1. 防止别人导入文件的时候执行main里面的方法
# 2. 防止Windows系统递归创建子进程
if __name__ == '__main__':
    # 1.创建子线程
    t1 = threading.Thread(target=sining, args=("bingbing",))    # **注意：当元组只传入一个参数时，要在该参数后面加逗号
    t2 = threading.Thread(target=dance, args=("bingbing",))
    # print(t1)    # 不会打印，需要启动

    # 3.守护线程: 主线程执行结束，子线程也会执行结束（注意：必须放在启动线程前）
    t1.setDaemon(True)
    t2.setDaemon(True)

    # 2.启动子线程
    t1.start()
    t2.start()

    # 4. 阻塞主线程：起到暂停的作用，等子线程执行结束后，主线程才会继续执行，（注意：必须放在启动线程后）
    t1.join()
    t2.join()

    # 5.获取线程名字：
    print(t1.getName())    # Thread-1 (默认名字)
    print(t2.getName())    # Thread-2

    # 6.更改线程名字：
    t1.setName("子线程1")
    t2.setName("子线程2")
    print(t1.getName())    # 子线程1
    print(t2.getName())    # 子线程2

    print("结束表演")
    # 若没有3和4，则“结束表演”会打在“开始唱歌跳舞”和“结束唱歌跳舞之间”
    # 若只有3，则在打完“开始唱歌跳舞”后会打印“结束表演”并结束子线程，即不会打“结束唱歌跳舞”    此时“结束唱歌”和"结束跳舞"会打在同一行，因为--资源竞争
# 在上面的代码中，由于后面使用了 join() 方法（第4步），会阻塞主线程等待子线程执行完毕，
# 所以此时守护线程（第3步）的设置实际上不会产生效果（因为 join() 已经确保主线程会等待子线程完成）
# 守护线程的典型使用场景是：
# 1.当子线程是 "辅助性" 的任务（如日志记录、后台监控等）
# 2.你希望主线程结束时，这些辅助线程也随之结束，不需要继续运行
# 3.避免主线程退出后，子线程还在运行导致程序无法正常结束

# 多线程的特点：
# 1.线程之间执行是无序的（线程执行是根据cpu调度决定的）
def task():
    time.sleep(1)
    print("当前线程是：", threading.current_thread().name)    # 后面的函数用来显示当前线程对象名
if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=task)
        t.start()
# 执行上面代码会发现每次打出来的线程对象名的顺序都不一样

# 2.线程之间共享资源
li = []
def wdate():
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print("写入的数据是：", li)
def rdate():
    print("读取的数据是：", li)
if __name__ == "__main__":
    w = threading.Thread(target=wdate)
    r = threading.Thread(target=rdate)
    w.start()
    w.join()
    r.start()
    r.join()
    # 若不加入上面两个阻塞线程（join）语句的话，则会先打读后打写

# 3.资源竞争
a = 0
b = 100000000
def add():
    for i in range(b):
        global a
        a += 1
    print(a)
def add2():
    for i in range(b):
        global a
        a += 1
    print(a)
if __name__ == "__main__":
    a1 = threading.Thread(target=add)
    a2 = threading.Thread(target=add2)
    a1.start()
    a1.join()    # 代码意义：等待a1子线程执行结束以后，代码再继续往下运行，开始执行a2子线程
    a2.start()
    a2.join()    # 代码意义: **即使a2之后没有其他需要执行的子线程，也依然要加上线程阻塞语句，
                 # 因为若不加阻塞语句，主线程（if __name__ == "__main__": 所在的线程）在启动a2子线程后会继续执行后续代码（此处后续没有其他代码，但主线程会直接结束），
                 # 当主线程结束时，即使子线程 a2 还未执行完毕，整个程序也会退出，可能导致 a2 的任务未完成
    # 同样若不写入阻塞语句（join）的话，打出来的结果每次都不一样

# 为了避免上面的问题发生需要做到 线程同步，一般有两种方法实现：
# 1.线程等待（即使用线程阻塞（join）语句）
# 2.互斥锁
    # 概念：对共享数据进行锁定，保证多个线程访问共享数据不会出现数据错误问题（保证同一时刻只能有一个线程去操作）
    # *缺点：会影响代码的执行效率
    # 语法：
        # acquire() -- 上锁
        # release() -- 释放锁
        # **注意：这两种方法必须成对出现，否则容易形成死锁（即一直等待释放锁的情景，会造成应用程序停止响应，不能处理其他任务）
# 导入模块
from threading import Lock
lock = Lock()    # *创建全局互斥锁（必须要有，否则每次调用Lock()都会创建一个新的锁对象，
                 # 由于两个线程使用的是不同的锁，它们无法相互制约 ——add 上锁时，add2 仍能同时执行）
a = 0
b = 100000000
def add():
    lock.acquire()     # 上锁
    for i in range(b):
        global a
        a += 1
    print(a)
    lock.release()     # 释放锁
def add2():
    lock.acquire()     # 上锁
    for i in range(b):
        global a
        a += 1
    print(a)
    lock.release()     # 释放锁
if __name__ == "__main__":
    a1 = threading.Thread(target=add)
    a2 = threading.Thread(target=add2)
    a1.start()
    a2.start()

# 导入线程模块时为了方便后续创建子线程可以这么写导入：
from threading import Thread

if __name__ == '__main__':
    t = Thread(target=func)    # 不用在前面加上 threading. 了
    t.start()


# 十、进程
# 是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
# 一个正在运行的程序或者软件就是一个进程（程序跑起来就成了进程）
# 程序是静态概念，而进程是动态概念

# 进程的状态：
# 1. 就绪状态：运行的条件都已经满足了，正在等待cpu执行
# 2. 执行状态：cpu正在执行其功能
# 3. 等待（阻塞）状态：等待某些条件满足，如一个程序sleep了，此时就处于等待状态

# 进程语法结构
# multiprocessing 模块提供了Process类 代表进程对象
from multiprocessing import Process
# 1. Process类参数：
    # 1. target：执行的目标任务名，即子进程要执行的任务
    # 2. args：以元组的形式进行传参
    # 3. kargs：以字典的形式进行传参
# 2. 常用的方法：
    # 1. start()：开启子进程
    # 2. is_alive()：判断子进程是否还活着，存活返回True，否则返回False
    # 3. join()：主进程等待子进程执行结束
# 3. 常用的属性：
    # 1. name：当前进程的别名，默认为Process-N（N为由1开始递增的整数）
    # 2. pid：当前进程的进程编号
import os    # 为了查看父进程的编号
def sing():
    # os.getpid():获取当前进程的编号
    # os.getppid():获取当前父进程的编号
    print(f"sing子进程的编号：{os.getpid()}，父进程的编号：{os.getppid()}")    # 该父进程的pid就是py文件主进程的id
    print("唱歌")
def dance():
    print(f"dance子进程的编号：{os.getpid()}，父进程的编号：{os.getppid()}")
    print("跳舞")
if __name__ == "__main__":
    # 创建子进程
    p1 = Process(target=sing, name="子进程一")    # 第一种修改子进程名字的方式
    p2 = Process(target=dance, name="子进程二")
    # 启动子进程
    p1.start()
    p2.start()
    # 第二种修改子进程名字的方式
    p1.name = "子进程1"
    p2.name = "子进程2"
    # 访问name属性
    print("p1:",p1.name)
    print("p2:",p2.name)
    # 查看子进程的进程编号
    print("p1.pid:",p1.pid)
    print("p2.pid:",p2.pid)
    print(f"主进程pid：{os.getpid()}，其父进程pid：{os.getppid()}",)    # 该父进程pid其实就是PyCharm软件的进程编号
    # cmd命令提示符窗口输入tasklist可以查看电脑里面进程的命令
    # Ctrl + Shift + F ：关键字查找
def eat(name):
    print(f"{name}在吃饭")
def sleep(name):
    print(f"{name}在睡觉")
if __name__ == "__main__":
    p1 = Process(target=eat, args=("bingbing",))
    p2 = Process(target=sleep, args=("ziyi",))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("p1的存活状态：", p1.is_alive())    # False
    print("p2的存活状态：", p2.is_alive())    # False
    # *注意：写在主进程中判断存活状态的时候要加入join()阻塞一下 （上面若不加入阻塞语句打出来的都会是True）

# **注意：进程间不共享全局变量
from time import sleep
li = []
def write():
    for i in range(5):
        li.append(i)
        sleep(1)
    print("写入的数据是：", li)
def read():
    print("读取的数据是：", li)
if __name__ == "__main__":
    p1 = Process(target=write)
    p2 = Process(target=read)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
# 执行上面代码打出来的读取数据一直是空列表

# 进程间的通信
# 作用：让资源进行传输
# 需要用到Queue队列：
# 1. q.put()：放入数据
# 2. q.get()： 取出数据，然后将其从队列中移除
# 3. q.empty()：判断队列是否为空
# 4. q.qsize()：返回当前队列包含的消息数量
# 5. q.full()：判断队列是否满了

# 导入模块
from queue import Queue
# 初始化一个队列对象
q = Queue(3)    # 括号里面的是队列的大小，即可以接受多少消息，若为空或负值则代表无上限
q.put("一")
q.put("二")
print(q.full())     # False
q.put("三")
print(q.full())     # True
print(q.qsize())    # 3
print(q.get())      # 一
print(q.get())      # 二
print(q.empty())    # False
print(q.get())      # 三
print(q.qsize())    # 0
print(q.empty())    # True

from multiprocessing import Process, Queue    # 进程模块中自带Queue队列
li = ["张三", "李四", "王五", "赵六"]
def write(q1):
    for i in range(4):
        print(f"{i}已经被放入")
        q1.put(li[i])
        sleep(1)
def read(q2):
    while True:
        if q2.empty():
            break
        else:
            print("取出数据：", q2.get())
if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=write, args=(q,))
    p2 = Process(target=read, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

# 进程池：预先创建一定数量的进程，将任务分配给这些进程执行，任务完成后进程不销毁而是继续等待新任务，从而避免频繁创建和销毁进程带来的性能开销

# 进程池的工作流程：
# 1. 初始化进程池：指定进程池中的进程数量（通常根据cpu核心数设定，避免资源浪费）
# 2. 提交任务：将需要执行的任务提交给进程池，进程池会分配空闲进程处理任务
# 3. 执行任务：进程处理完当前任务后不会销毁，而是回到“空闲”状态，等待处理新任务
# 4. 关闭进程池：所有任务完成后，关闭进程池，释放资源

# Python 的 multiprocessing 模块提供了 Pool 类来实现进程池，常用方法如下：
# 1. Pool(n)：创建一个包含n个进程的进程池（n默认为cpu核心数）
# 2. apply(func, args)：同步提交任务（阻塞等待任务完成，效率低，不常用）
# 3. apply_async(func, args)：异步提交任务（非阻塞，立即返回，常用）
# 4. close()：关闭进程池，不再接受新任务
# 5. join()：等待所有任务完成后，再继续执行后续代码（需在 close() 后调用）
# 6. terminate()：立即终止所有进程（不管任务是否完成）

from multiprocessing import Pool

def task(num):
    time.sleep(1)
    return num * num

if __name__ == "__main__":
    # 创建包含两个进程的进程池
    pool = Pool(2)

    # 准备任务参数（1-5的平方）
    nums = [1, 2, 3, 4, 5]

    # 异步提交所有任务（返回一个迭代器）
    result = pool.map_async(task, nums)    # map_async -- 批量提交任务

    # 关闭进程池
    pool.close()

    # 等待所有任务完成
    pool.join()

    # 获取任务结果
    print("结果：", result.get())    # 结果： [1, 4, 9, 16, 25]

# 在上面的代码中，创建的进程池会并发执行task函数的不同实例（即针对不同参数的调用）
# **注意：task函数是 “任务模板”，我们提交给进程池的是基于这个函数的多个具体任务（比如用参数1,2,3,4,5分别调用task）。
#        这些任务本质上是task(1)、task(2)、task(3)、task(4)、task(5)这 5 个独立的函数调用。
# 上面代码的运行过程：
# 1. 一开始，进程 1 处理task(1)，进程 2 处理task(2)（同时进行，各耗时 1 秒）
# 2. 1 秒后，两个进程完成任务并回到 “空闲” 状态，进程池分配它们处理下一批任务：进程 1 处理task(3)，进程 2 处理task(4)（再耗时 1 秒）
# 3. 又 1 秒后，两个进程再次空闲，进程 1 处理最后一个任务task(5)（耗时 1 秒）
# 4. 总耗时约 3 秒（而不是单进程的 5 秒），体现了并发效率


# 十一、协程
# 协程又称为微线程，是单线程下的开发
# **注意：线程和进程的操作是由程序触发系统接口，最后的执行者是系统。而协程的操作则是程序员
# 应用场景：
# 1. 如果一个线程里面IO操作（输入/输出操作）比较多的时候，可以用协程
#    常见的IO操作：文件操作、网络请求
# 2. 适合高并发处理

# 简单实现协程
import time
def task1():
    yield "a"
    yield "哈哈哈"
def task2():
    yield "b"
    yield "呵呵呵"
def task3():
    while True:
        yield "c"
def task4():
    while True:
        yield "d"
if __name__ == "__main__":
    t1 = task1()
    t2 = task2()
    print(t1)
    print(next(t1))
    print(next(t1))
    print(next(t2))
    print(next(t2))
    t3 = task3()
    t4 = task4()
    while True:
        print(next(t3))
        print(next(t4))

# greenlet：是一个由C语音实现的协程模块，通过设置switch()来实现任意函数之间的切换
# 为了更好使用协程来完成多任务，Python提供了第三方模块 -- greenlet 对其封装，从而使得切换任务变得更加简单
# 使用前需要先安装：在终端输入 python -m pip install greenlet
# 检查是否安装成功： 在终端输入 python -m pip list
# 卸载： 在终端输入 python -m pip uninstall greenlet
# **注意：greenlet属于手动切换，当遇到IO操作程序会阻塞，而不能进行自动切换

# 通过greeenlet实现任务的切换
# 导入模块：
from greenlet import greenlet
def sing():
    print("在唱歌")
    g2.switch()    # 跳到任务（g2）去执行
    print("唱完了")
def dance():
    print("在跳舞")
    print("跳完了")
    g1.switch()    # 跳到任务（g1）去执行 （从上次阻塞的地方开始）
if __name__ == "__main__":
    # 创建协程对象 greenlet(函数名)
    g1 = greenlet(sing)
    g2 = greenlet(dance)
    # 手动切换执行任务
    g1.switch()
# 执行上面代码打出：
# 在唱歌
# 在跳舞
# 跳完了
# 唱完了

# gevent：遇到IO操作时，会进行自动切换，属于主动式切换
# 相较greenlet更强大，而且能够自动切换任务
# 同样需要先安装： pip install gevent

# gevent模块的常用功能：
# 1. gevent.spawn(函数名)： 创建协程对象
# 2. gevent.sleep()：耗时操作
# 3. gevent.join()：阻塞，等待某个协程执行结束
# 4. gevent.joinall()：等待所有协程对象都执行结束后再退出，其参数是一个协程对象列表

# 导入模块：
import gevent
def sing():
    print("在唱歌")
    gevent.sleep(2)    # 等待两秒后再继续执行
    print("唱完了")
def dance():
    print("在跳舞")
    gevent.sleep(2)
    print("跳完了")
if __name__ == "__main__":
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)
    g1.join()
    # 上面的join语句其作用是：
    # 1. 阻塞当前主线程，等待g1协程执行完成
    # 2. 触发所有已创建的gevent协程开始执行（包括g1和g2）

def sing(name):
    for i in range(3):
        gevent.sleep(1)    # *注意：此处用到的是gevent里面的sleep而不是time里的sleep
        print(f"{name}在唱第{i}首歌")
if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(sing, "bingbing"),
        gevent.spawn(sing, "冰冰")
    ])
# 在上面的代码中若不加sleep，则会先执行“bingbing”任务，再执行“冰冰”任务
# 加上sleep后，则会同时执行两个任务

# monkey补丁：拥有在模块运行时替换的功能
# 导入模块：
from gevent import monkey
monkey.patch_all()    # 将下面用到的time.sleep()代码替换成gevent里面自己实现耗时操作的gevent.sleep()代码
# **注意：“monkey.patch_all()”这句代码必须放在被打补丁者（eg：time.sleep()）的前面
def sing(name):
    for i in range(3):
        time.sleep(1)
        print(f"{name}在唱第{i}首歌")
if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(sing, "bingbing"),
        gevent.spawn(sing, "冰冰")
    ])

# 总结：
# 1. 线程是CPU调度的基本单位，进程是资源分配的基本单位
# 2. 进程、线程和协程的对比
    # 进程：切换需要的资源最大，效率最低
    # 线程：切换需要的资源一般，效率一般
    # 协程：切换需要的资源最小，效率高
# 3. 多线程适合IO密集型操作（eg：文件操作、网络请求、网络爬虫），多进程适合CPU密集型操作（eg：科学计算、对视频进行高清解码）
# 4. 进程、线程、协程都是可以完成多任务的，可以根据自己的实际开发的需要选择使用


# 十二、正则基础

# 正则表达式
# 含义：记录文本规则的代码
# 优点：通用性很强，适用于多种编程语言
# 缺点：语法比较复杂，可读性较差
# 步骤：
#   1. 导入re模块
#   2. 使用match方法进行匹配操作（re.match()能匹配出以xxx开头的字符串，如果起始位置没有匹配成功，返回None）
#      re.match(pattern,string,flags) -- pattern：匹配的正则表达式；string：要匹配的字符串；flags：标志位（是否区分大小写、多行匹配等）（了解就行）
#   3. 如果上一步数据匹配成功，使用group()提取数据

import re
res = re.match("冰","冰冰永远18")
print(res)    # <re.Match object; span=(0, 1), match='冰'>
print(res.group())    # 冰  （*注意：若“冰”字不在开头则会报错，因为match是从开头位置匹配的，匹配不到就没有，且匹配的是表达式整体（即把要查找的字符串作为一个整体））

# 匹配单个字符：
# 1. . -- 匹配任意一个字符，除\n以外（常用）
res1 = re.match(".","hello")
print(res1.group())     # h
res2 = re.match("h.","hello")
print(res2.group())     # he

# 2. [] -- 匹配括号中列举的字符（注意：只匹配单个字符，即查看首字符是不是括号内的字符之一）（常用）
res1 = re.match("[he]","hello")
print(res1.group())      # h
res2 = re.match("[0-46-9]","2468")    # 可以用“-”来表示查找的范围，此处表示的范围是 0到4 和 6到9
print(res2.group())     # 2

# 3. \d -- 匹配数字0-9（常用）
res = re.match(r"[\d]","2468")    # 注意：建议加上取消转义符r
print(res.group())     # 2

# 4. \D -- 匹配非数字（常用）
res = re.match("[\D]","a468")
print(res.group())     # a

# 5. \s -- 匹配空白（即空格和Tab键）
res = re.match(".\s.","a b c")
print(res.group())    # a b

# 6. \S -- 匹配非空白
res = re.match("\S","abcd")
print(res.group())     # a

# 7. \w -- 匹配单词字符（即 a-z，A-Z，0-9，_，汉字）(常用）
res = re.match("\w\w\w\w\w","a_A0一")
print(res.group())    # a_A0一

# 8. \W -- 匹配非单词字符
res = re.match("\W\W\W",", .")
print(res.group())    # , .

# 匹配多个字符：
# 1. * -- 匹配前一个字符出现0次或无限次，即可有可无（常用）
res = re.match("\w*","bing,bing")
print(res.group())     # bing

# 2. + -- 匹配前一个字符出现1次或无限次，即至少出现一次（常用）
res = re.match("\d+","bing,bing")
print(res.group())     # 报错

# 3. ？ -- 匹配前一个字符出现1次或0次（常用）
res1 = re.match("\d?","123bing,bing")
print(res.group())    # 1
res2 = re.match("\s?","123bing,bing")
print(res2.group())    # 不报错

# 4. {m} -- 匹配前一个字符出现m次
res1 = re.match("\w{3}","123456789")
print(res1.group())    # 123
res2 = re.match("\w{3}","12,34,")
print(res2.group())    # 报错

# 5. {m,n} -- 匹配前一个字符出现m-n次
res1 = re.match("\w{3,5}","abcdefg")
print(res1.group())    # abcde
res2 = re.match("\w{3,5}","ab")
print(res2.group())    # 报错
res3 = re.match("\w{3,5}","abc，d")
print(res3.group())    # abc

# 匹配开头结尾：
# 1. ^ -- 匹配字符串开头（也可以表示取反，当放在[]内表示不匹配，即开头不是···）
res1 = re.match("^abc","abcde")
print(res1.group())    # abc
res2 = re.match("^123","1,2,3")
print(res2.group())    # 报错
res3 = re.match("[^123]","abc123")
print(res3.group())    # a
res4 = re.match("[^123]","123abc")
print(res4.group())    # 报错

# 2. $ -- 尝试从字符串的起始位置开始匹配，并以···结尾的模式
res1 = re.match("c$","123abc")
print(res1.group())    # 报错 （**注意：re.match() 要求匹配必须从字符串的第一个字符开始，而这里的匹配模式是从字符串末尾开始的，所以无法匹配成功）
res2 = re.match(".{5}c$","123abc")
print(res2.group())    # 123abc
res3 = re.match(".{3}a","123abd")
print(res3.group())    # 123a
res4 = re.match(".{3}a$","123abd")
print(res4.group())    # 报错


# 十三、正则进阶

# 匹配分组：
# 1. | -- 匹配左右任意一个字符串（常用）
res1 = re.match("123|abc","123")
print(res1.group())    # 123
res2 = re.match("123|abc","abc")
print(res2.group())    # abc

# 2. () -- 将括号中字符作为一个分组（常用）
res1 = re.match("\w*@(163|qq|126).com","123@163.com")
res2 = re.match("\w*@(163|qq|126).com","123@qq.com")
res3 = re.match("\w*@(163|qq|126).com","123@126.com")
print(res1.group())    # 123@163.com
print(res2.group())    # 123@qq.com
print(res3.group())    # 123@126.com

# 3. \num -- 匹配第num个分组匹配到的字符串（经常在匹配标签时使用）
res1 = re.match("<\w*>\w*</\w*>","<html>login</html>")
print(res1.group())    # <html>login</html>
# 由于html出现了两次，所以可以把第一个html作为一个分组，当需要再次匹配同一字符串时可以之间用“\num”来匹配（num是指第几个分组，不能随便写，从外到内排序，从1开始）
# **注意：必须使用取消转义字符（\\或加r），否则\num不会起作用
res2 = re.match(r"<(\w*)>\w*</\1>","<html>login</html>")
print(res2.group())    # <html>login</html>
res3 = re.match(r"(\w*),(\w*),\1,\2","abc,123,abc,123")
print(res3.group())    # abc,123,abc,123

# 4. (?P<name>) -- 给分组起别名
# 5. (?P=name) -- 引用别名为name分组匹配到的字符串
res = re.match("(?P<a>\w*),(?P<b>\w*),(?P=a),(?P=b)","abc,123,abc,123")
print(res.group())    # abc,123,abc,123

# 综合案例：
li = ["www.baidu.com","www.python.org","http.jd.com","www.py.cn","http.abc.en"]
for i in li:
    res = re.match(r"(www|http)(.)\w*\2(com|org|cn)",i)
    if res:
        print(res.group())
    else:
        print(f"{i}这个网址有错误")
# www.baidu.com
# www.python.org
# http.jd.com
# www.py.cn
# http.abc.en这个网址有错误

# 高级用法：
# 1. search() -- 扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败则返回None
res = re.search("py","123py456")
print(res.group())    # py

# 2. findall() -- 从头到尾匹配，找到所有匹配成功的对象，返回一个列表（*注意：打印时不需要group()）
res = re.findall("\d","abc123def")
print(res)    # ['1', '2', '3']

# 3. sub(pattern,repl,string,count) （注意：同样不需要group()来打印）
#   pattern  -- 正则表达式（代表需要被替换的，也就是字符串里的旧内容）
#   repl     -- 新内容
#   string   -- 字符串
#   count    -- 指定替换的次数（默认全部改掉）
res = re.sub("python","bingbing","hello python")
print(res)    # hello bingbing
res = re.sub("\d","0","123456789",5)
print(res)    # 000006789

# 4. split(pattern,string,maxsplit) （注意：同样不需要group()来打印）
#   pattern  -- 正则表达式
#   string   -- 字符串
#   maxsplit -- 指定最大分割次数（默认全分割）
res1 = re.split("，","hello，python，123，abc")
print(res1)    # ['hello', 'python', '123', 'abc']
res2 = re.split("，","hello，python，123，abc",2)
print(res2)    # ['hello', 'python', '123，abc']

# 贪婪与非贪婪
# 贪婪匹配：在满足匹配时，匹配尽可能长的字符串（默认情况下采用贪婪匹配）
# 非贪婪匹配：在满足匹配时，匹配尽可能短的字符串，使用?来表示非贪婪匹配
res1 = re.match("a*1*?","aaa111")
print(res1.group())    # aaa
res2 = re.match("\d{3,9}?","1234567890")
print(res2.group())    # 123

# 原生字符串：在Python里面在字符串前面加上r表示原生字符串
print("abcd\t1234")    # abcd	1234
print(r"abcd\t1234")   # abcd\t1234
res1 = re.match("\","\def")
print(res1.group())    # 报错
res2 = re.match("\\\\","\def")
print(res2.group())    # \
res3 = re.match(r"\\","\def")
print(res3.group())    # \
# *注意：正则表达式中，匹配字符串中的字符“\”需要“\\\\”（即四个斜杠匹配一个）或者加r后写“\\”（即两个斜杠匹配一个）


# 十四、内置模块

# os模块
# 作用：用于和操作系统进行交互

import os

# 1. os.name    --  指示正在使用的工作平台（返回操作系统类型：Windows返回nt，Linus返回posix）
print(os.name)      # nt

# 2. os.getenv()    --  读取环境变量（环境变量 —— 它存储着系统或应用程序运行时需要的关键信息（如路径、配置参数等），且所有软件（包括操作系统本身）都能随时读取这些信息，无需重复设置）
print(os.getenv("path"))

# 3. os.path.split()    --  把目录名和文件名分离，以元组的形式接受，第一个元素是目录路径，第二个元素是文件名
# 4. os.path.dirname()  --  显示split分割的第一个元素，即目录路径
# 5. os.path.basename() --  显示split分割的第二个元素，即文件名
print(os.path.split(r"/python/note.py"))      # ('D:\\PythonCode\\pynote1', 'note.py')
print(os.path.dirname(r"/python/note.py"))    # D:\PythonCode\pynote1
print(os.path.basename(r"/python/note.py"))   # note.py

# print(os.path.basename(r"D:\PythonCode\pynote1\"))
# **注意：上面一行代码会报错。如果路径以“/”结尾，就返回空值；如果路径以“\”结尾，则会报错

# 6. os.path.exists()   -- 判断路径（文件或目录）是否存在，存在的话就返回True，不存在就返回False
print(os.path.exists(r"/python/note.py"))     # True
print(os.path.exists(r"D:\PythonCode\pynote1\note.ja"))     # False

# 7. os.path.isfile()   -- 判断是否是文件
# 8. os.path.isdir()    -- 判断是否是目录
print(os.path.isfile(r"/python/note.py"))     # True
print(os.path.isfile(r"/"))             # False
print(os.path.isdir(r"/python/note.py"))      # Flase
print(os.path.isdir(r"/"))              # True

# 9. os.path.abspath()  -- 获取当前路径下的绝对路径
# 10. os.path.isabs()   -- 判断当前路径是否是绝对路径
print(os.path.abspath("note.py"))   # D:\PythonCode\pynote1\note.py
print(os.path.isabs(r"/python/note.py"))  # True

# sys模块
# 作用：负责程序跟Python解释器的交互

import sys

# 1. sys.getdefaultencoding()   -- 获取系统默认编码格式
print(sys.getdefaultencoding())     # utf-8

# 2. sys.path   -- 获取环境变量的路径，跟解释器有关
print(sys.path)     # 以列表的形式返回，第一项为当前所在的工作目录
# ['D:\\PythonCode\\pynote1', 'D:\\PythonCode\\pynote1', 'E:\\Python\\python37.zip', 'E:\\Python\\DLLs', 'E:\\Python\\lib', 'E:\\Python', 'E:\\Python\\lib\\site-packages', 'E:\\Python\\lib\\site-packages\\win32', 'E:\\Python\\lib\\site-packages\\win32\\lib', 'E:\\Python\\lib\\site-packages\\Pythonwin']
print(sys.path[0])  # D:\PythonCode\pynote1

# 3. sys.platform   -- 获取操作系统平台名称
print(sys.platform)     # win32

# 4. sys.version    -- 获取Python解释器的版本信息
print(sys.version)      # 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]

# time模块
# 三种时间表示
#   1. 时间戳（timestamp）
#   2. 格式化的时间字符串（format time）
#   3. 时间元组（struct_time）

import time

# 1. time.sleep()   -- 延时操作，以秒为单位
print("12")
time.sleep(2)
print("ab")

# 2. time.time()    -- 获取到当前的时间戳 —— 以秒为单位计算，从1970年1月1日的00:00:00开始到现在的时间差
print(time.time())  # 返回的是浮点型

# 3. time.localtime()   -- 将一个时间戳转换为当前时区的struct_time，包含九个元素（年、月、日、时、分、秒、周几、一年中的第几天、夏令时标志（0：不处于夏令时；1：处于夏令时；-1：不确定（默认值））
print(time.localtime())     # time.struct_time(tm_year=2025, tm_mon=10, tm_mday=31, tm_hour=11, tm_min=11, tm_sec=29, tm_wday=4, tm_yday=304, tm_isdst=0)

# 4. time.asctime() -- 获取系统当前时间，把struct_time换成固定的字符串表达式
print(time.asctime())   # Fri Oct 31 11:20:20 2025  （星期、月、日、时、分、秒、年）
t1 = time.localtime()
print(time.asctime(t1))  # Fri Oct 31 11:21:35 2025  （与上面的效果相同）
t2 = time.time()
print(time.asctime(t2)) # 报错，不能对时间戳使用

# 5. time.ctime()   -- 获取系统当前时间，把timestamp换成固定的字符串表达式
print(time.ctime())     # Fri Oct 31 11:25:13 2025
t = time.time()
print(time.ctime(t))    # Fri Oct 31 11:25:48 2025  （与上面的效果相同）

# 6. time.strftime()    -- 将struct_time转换成时间字符串（需要自己编写格式）
# 7. time.strptime()    -- 将时间字符串转换成struct_time（需要自己编写格式）
    # 时间字符串支持的格式符号
    #   1.  %a  --  本地星期名称的简写
    #   2.  %A  --  本地星期名称的全称
    #   3.  %b  --  本地月份名称的简写
    #   4.  %B  --  本地月份名称的全称
    #   5.  %c  --  本地相应的日期和时间的字符串表式（eg：15/08/27 10:20:06）
    #   6.  %d  --  一个月中的第几天（01-31）
    #   7.  %f  --  微妙（范围0.999999）
    #   8.  %H  --  一天中的第几个小时（00-23）
    #   9.  %I  --  第几个小时（01-12）
    #   10. %j  --  一年中的第几天（001-366）
    #   11. %m  --  月份（01-12）
    #   12. %M  --  分钟数（00-59）
    #   13. %p  --  本地am或pm的相应符号
    #   14. %S  --  秒（01-61）（闰年秒占两秒）
    #   15. %U  --  一年中的星期数（00-53）（星期日作为一个星期的开始，所以第一个周日之前的天放在第0周）
    #   16. %w  --  一个星期中的第几天（0-6）（0为周日）
    #   17. %W  --  和%U相同，不过将周一作为一周的开始
    #   18. %x  --  本地相应日期的字符串（eg：25/10/31）
    #   19. %X  --  本地相应时间的字符串（eg：11:49:36）
    #   20. %y  --  去掉世纪的年份（00-99）
    #   21. %Y  --  完整的年份（四位数）
    #   22. %z  --  与UTC时间的间隔（如果是本地时间则返回空字符串） （UTC —— 世界标准时间）
    #   23. %Z  --  时区的名字（如果是本地时间则返回空字符串）
    #   24. %%  --  “%”字符
        # 注意：
        # 1. %p 只有和 %I 配合使用才有效
        # 2. 当使用strptime()函数时，只有当在这年中的周数和天数被确定的时候 %U和%W 才会被计算
print(time.strftime("%Y-%m-%d",time.localtime()))   # 2025-10-31
print(time.strptime("2025/10/31","%Y/%m/%d"))       # time.struct_time(tm_year=2025, tm_mon=10, tm_mday=31, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=304, tm_isdst=-1)
# **注意：time.strptime括号里面的两个字符串隔开数字和格式的方法要一致（如上面靠“/”隔开）

# logging模块
# 作用：用于记录日志信息
# 日志的作用：
#   1. 程序调试
#   2. 了解软件程序运行情况是否正常
#   3. 软件程序运行故障分析与问题定位

import logging

# logging中的等级（由低到高）：
#   1. NOTSET           （0）     -- 不设置级别，按照父logger的级别显示日志，如果是root logger，那么就会显示所有的日志
#   2. DEBUG            （10）    -- 程序的详细调试信息，调试代码会用到
#   3. INFO             （20）    -- 普通信息，确定程序是否按照正常的运行
#   4. WARNING          （30）    -- 程序发出警告，表示发生意想不到的事情或指示接下来可能会出现一些问题，但是还能正常运行
#   5. ERROR            （40）    -- 程序发生错误，某些功能无法运行
#   6. CRITICAL/FATAL   （50）    -- 程序出现致命错误，无法运行

logging.debug("我是debug")
logging.info("我是info")
logging.warning("我是warning")
logging.error("我是error")
logging.critical("我是critical")
# WARNING:root:我是warning
# ERROR:root:我是error
# CRITICAL:root:我是critical
# **注意：logging默认的level就是warning，也就是说logging只会显示级别大于等于warning的日志信息

# logging.basicConfig() -- 配置root logger的参数
    #   1. filename：指定日志文件的文件名（所有会显示的日志都会存放到这个文件中去）
    #   2. filemode：文件的打开方式，默认为a —— 追加模式（文件操作）
    #   3. level：指定日志显示级别，默认是warning
    #   4. format：指定日志信息的输出格式
        # 常用的格式占位符（也称为日志记录属性）如下：
        #   1. 基本信息
            #   1. %(asctime)s：日志记录的时间，默认格式为 YYYY-MM-DD HH:MM:SS,mmm
            #   2. %(name)s：日志器（logger）的名称
            #   3. %(levelname)s：日志级别（如 DEBUG、INFO、WARNING 等）
            #   4. %(message)s：日志消息内容
        #   2. 位置信息
            #   1. %(filename)s：当前执行日志记录的文件名
            #   2. %(module)s：当前执行日志记录的模块名
            #   3. %(lineno)d：日志记录所在的行号
            #   4. %(pathname)s：当前执行日志记录的文件路径
        #   3. 进程 / 线程信息
            #   1. %(process)d：进程 ID
            #   2. %(processName)s：进程名称
            #   3. %(thread)d：线程 ID
            #   4. %(threadName)s：线程名称
        #   4. 其他
            #   1. %(funcName)s：执行日志记录的函数名
            #   2. %(created)f：日志记录创建的时间戳（Unix 时间）
            #   3. %(msecs)d：日志记录创建时间的毫秒部分
            #   4. %(relativeCreated)d：输出日志信息时，自当前 logger 实例创建以来所经过的毫秒数
logging.basicConfig(filename="log.log")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# 执行上面的代码会创建一个名为“log.log”的文件，里面会存放：
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical

logging.basicConfig(filename="log.log", filemode="a")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# 执行上面的代码，会在log.log文件中往下加入重复的内容

logging.basicConfig(filename="log.log", filemode="w", level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# 执行上面的代码会覆盖之前log.log文件里面的内容，写入：
# DEBUG:root:debug
# INFO:root:info
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical

logging.basicConfig(filename="log.log", filemode="w", format="%(levelname)s:%(asctime)s\t%(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# 执行上面的代码会按照格式（等级名称:具体时间\t信息）来打印：
# WARNING:2025-10-31 15:28:58,481	warning
# ERROR:2025-10-31 15:28:58,482	error
# CRITICAL:2025-10-31 15:28:58,482	critical

# random模块
# 作用：用于实现各种分布的伪随机数生成器，可以根据不同的实数分布来随机生成值

import random

#   1. random.random()  -- 产生大于0且小于1的小数
#   2. random.uniform() -- 产生指定范围的随机小数
#   3. random.randint() -- 产生指定范围内的随机整数（*注意：包括开头和结尾）
#   4. random.randrange(start,stop,step)  -- 产生从start到stop范围内的随机整数（*注意：包含开头，不包含结尾），step —— 步长（从start开始只能取满足步长的整数）
print(random.uniform(3,6))  # 产生3到6的随机小数
print(random.randrange(1,10,3))   # 只能产生：1、4、7

# json模块
# 作用：在 Python 对象和 JSON 字符串之间进行相互转换
# 应用场景：数据存储、网络传输、API 响应 或 读取配置文件、处理 API 请求、解析数据

import json



# requests模块


# 十五、Linux基本命令

# 关机、重启命令：
#   1. poweroff -- 立即关机
#   2. shutdown -h now   -- 立即关机，now也可以换成数字（以分钟为单位）或者具体时间
#   3. reboot   -- 立即重启
#   4. shutdown -r now   -- 立即重启，now也可以换成数字（以分钟为单位）或者具体时间

# 目录操作命令：
# cd    -- 目录切换
    #   1. cd /     -- 切换到根目录
    #   2. cd /usr  -- 切换到根目录下的usr目录
    #   3. cd ..    -- 切换到上一级目录
    #   4. cd ~     -- 切换到home目录
    #   5. cd -     -- 切换到上次访问的目录
# ls    -- 目录查看
    #   1. ls       -- 查看当前目录下的所有内容（不同的颜色代表不同的权限）
    #   2. ls -a    -- 查看当前目录下的所有目录和文件（包括隐藏的文件）
    #   3. ls -l    -- 列表查看当前目录下的所有目录和文件（列表查看显示更多信息）
    #   4. ls /文件名或目录名  -- 查看指定目录下的所有目录和文件
    #   5. dir      -- 查看当前路径下的所有文件（不变色）
# mkdir -- 创建目录
    #   1. mkdir 目录名         -- 在当前目录下创建一个目录
    #   2. mkdir /路径/目录名    -- 在指定目录下创建一个目录
# rm    -- 删除目录或文件
    #   1. rm 文件名       -- 删除当前目录下的文件
    #   2. rm -f 文件名    -- 删除当前目录下的文件（不询问）
    #   3. rm -r 目录名    -- 递归删除当前目录下的目录
    #   4. rm -rf 目录名   -- 递归删除当前目录下的目录（不询问）
    #   5. rm -rf*        -- 将当前目录下的所有目录和文件全部删除
    #   6. rm -rf/*       -- 将根目录下的所有文件全部删除（**注意：自杀式命令，慎重使用）
# mv和cp -- 目录修改
    #   1. mv 当前目录 新目录              -- 重命名目录
    #   2. mv 目录名称 目录的新位置         -- 剪切目录
    #   3. cp -r 目录名称 目录拷贝的目标位置 -- 拷贝目录
# find  -- 目录搜索
    #   1. find 目录 参数 文件名称  -- 搜索目录

# 文件操作命令：
# touch 文件名     -- 新建文件
# rm -rf 文件名    -- 删除文件
# vi/vim 文件名    -- 修改文件
    # vi编辑器的三种模式：
    # 1. 命令行模式（command mode）    -- 控制屏幕光标的移动；字、行的删除；查找字符串；复制粘贴
        # 光标移动操作：
        #   1. 上下左右方向键/k、j、h、l  -- 向上下移动一行或者向左右移动一个字符
        #   2. w    -- 跳到下一个单词的开头
        #   3. b    -- 跳到上一个单词的开头
        #   4. 0    -- 跳到当前行的开头（行首）
        #   5. $    -- 跳到当前行的末尾（行尾）
        #   6. gg   -- 跳到文件第一行
        #   7. G    -- 跳到文件最后一行
        #   8. nG   -- 跳到第 n 行（n 为数字）
        # 文本删除操作：
        #   1. x    -- 删除光标所在位置的单个字符
        #   2. nx   -- 删除光标后 n 个字符
        #   3. dd   -- 删除当前行（剪切行，可粘贴）
        #   4. ndd  -- 从当前行开始，删除 n 行
        #   5. d0   -- 删除从光标位置到行首的内容
        #   6. d$   -- 删除从光标位置到行尾的内容
        # 复制粘贴操作：
        #   1. yy   -- 复制当前行
        #   2. nyy  -- 从当前行开始，复制 n 行
        #   3. p    -- 在光标所在行的下方粘贴复制 / 剪切的内容
        #   4. P    -- 在光标所在行的上方粘贴复制 / 剪切的内容
        # 撤销/重做操作：
        #   1. u        -- 撤销上一步操作
        #   2. Ctrl + r -- 重做（恢复被撤销的操作）
        # 模式切换操作：
        #   1. i / a / o / s等   -- 进入编辑模式（具体见编辑模式说明）
        #   2. :    -- 进入底行模式
        # 其他操作：
        #   1. r + 字符   -- 替换光标所在位置的单个字符（输入 r 后按新字符，直接替换）
        #   2. ZZ   -- 快速保存并退出（等效于底行模式的 :wq）
    # 2. 编辑模式（insert mode）      -- 只有在insert模式下才能对文字进行修改和编辑（按ESC返回命令行模式）
        # 进入方式：
        #   1. i    -- 在光标当前位置前插入文本（最常用）
        #   2. a    -- 在光标当前位置后插入文本
        #   3. o    -- 在光标所在行的下方新建一行，并在新行插入文本
        #   4. O    -- 在光标所在行的上方新建一行，并在新行插入文本
        #   5. I    -- 跳到当前行的开头并插入文本（忽略行首空格）
        #   6. A    -- 跳到当前行的末尾并插入文本
        #   7. s    -- 删除光标所在字符并进入插入模式
        #   8. S    -- 删除当前行并进入插入模式
        # 编辑中的操作：
        #   1.可直接使用方向键移动光标（部分环境支持，不支持时需按 Esc 退回命令模式移动）
        #   2.按 Backspace 或 Delete 删除字符
        #   3.完成编辑后，按 Esc 退回命令模式
    # 3. 底行模式（last line mode）   -- 将文件进行保存和退出；设置编辑环境（用“:”进入底行模式）
        # 文件操作：
        #   1. :q       -- 退出编辑
        #   2. :q!      -- 强制退出
        #   3. :wq/:x   -- 保存并退出
        #   4. :w       -- 保存当前文件
        #   5. :w 文件名 -- 将当前内容另存为指定文件（如 :w new.txt）
        #   6. :w!      -- 强制保存（忽略文件只读属性，需有权限）
        #   7. :e 文件名 -- 打开指定文件编辑（当前文件未保存时需加 ! 强制打开，如 :e! test.txt）
        #   8. :e!      -- 放弃当前修改，重新加载文件原始内容
        # 搜索替换：
        #   1. :/关键词    -- 从当前位置向下搜索 “关键词”，按 n 找下一个，N 找上一个
        #   2. :?关键词    -- 从当前位置向上搜索 “关键词”，按 n 找上一个，N 找下一个
        #   3. :%s/旧内容/新内容/g    -- 全局替换所有 “旧内容” 为 “新内容”（% 表示所有行，g 表示一行内全部替换）
        #   4. :n1,n2s/旧内容/新内容/c    -- 替换第 n1 到 n2 行的 “旧内容”，每次替换前询问确认（c 为确认选项）
        # 显示设置：
        #   1. :set nu / :set number        -- 显示行号
        #   2. :set nonu / :set nonumber    -- 隐藏行号
        #   3. :set hlsearch    -- 开启搜索高亮（默认开启）
        #   4. :set nohlsearch  -- 关闭搜索高亮
        #   5. :noh             -- 取消当前搜索结果的高亮（临时生效）
        # 行跳转：
        #   1. :n   -- 跳转到第 n 行
        #   2. :$   -- 跳转到文件最后一行
        # 其他：
        #   1. :!系统命令   -- 临时执行系统命令（如 :!ls 查看目录文件，按 Enter 返回 vi）
        #   2. :r 文件名   -- 在当前行下方插入指定文件的内容（如 :r data.txt）
        #   3. :r !系统命令 -- 在当前行下方插入系统命令的输出（如 :r !date 插入当前时间）
# cat 文件名   -- 查看文件最后一屏
# more 文件名  -- 百分比显示
# less 文件名  -- 翻页查看文件内容
# tail 文件名  -- 指定行数或者动态查看文件内容

# 压缩文件操作命令：
# 1. 压缩：tar -zcvf 打包压缩后的文件名 要打包的文件
# 2. 解压：tar -zxvf 压缩文件
# **注意：
# Windows的压缩文件的扩展名：.zip/.rar
# Linux中的打包文件：aa.tar
# Linux中的压缩文件：bb.gz
# Linux中打包并压缩的文件：.tar.gz

# 其他常用命令：
#   1. pwd      -- 查看当前目录
#   2. ps -ef   -- 查看所有正在运行的进程
#   3. clear    -- 清空终端屏幕命令
#   4. Ctrl + L -- 清屏
#   5. su - 用户名 -- 切换用户
#   6. tab      -- 自动补全





















#    目录    #
#             *语法基础*
# ···
# 五、注释                        （30）
# 六、输出函数(print)              （42）
# 七、变量                        （52）
# 八、标识符                      （70）
# 九、数值类型                     （88）
# 十、字符串                      （102）
# 十一、格式化输出                 （112）
# 十二、运算符                    （155）
# 十三、输入函数(input)           （183）
# 十四、转义字符( \ )             （190）
# 十五、if判断语句                （201）
# 十六、循环语句                  （240）
# 十七、字符串                    （276）
# 十八、列表                     （414）
# 十九、元组                     （499）
# 二十、字典                     （516）
# 二十一、集合(set)              （587）
# 二十二、类型转换                （626）
# 二十三、深浅拷贝                （701）
# 二十四、函数基础                （781）
# 二十五、函数进阶                （843）
#       1.作用域                （845）
#       2.匿名函数              （892）
#       3.内置函数              （916）
#       4.拆包                 （976）
# 二十六、异常(即bug)            （995）
# 二十七、模块                  （1068）
# 二十八、包                    （1097）
# 二十九、递归函数               （1108）
# 三十、闭包&装饰器              （1137）
#             *语法进阶*
# 一、面向对象基础               （1268）
#       1.类和对象              （1274）
#       2.构造函数              （1316）
#       3.析构函数              （1331）
# 二、封装                      （1352）
# 三、继承                      （1404）
# 四、多态                      （1504）
# 五、单例模式                   （1603）
# 六、魔法（魔术）方法&属性        （1675）
# 七、文件                      （1699）
#       1.文件读写              （1703）
#       2.访问模式              （1761）
#           文件定位操作         （1790）
#       3.编码格式              （1809）
#       4.目录常用操作           （1828）
# 八、迭代器&生成器              （1841）
# 九、线程                      （1942）
# 十、进程                      （2114）
# 十一、协程                    （2302）
# 十二、正则基础                 （2433）
# 十三、正则进阶                 （2538）
# 十四、内置模块                 （2632）
#       1. os模块              （2634）
#       2. sys模块             （2674）
#       3. time模块            （2696）
#       4. logging模块         （2755）
#       5. random模块          （2851）
#       6. json模块            （2863）
#       7. requests模块        （）
# 十五、Linux基本命令            （）
#              练习题目
#              网络爬虫
# 一、爬虫基本介绍               （）
# 二、requests库基本使用         （）
# 三、requests发送post请求       （）