from lib.classifier import Classifier


class Parser:
	def __init__(self, classifier_list: list[:Classifier]):
		self._classifier_list = classifier_list
		self._classifier_list.append(Classifier())

	def parse(self, text):
		text_list = list(text)

		for keyword in text_list:
			for classifier in self._classifier_list:
				kind = classifier.classify(keyword)

				if kind is not None:

					break
