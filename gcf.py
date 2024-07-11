def euclidian(arrayOld):
  a = arrayOld[1]
  b = arrayOld[3]
  if b>a:
    tempA = a
    a = b
    b = tempA
  q = a//b
  r = a-b*q
  return [a, b, q, r]

def gcf(a, b):
  array = [0, a, 0, b]
  while array[3] != 0:
    arrayOld = array
    array = euclidian(arrayOld)
  return arrayOld[3]

firstNum = int(input("First Number: "))
secondNum = int(input("Second Number: "))
print("GCF: ", gcf(firstNum, secondNum))
