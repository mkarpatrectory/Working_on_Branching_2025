import pandas as pd
cus = pd.read_csv("customers.csv")
cols = cus.columns.tolist()

ind = int(input("Give me the index of the column you're looking at: "))
look = input("Give me the name of the object you want to find: ")

def func(ind, look):
	count = cus[cols[ind]].tolist()
	n = 0
	
	for i in range(len(count)):
		if look in count[i]:
			n += 1
	return str(n)

print(func(ind,look))
	
	
	
