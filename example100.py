#!/usr/bin/python
# -*- coding: UTF-8 -*-
import copy
import time

# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引


class SortClass:

    number = 0

    def partition(self, arr, low, high):
        i = (low-1)         # 最小元素索引
        pivot = arr[high]  # 取枢纽为最右侧数

        for j in range(low, high):  # j用来从左到右遍历数组
            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                i = i+1  # 将指针向右移一位
                '''
                让指针指向已排序的元素最右位置（下一个位置就大于pivot）
                此处两种情况：
                1.如果当前遍历元素小于等于pivot----> i==j 交换元素不产生变化--->下一次循环j+1
                2.如果中间出现大于pivot的元素，i未进入if不右移---> i不变 j+1（相对于i的位置向后移动n(出现大于pivot元素的次数)位）
                  下次循环元素如果小于pivot---->i+1之后指向大于pivot的元素，此时交换当前遍历元素(小于pivot)和大于pivot的元素
                  保证指针永远指向已排序数列的最右侧位置
                '''
                arr[i], arr[j] = arr[j], arr[i]
        '''
        一趟循环完成小于pivot的数据都在左侧
        指针指向已排序数据最右
        交换pivot和已排序最右+1大于pivot的元素
        '''
        arr[i+1], arr[high] = arr[high], arr[i+1]
        # 指向交换完成的最右
        return (i+1)

    # 快速排序函数（单项划分）
    def quickSort(self, arr, low, high):
        if low < high:

            pi = self.partition(arr, low, high)
            # 一趟循环完成小于pivot的数据都在左侧
            # 根据pi位置将原数组分割成两个数组
            # 分别递归进行下一次分割
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
        self.number += 1
        print('循环了:{:d}次'.format(self.number))


