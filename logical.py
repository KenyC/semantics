from value import Value
from type import Type
from utils import currify
from nonlogical import mod

def binder(index, typeA = Type("e")):
	return Value(typeV = ("binder", typeA), value = index)

def pro(index, typeA = Type("e")):
	return Value(typeV = typeA, value = lambda g: g[index])

# Uncurrified version of every
def every_unC(domain, g, pred1, pred2):
	return all(pred2(x) if pred1(x) else True for x in domain)

# Semantic value of every for a particular domain
def every_C(domain):
	return Value(Type("(et)(et)t"), currify(every_unC, 4)(domain))

every = every_C(mod.E)