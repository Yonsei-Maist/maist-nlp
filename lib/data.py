import os


class DataManager:
	@staticmethod
	def get_all_data(base_path):
		file_list = []
		for (dir_path, dir_names, file_names) in os.walk(base_path):
			if len(file_names) > 0:
				file_list.extend(["{0}{1}".format(dir_path, item) for item in file_names])

		return file_list
