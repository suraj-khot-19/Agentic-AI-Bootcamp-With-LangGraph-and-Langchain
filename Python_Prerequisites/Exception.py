a= 10

try:
    a=b
except Exception as e:
    print(e)


try:
    a= a/0
except ZeroDivisionError as e:
    print(e)