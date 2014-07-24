class importAs(object):
	"""docstring for importAs"""
	def __init__(self, filename):
		super(importAs, self).__init__()
		self.filename = filename
	
	def list_of_chars():
	    '''file -> list of chars
	    '''
	    f = open(self.filename, 'r')
	    file_list = list(f.read())
	    f.close()
	    return file_list

	def list_of_csv_rows():
		import DictReader from csv
	    '''csv file -> list of rows'''
	    with open(self.filename) as verification:
	        ver_dict = [line for line in DictReader(verification)]
	    return ver_dict