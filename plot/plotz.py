# -*- coding: UTF-8 -*-

#カメラに近いほどZ値の精度を上げるための計算式と通常の計算を比較
#直線
#	カメラとの距離に関係なくZ値は均等
#	遠くて良く見えないものにも、近くと同じレンジでZ値が割当たる
#点線
#	遠くて良く見えないものはZ値が変化しない
#	近い方はZ値の精度が上がる

import numpy as np
import matplotlib.pyplot as plt

def normalizeZ(z, near, far):
	return (z - near)/(far - near)

def normalizeZ2(z, near, far):
	return (far/z)*(z - near)/(far - near)

far = 1000.0
near = 10

z = np.arange(near, far, 10)
y = normalizeZ(z, near, far)
y2 = normalizeZ2(z, near, far)

plt.xlabel("Z")
plt.ylabel("Depth")
plt.plot(z, y)
plt.plot(z, y2, linestyle="--")	#「-」「--」「:」「-.」
plt.show()
