def isNumber(word):
  try:
        float(word)
        return True
  except ValueError:
        return False
