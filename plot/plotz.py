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

def calcDepthZ(z, near, far):
	return (z - near)/(far - near)

def calcDepthZ2(z, near, far):
	return (far/z)*(z - near)/(far - near)

def calcProjectionDepthZ(z, near, far):
	return (-z*(near + far) + (-2*near*far))/(far - near) / (-z)	#投影マトリクスの計算によるもの

#far = 1000.0
#near = 10
far = 100.0
near = 0.3

#z = np.arange(near, far, 10)
#y = calcDepthZ(z, near, far)
#y2 = calcDepthZ2(z, near, far)

z = np.arange(-near, -far, -10)
y3 = calcProjectionDepthZ(z, near, far)

plt.xlabel("Z")
plt.ylabel("Depth")
#plt.plot(z, y, label="(z - near)/(far - near)")
#plt.plot(z, y2, linestyle="--", label="(far/z)*(z - near)/(far - near)")	#「-」「--」「:」「-.」
plt.plot(z, y3, linestyle="--", label="Projection")	#「-」「--」「:」「-.」
plt.legend();

plt.show()
