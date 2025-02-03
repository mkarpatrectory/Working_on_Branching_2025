import pandas as pd

customers = pd.read_csv("customers.csv")


for i in customers:

	print(customers[i])

inp1 = input("What column are you looking for? ")
	
inp2 = input("What item are you looking for? ")
	
	
def dontknow(inp1, inp2):
	count = 0
		
	column = customers[inp1]
	
	for i in column:
		if inp2 == i or inp2 in i:
			count += 1
	print(count)

dontknow(inp1, inp2)
