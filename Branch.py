import pandas as pd

customers = pd.read_csv("customers.csv")
cols=customers.columns.tolist()

def cust(column,target):
	col1 = customers[cols[cols.index(column)]].tolist()
	
	cols1 = 0
	
	for i in col1:
		if i ==target:
			cols1 = cols1+1
			
	return cols1

y = input("What column are u looking for? (Customer Id, First Name, Last Name, Company, City, Country, Phone 1, Phone 2, Email, Subscribtion Date, Website)")
x = input("what are u looking for?")	

cols1=cust(y,x)
print(cols1)




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
