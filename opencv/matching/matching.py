import numpy as np
import cv2

def matchWithTemplate():
	image = cv2.imread('../images/IMG_1402_1024.jpg')
	templ = cv2.imread('../images/template_start.png', cv2.IMREAD_GRAYSCALE)
	#templ = cv2.imread('../images/template_data.png', cv2.IMREAD_GRAYSCALE)	#	複数箇所の認識確認用
	w,h = templ.shape[::-1]

	result_image = image.copy()
	#	マッチングに使う画像は8bitか32bit浮動小数のグレースケールなので変換(結果表示に使うので、元画像はカラーで読み込んでいる)
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#res = cv2.matchTemplate(image_gray, templ, cv2.TM_SQDIFF )
	res = cv2.matchTemplate(image_gray, templ, cv2.TM_CCOEFF_NORMED )

	min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
	top_left = min_loc  #	TM_SQDIFF/TM_SQDIFF_NORMEDの時はこっち
	#top_left = max_loc
	bottom_right = (top_left[0]+w-1, top_left[1]+h-1)
	#cv2.rectangle(result_image, top_left, bottom_right, (0,0,255), 2)

	threshold = 0.85
	loc = np.where(res>=threshold)
	for pt in zip(*loc[::-1]):
		cv2.rectangle(result_image, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)

	cv2.imshow('Result', result_image)

	while True:
		ch = 0xFF & cv2.waitKey(0)
		if ch == 27:
			break

matchWithTemplate()

