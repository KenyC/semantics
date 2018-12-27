# Standard Heim & Kratzer rules of composition
from utils import isTEnding
from rules import Rule
from type import Type
from value import Value

class FA(Rule):

	def match(self, type1, type2):
		return isinstance(type1, Type) and isinstance(type2, Type) and not type2.is_basic() and type1 == type2[0]

	def combine_val(self, val1, val2):
		return Value(val2.type[1], lambda g: val2.value(g)(val1.value(g)))


	def __str__(self):
		return "Functional Application"

	
class Abstraction(Rule):

	def match(self, type1, type2):
		return isinstance(type1, tuple) and (type1[0] == "binder")

	def combine_val(self, val1, val2):
		return Value(Type((val1.type[1], val2.type)), lambda g: lambda x: val2.value({**g, val1.value: x}))

	def __str__(self):
		return "Lambda Abstraction"

class PredicateModification(Rule):

	def match(self, type1, type2):
		return type1 == type2 and isTEnding(type1)

	def combine_val(self, val1, val2):
		return Value(val1.type, lambda g: self.conjoin(val1.value(g), val2.value(g), val1.type))

	def conjoin(self, val1, val2, typeV):
		if typeV.is_basic():
			return val1 and val2
		else:
			return lambda x: self.conjoin(val1(x), val2(x), typeV[1])

	def __str__(self):
		return "PredicateModification"

StdHK = [FA(), Abstraction(), PredicateModification()]