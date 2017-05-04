#coding: UTF-8

#	リストの計算
#	…ができるものと思っていたが、実際は numpy の arange の戻り値が対応しているだけだった

#	list と numpy.arange の結果の違いは以下の通り

import numpy as np

n = [1,2,3,4,5]
a = n * 2
print(type(n))	#<class 'list'>
print(a)		#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

m = np.arange(1,6,1)
b = m * 2
print(type(m))	#<class 'numpy.ndarray'>
print(b)		#[ 2  4  6  8 10]

