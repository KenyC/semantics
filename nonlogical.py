from utils import currify, untuple
from type import Type
from value import Value
from stdhk import StdHK

if __name__ == "__main__":
	Value.rules = StdHK

class Universe:

	def __init__(self):
		self.values = dict()
		self.E = set()


	def __getitem__(self, name, n = None):
		if n is None:
			n = 1 if isinstance(self.values[name][0], str) else len(self.values[name][0])
		return currify(untuple(self.values[name]), n)

	def __setitem__(self, name, value):
		# Since the function denoted by getitem is dependent on self.values[name],
		# we don't want to overwrite the reference of self.values[name],
		# just its values, hence the "[:]" at the end
		# The model is dynamically updated
		if name in self.values:
			self.values[name][:] = self.register(value)
		else:
			self.values[name] = self.register(value)
		

	def register(self, values):
		# We add potentially new individuals to the domain
		if isinstance(values, list):
			for t in values:
				t1 = t if isinstance(t, tuple) else [t]
				for v in t1:
					if isinstance(v, str):
						self.E.update([v])
		elif isinstance(values, str):
			self.E.update([values])
		else:
			raise Exception("Can't register this value")
		# for chaining
		return values

	def predicate(self, name, typeV = None):
		if typeV is None:
			if self.values[name]:
				n = 1 if isinstance(self.values[name][0], str) else len(self.values[name][0])
				typeV = Type(n*"e" + "t")
			else:
				raise Exception("Can't implicitly infer type: no element in extension")
		return Value(typeV, lambda g: mod[name])

	def individual(self, name):
		return Value(Type("e"), lambda g: self.register(name))


mod = Universe()

# love: a classic love triangle between the first three protagonists of our model
mod["love"] = [("Rosa", "Ahmed"), ("Ahmed", "Ren"), ("Ren", "Rosa")]
love = mod.predicate("love")

# basic predicates
mod["woman"] = ["Rosa", "Ren"]
woman = mod.predicate("woman")

mod["man"] = ["Ahmed", "Ben"]
man = mod.predicate("man")

mod["smiles"] = ["Ahmed", "Ben", "Rosa"]
smiles = mod.predicate("smiles")

# some individuals 
ahmed = mod.individual("Ahmed")
rosa = mod.individual("Rosa")
ren = mod.individual("Ren")