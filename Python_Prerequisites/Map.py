number = [1,2,3,4,5,6,7]
number2 = [1,5,6,7,9,11]

product =list(map(lambda x:x*x, number))
print(product)

double= list(map(lambda a,b:a+b, number,number2))
print(double)
