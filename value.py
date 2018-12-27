

class TypeMismatch(Exception):
	def __init__(self, rules, *types):
		 Exception.__init__(self,"Types {} can't combine.\n Rules are: {}".format(" and ".join([str(t) for t in types]), ",".join([str(r) for r in rules])))

class Value:

	rules = []

	def __init__(self, typeV, value, metaLg = None):
		self.type = typeV
		self.value = value
		self.metaLg = None

	""" Combine two semantic values according to "rules"
	Args:
		- option (optional)
			* "first" the first rule that can apply applies ; if rules are symmetric, left-to-right is chosen over right-to-left
			* "all" returns all possible values (not implemented yet)
	"""
	def __add__(self, other, option = "first"):
		if option == "first":
			for rule in Value.rules:
				if rule.match(self.type, other.type):
					return rule.combine_val(self, other)
				elif rule.symmetric and rule.match(other.type, self.type):
					return rule.combine_val(other, self)

			raise TypeMismatch(Value.rules, self.type, other.type)
		else:
			raise NotImplementedError()

	def val(self, g = {}):
		return self.value(g)