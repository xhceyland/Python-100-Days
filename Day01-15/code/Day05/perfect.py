"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):#求开方+1，则保证了至少一半的因子会被遍历到
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:#这里的！=是为了避免重复计算两次因子，例如36//6=6
                result += num // factor#这里将结果加入result计算相加，类似前一步48开方遍历到2，则计算出48//2=24，24加入计算
    if result == num:
        print(num)
