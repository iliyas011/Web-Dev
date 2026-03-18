def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == False:
    return False 
  elif weekday ==False and vacation == True :
    return True 
  elif weekday == True  and vacation == True :
    return True 

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))