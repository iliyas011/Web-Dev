def missing_char(str, n):
   a = str[:n]
   b = str[n+1:]
   return a+b  

print(missing_char('kitten', 1))    
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))