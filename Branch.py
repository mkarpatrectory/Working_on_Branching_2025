import pandas as pd

customers = pd.read_csv("customers.csv")
cols=customers.columns.tolist()

def cust(column,target):
	col1 = customers[cols[column]].tolist()
	
	cols1 = 0
	
	for i in col1:
		if i ==target:
			cols1 = cols1+1
			
	return cols1
	
cols1=cust(6,"China")
print(cols1)

cols2=cust(2, "John")
print(cols2)


"""
country=customers[cols[6]].tolist()


China=0
Company=0

for i in country:
	if i =="China":
		China = China + 1

for i in company:
	if "LLC" in i:
		Company = Company + 1
		
print(China, Company)
"""
