from functools import reduce
from operator import add

#分解する
#1の数を足算する
#出力する
print(reduce(add, map(int, list(input()))))

