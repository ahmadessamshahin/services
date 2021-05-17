import sys
sys.setrecursionlimit(30000)

def fibonacci(number, method="iterative"):
  """ DP implementation of Fibonacci to memoization the calculated values for nutural number using iterative approach 

  Args:
      number (Int): zero or positive numbers
			method (iterative | recursive)


  Raises:
      TypeError: Only integers are allowed
      Exception: Only zero and positive numbers

  Returns:
      Int: The fibonacci number of given input
  """
  fibonacciValidation(number)
  methods = {
    "iterative": fibonacciIterativeEvaluation,
    "recursive": fibonacciRecursiveEvaluation
    }
  return methods[method](number)

def fibonacciValidation(number):
  """ Fibonacci input validation 

  Args:
      number (Int)

  Raises:
      TypeError: Only integers are allowed
      Exception: Only zero and positive numbers
  """
  if not type(number) is int:
      raise TypeError("Only integers are allowed")
  if number < 0:
    raise Exception("Only zero and positive numbers")

def fibonacciIterativeEvaluation(number):
  """
  Args:
      number (Int)
  Returns:
      Int: The fibonacci number of given inputs
  """
  first = 0
  second = 1
  if number == 0:
    return first
  elif number == 1:
    return second
  else:
    for _ in range(2,number+1):
      temp = first + second
      first = second
      second = temp
    return second

def fibonacciRecursiveEvaluation(number, lookup = {}):
  """[summary]
  
  Args:
      number (Int)
      lookup (dict, optional). Defaults to {}.
  Raises:
        RecursionError: maximum recursion depth exceeded in comparison
  
  Returns:
      Int: The fibonacci number of given inputs
  """
  if(number == 0): 
      return 0
  if(number == 1):
      return 1
  if(number in lookup):
      return lookup[number]
  evaluation = fibonacciRecursiveEvaluation(number-1, lookup) + fibonacciRecursiveEvaluation(number-2, lookup)
  lookup[number]= evaluation
  return evaluation
