class Type:

	# Caracters corresponding to type constructors
	funcCaracter = ["(", ")", 0]
	# From a string in Landau notation, returns a Type object corresponding to that string
	def parse(strType):

		# In Landau notation, -> type constructor is implicit
		# This generator inserts -> where they should be
		def genOp(s):
			for i, c in enumerate(s):
				if i != 0 and s[i-1] != "(" and s[i] != ")":
					# 0 is used as a code for -> type constructor
					yield 0
				yield c

		operands = []
		operators = []


		for c in genOp(strType):
			if c in Type.funcCaracter:
				if c != ")":
					operators.append(c)
				else:
					while operators[-1] != "(":
						if operators[-1] == 0:
							operators.pop()
							a = operands.pop()
							b = operands.pop()
							operands.append(Type((b,a)))
					operators.pop()

			else:
				operands.append(Type(c))

		while operators:
			if operators[-1] == 0:
				operators.pop()
				a = operands.pop()
				b = operands.pop()
				operands.append(Type((b,a)))
			else:
				raise NotImplementedError()

		return operands[-1].struct




	def __init__(self, strType):
		if isinstance(strType, str) and len(strType) > 1:
			self.struct = Type.parse(strType)
		else:
			self.struct = strType

	def __getitem__(self, idx):
		return self.struct[idx]

	def __repr__(self):
		return "Type({})".format(self.struct.__repr__())

	def __eq__(self, other):
		return isinstance(other, Type) and (
			   (self.is_basic() and other.is_basic() and self.struct == other.struct)
			   	or
			   	(not self.is_basic() and not other.is_basic() and self[0] == other[0] and self[1] == other[1]))

	def is_basic(self):
		return isinstance(self.struct, str)

	def __str__(self):
		if self.is_basic():
			return self.struct
		else:
			return ("({}){}" if not self[0].is_basic() else "{}{}").format(self[0], self[1])





