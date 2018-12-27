from type import Type

def isTEnding(typeV):
	return isinstance(typeV, Type) and typeV.struct == "t" if typeV.is_basic() else	(isTEnding(typeV[1]))

def currify(f, n):
	if n == 1:
		return f
	else:
		return lambda x: currify(lambda *args: f(x, *args), n-1)

def untuple(l):
	return lambda *args: (args if len(args) > 1 else args[0]) in l


def test(a, b, c):
	return a + (b*c)