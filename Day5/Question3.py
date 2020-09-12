
str = str(input("Enter the number"))

st = ' '.join(list(map(lambda x: x.strip().capitalize(), str.split(' '))))
print("Capitalizing :",st)