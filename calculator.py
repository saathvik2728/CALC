what = input("what are we doing?: (+,-,*,/,**):" )

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if what == "+":
  c = a + b
  print ("Answer =" + str(c))
elif what == "-":
  c = a - b
  print ("Answer =" + str(c))
elif what == "*":
  c = a * b
  print ("Answer =" + str(c))
elif what == "/":
  c = a / b
  print ("Answer =" + str(c) + "(balance)")
elif what == "**":
  c = a ** b
  print ("Answer =" + str(c))
else:
  print ("Invalid operation selected!")
  
  input ()