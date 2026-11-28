num=[0,1,2,3,4,5,6,7, 3,6,7,8,9,10]

bools = list(map(lambda x:x%2==0, num))
print(bools)
even = list(filter(lambda x:x%2==0, num))
print(even)

odd = list(filter(lambda x:x%2!=0, num))
print(odd)