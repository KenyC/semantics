from value import Value
from stdhk import StdHK
from nonlogical import *
from logical import *

if __name__ == "__main__":
	Value.rules = StdHK

test = 	(every + man) + smiles





print(test.val())

test = ren + (binder(1) + (pro(1) + smiles))
print(test.val())


test = (every + man) + (binder(1) + (rosa + (loves + pro(1))))
print(test.val())
