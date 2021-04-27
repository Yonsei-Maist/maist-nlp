"""
Library for Hangul Jaum Moum
@author Chanwoo Gwon, Yonsei Univ. Researcher, since 2020.05.~
@Date 2021.04.27
"""
import re


class HanJaMo:
	"""
	this class will help to divide or union Hangul's Jaum, Moum
	ex) 가나다 -> ㄱㅏㄴㅏㄷㅏ, ㅌㅏㅍㅏㅎㅏ -> 타파하
	idea from https://github.com/neotune/python-korean-handler
	"""

	CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
	JONGSUNG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
	                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
	BASE_MO = ord('ㅏ')
	BASE_JA = ord('ㄱ')
	END_MO = ord('ㅣ')
	BASE_CODE = ord('가')

	def divide(self, content):
		"""
		초성 = ((X - 0xAC00) / 28) / 21
		중성 = ((X - 0xAC00) / 28) % 21
		종성 = (X - 0xAC00) % 28
		:param content:
		:return:
		"""
		keyword_list = list(content)
		sentence = ""
		for keyword in keyword_list:
			if re.match('[가-힣]', keyword) is not None:
				keyword = ord(keyword)
				cho = HanJaMo.CHOSUNG_LIST[int((keyword - HanJaMo.BASE_CODE) / 28 / 21)]
				jung = chr(int((keyword - HanJaMo.BASE_CODE) / 28 % 21) + HanJaMo.BASE_MO)
				jong = HanJaMo.JONGSUNG_LIST[int((keyword - HanJaMo.BASE_CODE) % 28)]

				sentence = "{0}{1}{2}{3}".format(sentence, cho, jung, jong)
			else:
				sentence = "{0}{1}".format(sentence, keyword)

		return sentence

	def union(self, sequence):
		"""
		한글코드의 값 = ((초성 * 21) + 중성) * 28 + 종성 + 0xAC00
		:param sequence:
		:return:
		"""
		sentence = ""
		keyword_list = list(sequence)
		keyword_dict = {
			'cho': None,
			'jung': None,
			'jong': None,
			'edit': False
		}

		def make_other(other_word):
			return "{0}{1}".format(sentence, other_word)

		def make_keyword():
			cho = HanJaMo.CHOSUNG_LIST.index(keyword_dict['cho'])

			if keyword_dict['jung'] is None:
				keyword = ord(keyword_dict['cho'])
			else:
				jung = ord(keyword_dict['jung']) - HanJaMo.BASE_MO
				jong = HanJaMo.JONGSUNG_LIST.index(keyword_dict['jong']) if keyword_dict['jong'] is not None else 0

				keyword = ((cho * 21) + jung) * 28 + jong + HanJaMo.BASE_CODE

			keyword_dict['cho'] = None
			keyword_dict['jung'] = None
			keyword_dict['jong'] = None
			keyword_dict['edit'] = False

			return "{0}{1}".format(sentence, chr(keyword))

		for keyword in keyword_list:
			if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
				if keyword_dict['edit']:
					if keyword in HanJaMo.JONGSUNG_LIST:
						# keyword can be jongsung
						# and some can be chosung
						if keyword_dict['jung'] is not None and keyword_dict['jong'] is None:
							keyword_dict['jong'] = keyword
						else:
							sentence = make_keyword()

							if keyword in HanJaMo.CHOSUNG_LIST:
								keyword_dict['cho'] = keyword
								keyword_dict['edit'] = True
							else:
								sentence = make_other(keyword)

					elif keyword in HanJaMo.CHOSUNG_LIST:
						# keyword can be chosung but not jongsung
						sentence = make_keyword()

						keyword_dict['cho'] = keyword
						keyword_dict['edit'] = True
					elif ord(keyword) >= HanJaMo.BASE_MO or ord(keyword) <= HanJaMo.END_MO:
						# keyword can be jungsung
						if keyword_dict['jung'] is not None:
							if keyword_dict['jong'] is not None and keyword_dict['jong'] in HanJaMo.CHOSUNG_LIST:
								temp = keyword_dict['jong']
								keyword_dict['jong'] = None
								sentence = make_keyword()
								keyword_dict['cho'] = temp
								keyword_dict['jung'] = keyword
								keyword_dict['edit'] = True
							else:
								sentence = make_keyword()
								sentence = make_other(keyword)
						else:
							keyword_dict['jung'] = keyword
					else:
						sentence = make_keyword()
						sentence = make_other(keyword)
				else:
					if keyword in HanJaMo.CHOSUNG_LIST:
						keyword_dict['cho'] = keyword
						keyword_dict['edit'] = True
					else:
						sentence = make_other(keyword)
			else:
				if keyword_dict['edit']:
					sentence = make_keyword()

				sentence = make_other(keyword)

		if keyword_dict['edit']:
			sentence = make_keyword()

		return sentence
