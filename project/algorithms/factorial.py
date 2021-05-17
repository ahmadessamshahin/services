def factorial(number,method="iterative"):
	"""
	Args:
			number (Int)
			method (iterative | recursive)

	Returns:
			Int: factorial of a given number
	"""
	factorialValidation(number)
	methods = {
		"iterative": factorialIterativeEvaluation,
		"recursive": factorialRecursiveEvaluation
	}
	return methods[method](number)


def factorialValidation(number):
	""" Check for zero positive numbers
	Args:
			number (int): 

	Raises:
			TypeError: Only integers are allowed
			Exception: Only zero and positive numbers
	"""
	if not type(number) is int:
		raise TypeError("Only integers are allowed")
	if number < 0:
			raise Exception("Only zero and positive numbers")

def factorialRecursiveEvaluation(number):
	"""Recursive approach
	Args:
			number (Int)
	Raises:
			RecursionError: maximum recursion depth exceeded in comparison
	Returns:
			Int: factorial Value
	"""
	return 1 if (number == 1 or number == 0) else number * factorialRecursiveEvaluation(number - 1) 

def factorialIterativeEvaluation(number):
	"""Iterative approach
	Args:
			number (Int)
	Returns:
			Int: factorial Value
	"""
	result = 1
	for i in range(2,number+1):
		result*= i
	return result
