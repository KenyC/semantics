

class Rule:

	def __init__(self, symmetric = True):
		self.symmetric = symmetric

	def match(self, type1, type2):
		return False

	def combine_val(self, val1, val2):
		return None



