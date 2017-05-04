# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math

def plotExp(n):
	b = []
	#	通常の関数に渡す引数は1つずつ
	#	numpyだとまとめて処理できる
	for a in n :
		b.append( math.exp(a) )
	return	b

#	シグモイド関数
#	元は、この関数が描くグラフを確かめたかっただけ
def sigmoid(n):
	b = []
	for a in n :
		b.append( 1/(1+math.exp(-a)) )
	return	b

n = np.arange(0, 11, 0.2)
#a = plotExp(n)
#plt.plot(n,a)
a = sigmoid(n)
plt.plot(n,a)

#plt.plot(n, np.exp(n))
#plt.semilogy(n, np.exp(n))	#	Y軸のみを対数表記
plt.legend()
plt.show()

# [参考元]
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.loglog

