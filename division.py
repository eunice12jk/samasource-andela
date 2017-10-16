def divide(a,b):
  
  if type(a) == str:
    return "Has to be an integer"
  
  try:
    return a / b
    
  except ZeroDivisionError:
    return "Cannot divide by 0"
  
  