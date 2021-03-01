import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    count = 0
    final_array = []
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
        final_array = a
    print('Array is sorted in', count, 'swaps.')
    first = final_array[0]
    last = final_array[-1]
    print('First Element:', str(first))
    print('Last Element:', str(last))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
