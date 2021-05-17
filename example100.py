#!/usr/bin/python
# -*- coding: UTF-8 -*-

# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

class SortClass:

    number = 0
    
    def partition(self, arr, low, high):
        i = (low-1)         # 最小元素索引
        pivot = arr[high]  # 取枢纽为最右侧数

        for j in range(low, high): #j用来从左到右遍历数组
            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                i = i+1 #将指针向右移一位
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
            #一趟循环完成小于pivot的数据都在左侧
            #根据pi位置将原数组分割成两个数组
            #分别递归进行下一次分割
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
        l = [5,1,9,3,8,4,7]
        # for i in range(7):
        #     x = int(input('integer:\n'))
        #     l.append(x)  # 将三个数放入数组
       # l.sort() #数组排序
        SortClass().quickSort(l, 0, (len(l)-1))
        print(l)





e = Example()
e.ex5()