class Example:
    '100例练习'

    # 实例1
    """
    题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
    """

    def ex1(self):
        # 三位数 循环3次
        for i in range(1, 5):
            for j in range(1, 5):
                for k in range(1, 5):
                    if(i != k) and (i != j) and (j != k):  # 互不相同
                        print(i, j, k)

    # 实例2
    """
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
    程序分析：请利用数轴来分界，定位。
    """

    def ex2(self):
        i = int(input('净利润:'))
        money = [1000000, 600000, 400000, 200000, 100000, 0]
        rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
        result = 0
        for idx in range(0, len(money)):
            # 由高到底比较输入金额位于那一个档
            if i > money[idx]:
                # 由高到低档依次计算，累加结果
                result += (i-money[idx])*rate[idx]
                # 当前金额计算完成，将下一级要计算的等级金额赋值给计算值i
                i = money[idx]
            pass
        print(result)

    # 实例4
    """
    题目：输入某年某月某日，判断这一天是这一年的第几天？
    程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
    """

    def ex4(self):
        # 考察闰年
        year = int(input('year:\n'))
        month = int(input('month:\n'))
        day = int(input('day:\n'))
        # 每月天数
        mdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        sum = 0
        if 0 < month <= 12:
            # month-1 计算当前月份前共有多少天
            for mindex in range(0, month-1):
                sum += mdays[mindex]
        else:
            print('data error')
        # 加上输入的天数
        sum += day
        leap = 0
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):  # 是否闰年
            leap = 1
        if (leap == 1) and (month > 2):  # 闰年并且月份大于2
            sum += 1
        print('it is the %dth day.' % sum)

    # 实例5
    """
    题目：输入三个整数x,y,z，请把这三个数由小到大输出。
    程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
    """

    def ex5(self):
        l = [5, 1, 9, 3, 8, 4, 7]
        # for i in range(7):
        #     x = int(input('integer:\n'))
        #     l.append(x)  # 将三个数放入数组
       # l.sort() #数组排序
        SortClass().quickSort(l, 0, (len(l)-1))
        print(l)

    # 实例6
    """
    题目：斐波那契数列(面试老问这个)
    程序分析：0,1,1,2,3,5,8,13,21,34 后边等于前两个数之和
    """

    def ex6(self, n):  # n第几位斐波那契数列
        if n == 1 or n == 2:
            return 1
        # 此处是递归函数，就是自己调用自己，但是一般这么使用必须要有停止条件，不然会无限制执行
        return (self.ex6(n-1)+self.ex6(n-2))
        # 上班的if语句就是这个递归函数的停止条件，依次向前计算，计算到1or2时停止

    # 实例7
    """
    题目：将一个列表的数据复制到另一个列表中。
    程序分析：使用切片、构造函数、copy、*运算符
    """

    def ex7(self):
        a = [1, 2, 3]
        # 切片运算，通过调用a[:]，我们得到一个从列表首端开始到末端的切片，也就是a（指引的列表）的完整复制。但这不是复制列表的唯一方式。看看下面这集中情况的复制：
        b = a[:]
        c = list(a)  # list是列表构造函数
        d = a * 1
        e = copy.copy(a)
        # 如果有子列表上述 b/c/d/e 复制的子列表都指向同一对象！！！
        f = copy.deepcopy(a)  # 对于二维甚至更多维数组，deepcopy是最安全的方法，不管多少层，新列表都是深拷贝
        print(id(a), a)
        print(id(b), b)
        print(id(c), c)
        print(id(d), d)
        print(id(e), e)
        print(id(f), f)

    # 实例8
    """
    题目：输出 9*9 乘法口诀表。
    程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
    """

    def ex8(self):
        for i in range(1, 10):
            print() #控制行，换行
            for j in range(1, i+1):# 控制列,打印从行开始，第一行1列 第2行两列 …… 所以i+1
                print("{:d}*{:d}={:d}".format(j, i, i*j),end="\t")

    # 实例9
    """
    题目：暂停一秒输出。
    程序分析：使用 time 模块的 sleep() 函数。
    """
    def ex9(self):
        myD = {'你': '啊', '最': '腻','棒':'加','了':'油'}
        for key, value in dict.items(myD):
            print (key, value)
            time.sleep(1) # 暂停 1 秒


    # 实例10
    """
    题目：暂停一秒输出，并格式化当前时间。
    程序分析：使用 time 模块的 sleep() 函数。
    """
    def ex10(self):
        # strfrtime用法
        # time.strftime(format[,t])
        # t --- 可选的参数t是一个struct_time对象。
        # fromat --- 日期时间格式化字符串
        """
        指令：
            %a - 简写的星期几
            %A - 完整的星期几
            %b - 缩写的月份名称
            %B - 完整的月份名称
            %c - 首选日期和时间表示
            %C - 世纪值（年份除以100，范围从00到99）
            %d - 该月的第几天（01?31）
            %D - 类似 %m/%d/%y
            %e - 该月的一天（1?31）
            %g - 类似于%G，但是没有世纪
            %G - 对应于ISO周数4位数的年份（参见％V）
            %h - 类似于 %b
            %H - 小时，使用24小时制（00?23）
            %I - 小时，使用12小时制（01?12）
            %j - 一年中的哪一天（001?366）
            %m - 月份（01?12）
            %M - 分钟
            %n - 换行符
            %p - 根据给定的时间值am或pm
            %r - 时间在上午和下午的符号：am/pm
            %R - time in 24 hour notation
            %S - 秒
            %t - 制表符
            %T - 当前时间，等于 %H:%M:%S
            %u - 工作日为数字（1到7），星期一= 1。警告：在Sun Solaris上周日=1
            %U - 当年的周数，第一个星期日作为第一周的第一天
            %V - 本年度ISO 8601的周数（01到53），其中，第1周是在本年度至少4天的第一个星期，星期一作为一周的第一天
            %W - 当年的周数，与第一个星期一作为第一周的第一天
            %w - 星期为一个小数，星期日=0
            %x - 没有时间的日期表示
            %X - 无日期首选的时间表示
            %y - 一年无世纪（范围从00到99）
            %Y - 今年，包括世纪
            %Z or %z - 时区或名称或缩写
            %% -文字％字符
        """
        print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        
        # time.localtime--->struct_time
        # 格式化时间戳为本地时间

        # time.time
        # 获取时间戳

        # 暂停一秒
        time.sleep(1)

        print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    # 实例11
    """
    题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
    月份          兔子数                  说明

      1      1（对）            从开始有一对兔子

      2      1

      3      1+1       原本有一对  从第三个月开始 生了一对 一共是两对兔子

      4      1+1+1      生了第二对

      5      1+1+1+1+1   生了第三对兔子   同时3月生的第一对兔子又生了一对

      6      5+3=8

      兔子数目序列： 1 1 2 3 5 8 同上斐波那契数列
    """
    def ex11(self):
        month = 10
        sum = self.ex6(month) #第10个月兔子数，调用已写好的斐波那契数列方法
        print("{m}月共有{count}只兔子".format(m = month, count = sum*2)) #多少只？ 对*2


    # 实例12
    """
    题目：判断101-200之间有多少个素数，并输出所有素数。
    程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
    """
    def ex12(self):
        h = 0
        leap = 1
        from math import sqrt
        for m in range(101,201):
            k = int(sqrt(m + 1)) #平方根函数 如果 m 不能被 2 ~ m开平方 间任一整数整除，m 必定是素数。
            for i in range(2,k + 1):
                if m % i == 0:
                    leap = 0
                    break
            if leap == 1: #不能整除的为素数
                print ('%-4d' % m)
                h += 1  # 计算素数个数
                if h % 10 == 0:
                    print ('') #每10位输出一个换行
            leap = 1 # 还原标志位
        print ('The total is %d' % h)
e = Example()
# print(e.ex6(10))
e.ex12()
