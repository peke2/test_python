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

def calcProjectionDepthZ(z, n, f):
	return (z*-(n+f)+(-2*n*f))/(f-n) /(-z)	#OpenGLでの投影マトリクスの計算によるもの(near～far → -1～1)

def calcProjectionDepthZ2(z, near, far):
	return (z*far-near*far)/(far-near) / z	#左手系だけど、near～far が 0.0～1.0 に変換される

def calcZFromDepth(zn, n, f):
	return 2*f*n/(zn*(f-n)-(f+n))



#far = 1000.0
#near = 10
#step = 10
far = 100.0
near = 0.3
step = 1

#z = np.arange(near, far, step)
#y = calcDepthZ(z, near, far)
#y2 = calcDepthZ2(z, near, far)

#z = np.arange(-near, -far, -step)			#右手系なので、Z座標は奥がマイナス
#y3 = calcProjectionDepthZ(z, near, far)		#クリップ面は「カメラからの距離」なので、常にプラスで指定
#z = np.arange(near, far, step)
#y3 = calcProjectionDepthZ2(z, near, far)

#	arange(start, stop, step) [start,stop) stopは含まれない
#	stop近くの変化が大きいので1つ手前の0.98だとfarの-100まで届かないのでグラフがおかしく見える
#	計算結果は正しいのだが、見栄えを良くするためstopの「1」も確実に含まれるようにしておく
z = np.arange(-1, 1.02, 0.02)
y4 = calcZFromDepth(z, near, far)


#plt.xlabel("Z")
#plt.ylabel("Depth")
#plt.plot(z, y, label="(z - near)/(far - near)")
#plt.plot(z, y2, linestyle="--", label="(far/z)*(z - near)/(far - near)")	#「-」「--」「:」「-.」
#plt.plot(z, y3, linestyle="--", label="Projection")	#「-」「--」「:」「-.」
plt.xlabel("Depth")
plt.ylabel("Z")
plt.plot(z, y4, linestyle="--", label="Depth")	#「-」「--」「:」「-.」
plt.legend();

plt.show()
