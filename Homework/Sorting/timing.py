from typing import List

def make_list(n: int) -> List[int]:
	'''Return a random list of n ints.
	'''
	
	import random
	res = list(range(n))
	random.shuffle(res)
	return res


def time_listfunc(f, n: int, m: int) -> float:
	'''Return how many seconds it takes to run function f on a shuffled 
	list with n items, on average over m times.
	'''

	import time
	total = 0
	for i in range(m):
		L = make_list(n)
		t1 = time.time()
		L = f(L)
		t2 = time.time()
		total += t2 - t1
	return total / m
