import pandas as pd

data = pd.read_csv("customers.csv")
cols = data.columns.tolist()[1:]

def count_str(c, f):
	it = data[cols[c]].tolist()
	
	count = 0
	for i in it:
		if f in i:
			count += 1
	return count

c_inp = input("What column are you looking at? \n" + ", ".join(cols) + "\n> ")
c = cols.index(c_inp)
f = input("What text are you looking for?\n> ")

print(f"We found '{f}' {count_str(c, f)} times.")
