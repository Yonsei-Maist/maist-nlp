"""
test for all nlp
"""

from ko.lib.spelling import HanJaMo

han = HanJaMo()
ex = [
	"반가스빈다.",
	"만나서 반가워요!!"
]

for item in ex:
	res = han.divide(item)
	print(res)
	res = han.union(res)
	print(res)
