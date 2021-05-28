import sys
sys.setrecursionlimit(30000)

def ackermann(m, n, method="buttomUp"):
  """ Buttom up Implementation for Ackermann Algorithm

  Args:
      m (Int)
      n (Int)
			method (buttomUp | recursive)

  Returns:
      Int: Ackermann Evaluation
  """
  AckermannValidation(m, n)
  methods = {
		"buttomUp": AckermannButtomUpEvaluation,
    "recursive": AckermannRecursiveEvaluation,
	}
  return methods[method](m, n)

def AckermannValidation(m, n):
	""" Check for zero positive numbers
	Args:
			m (int)
			n (int)
	Raises:
			TypeError: Only integers are allowed
			Exception: Only zero and positive numbers
	"""
	if not type(m) is int or not type(n) is int:
		raise TypeError("Only integers are allowed")
	if m < 0 or n < 0:
			raise Exception("Only zero and positive numbers")

def AckermannButtomUpEvaluation(m, n):
  """memoization Buttom up approach
    Args:
        m (Int) 
        n (Int) 

    Returns:
        Int: Ackermann value
  """
  # memoized Array to save calculated values
  row= n+1 if(n==0 and m > 0 ) else n
  col= m
  lookup = [[0 for i in range(row + 1)] for j in range(col + 1)]
  for rows in range(col + 1):
      for cols in range(row + 1):
          # base case A ( 0, row ) = row + 1
          if rows == 0:       
              lookup[rows][cols] = cols + 1
          # base case  A ( col, 0 ) = 
          # A ( col-1, 1) [Computed already]
          elif cols == 0:
              lookup[rows][cols] = lookup[rows-1][1]
          else:
              # if rows and cols > 0
              # then applying A ( col, row ) = 
              # A ( col-1, A ( col, row-1 ) ) 
              r = rows - 1
              c = lookup[rows][cols-1]
              if r == 0:    
                  ans = c + 1
              elif c <= row:
                  ans = lookup[rows-1][lookup[rows][cols-1]]
              else:
                  ans = (c-row)*(r) + lookup[r][row]
              lookup[rows][cols] = ans
  return lookup[m][n]


def AckermannRecursiveEvaluation(m, n, lookup ={}):
  """ memoization Recursive approach
  Args:
      m (Int) 
      n (Int) 
      lookup (dict, optional). Defaults to {}.
  Raised: 
      segmentation fault (core dumped) 
  Returns:
      Int: Ackermann value
  """
  lookupIndex= (m, n)

  if not lookupIndex in lookup :   
    # base case A ( 0, n ) = n + 1
    if m == 0:
      result = n + 1
    # base case  A ( m, 0 ) = 
    # A ( m-1, 1) [Computed already]
    elif n == 0  : 
      result = AckermannRecursiveEvaluation(m-1, 1, lookup)

    else:
      result =  AckermannRecursiveEvaluation(m - 1,  AckermannRecursiveEvaluation(m, n-1, lookup), lookup)
  
    lookup[lookupIndex]  = result

  return lookup[lookupIndex]
