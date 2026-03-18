def front3(str):
  f = 3 
  if len(str) < f:
    f = len(str)
  f = str[:f]
  return f + f + f

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))