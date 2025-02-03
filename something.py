import pandas as pd

def find(col,word):
	app=0
	for i in range(len(col)):
		if col[i]==word:
			app+=1
		elif word in col[i]:
			app+=1
	return app
	
cus=pd.read_csv("customers.csv")
cols=cus.columns.tolist()
country=cus[cols[6]].tolist()
company=cus[cols[4]].tolist()

a=find(country, 'China')
b=find(company, 'LLC')

print('Customers from China',a)
print('Customers from llc', b)
