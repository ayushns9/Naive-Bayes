import csv

def getInput(a,b):
	"""
		Input: Name of file to read from and the array.
		Output: Enters the data into the array.
	"""
	with open(a) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    for row in csv_reader:
	    	b.append(row)

def loocv(data):
	correct=0
	for i in range(len(data)):
		a=bayes(data[:i]+data[i+1:],data[i])
		if(a and data[i][-1]=='positive'):
			correct+=1
		if(not(a) and data[i][-1]!='positive'):
			correct+=1
	return (correct/(len(data)))


def bayes(train,test):
	pyes=0
	nyes=0
	for i in train:
		if(i[-1]=='positive'):
			pyes+=1
			nyes+=1

	pyes/=len(train)

	px_given_yes=[0]*(len(train[0])-1)
	px_given_no=[0]*(len(train[0])-1)
	po_given_yes=[0]*(len(train[0])-1)
	po_given_no=[0]*(len(train[0])-1)
	pb_given_yes=[0]*(len(train[0])-1)
	pb_given_no=[0]*(len(train[0])-1)

	for j in range(len(train[0])-1):
		for i in train:
			if(i[j]=='x' and i[-1]=='positive'):
				px_given_yes[j]+=1
			if(i[j]=='x' and i[-1]!='positive'):
				px_given_no[j]+=1
			if(i[j]=='o' and i[-1]=='positive'):
				po_given_yes[j]+=1
			if(i[j]=='o' and i[-1]!='positive'):
				po_given_no[j]+=1
			if(i[j]=='b' and i[-1]=='positive'):
				pb_given_yes[j]+=1
			if(i[j]=='b' and i[-1]!='positive'):
				pb_given_no[j]+=1

	for i in range(len(train[0])-1):
		px_given_yes[i]/=nyes
		px_given_no[i]/=len(train)-nyes
		po_given_yes[i]/=nyes
		po_given_no[i]/=len(train)-nyes
		pb_given_yes[i]/=nyes
		pb_given_no[i]/=len(train)-nyes


	#print(pb_given_yes)
	ppos=1
	pneg=1

	#print(px_given_yes)

	for i in range(len(test)-1):
		if(test[i]=='x'):
			ppos*=px_given_yes[i]
			pneg*=px_given_no[i]
		if(test[i]=='o'):
			ppos*=po_given_yes[i]
			pneg*=po_given_no[i]
		if(test[i]=='b'):
			ppos*=pb_given_yes[i]
			pneg*=pb_given_no[i]
	#print(test)
	ppos*=pyes
	pneg*=(1-pyes)

	#print(ppos)
	return ppos>=pneg


if __name__ == '__main__':
	data=[]
	getInput("tic-tac-toe.data",data)
	ans=100*loocv(data)
	update=["Tic-Tac-Toe Endgame Data Set",ans]
	update1=["Dataset","Accuracy"]
	with open('Answer.csv', 'w') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(update1)
	with open('Answer.csv', 'a') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(update)
	print(ans)
