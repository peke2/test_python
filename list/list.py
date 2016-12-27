#coding: UTF-8

a = ["a","b","c","d","e"]

print(a)		#	内容を全部出力
print(a[0])		#	内容の一部を出力

#	部分的に取り出す
print(a[2:4])	#	['c', 'd']
print(a[2:])	#	['c', 'd', 'e']
print(a[:-1])	#	['a', 'b', 'c', 'd']

#	スキップ
print(a[::2])		#	['a', 'c', 'e']

#	逆順
print(a[::-1])		#	['e', 'd', 'c', 'b', 'a']
print(a[3:1:-1])	#	['d', 'c']

