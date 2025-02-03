import pandas as pd

def findc(ind,w):
	org=pd.read_csv("customers.csv")
	col=org.columns.tolist()
	ai=org[col[ind]].tolist()
	num=0
	for i in ai:
		if w in i: num+=1
	return str(num)
	
uin=int(input("Enter the index for the column:"))
uw=input("Enter the word you need to find:")
print("We find")
print(uw+":"+findc(uin,uw))
