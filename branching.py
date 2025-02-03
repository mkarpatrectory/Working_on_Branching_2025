def findc(ind,w):
	org=pd.read_csv("customers.csv")
	col=org.colums.tolist()
	ai=org[col[ind]].tolist()
	num=0
	for i in ai:
		if w in i: num+=1
	return num


