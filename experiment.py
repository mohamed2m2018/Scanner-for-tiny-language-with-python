z="444"

x=" 4  "
def isNumber(s):
  try:
        float(s)
        return True
  except ValueError:
        return False


print (isNumber(z))
print (isNumber(x))
