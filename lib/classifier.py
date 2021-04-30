from enum import Enum
import re


class CharType(Enum):
	KOREAN = 0
	ENGLISH = 1
	NUMBER = 2
	SPACE = 3
	OTHER = 4


class Character:
	ORIGIN = None
	TYPE = CharType.OTHER


class Classifier:
	def __init__(self, regex=None, tag=CharType.OTHER):
		self.regex = regex
		self._TAG = tag

	def classify(self, keyword):
		if self.regex is None or re.match(self.regex, keyword):
			return self._TAG
		else:
			return None


class KoreanClassifier(Classifier):
	def __init__(self):
		super().__init__('[ㄱ-ㅎ가-힣]', CharType.KOREAN)


class EnglishClassifier(Classifier):
	def __init__(self):
		super().__init__('[a-zA-Z]', CharType.ENGLISH)


class NumberClassifier(Classifier):
	def __init__(self):
		super().__init__('[0-9]', CharType.NUMBER)


class SpaceClassifier(Classifier):
	def __init__(self):
		super().__init__('\\s', CharType.SPACE)
