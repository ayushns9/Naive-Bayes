import numpy
import csv

def getInput(a,b):
	"""
		Input: Name of file to read from and the array.
		Output: Enters the data into the array.
	"""
	with open(a) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=' ')
	    for row in csv_reader:
	    	b.append(row)



def bayes(train,test):
	pyes=0
	nyes=0

	for i in train:
		if(i[0]=='1'):
			pyes+=1
			nyes+=1

	pyes/=len(train)

	p1_given_yes=[0]*(len(train[0])-2)
	p1_given_no=[0]*(len(train[0])-2)
	p2_given_yes=[0]*(len(train[0])-2)
	p2_given_no=[0]*(len(train[0])-2)
	p3_given_yes=[0]*(len(train[0])-2)
	p3_given_no=[0]*(len(train[0])-2)
	p4_given_yes=[0]*(len(train[0])-2)
	p4_given_no=[0]*(len(train[0])-2)

	for j in range(1,len(train[0])-1):
		for i in train:
			if(i[j]=='1' and i[0]=='1'):
				p1_given_yes[j-1]+=1
			if(i[j]=='1' and i[0]!='1'):
				p1_given_no[j-1]+=1
			if(i[j]=='2' and i[0]=='1'):
				p2_given_yes[j-1]+=1
			if(i[j]=='2' and i[0]!='1'):
				p2_given_no[j-1]+=1
			if(i[j]=='3' and i[0]=='1'):
				p3_given_yes[j-1]+=1
			if(i[j]=='3' and i[0]!='1'):
				p3_given_no[j-1]+=1
			if(i[j]=='4' and i[0]=='1'):
				p4_given_yes[j-1]+=1
			if(i[j]=='4' and i[0]!='1'):
				p4_given_no[j-1]+=1


	for i in range(len(train[0])-2):
		p1_given_yes[i]/=nyes
		p1_given_no[i]/=len(train)-nyes
		p2_given_yes[i]/=nyes
		p2_given_no[i]/=len(train)-nyes
		p3_given_yes[i]/=nyes
		p3_given_no[i]/=len(train)-nyes
		p4_given_yes[i]/=nyes
		p4_given_no[i]/=len(train)-nyes


	#print(pb_given_yes)
	ppos=1
	pneg=1

	#print(px_given_yes)

	for i in range(1,len(test)-1):
		if(test[i]=='1'):
			ppos*=p1_given_yes[i-1]
			pneg*=p1_given_no[i-1]
		if(test[i]=='2'):
			ppos*=p2_given_yes[i-1]
			pneg*=p2_given_no[i-1]
		if(test[i]=='3'):
			ppos*=p3_given_yes[i-1]
			pneg*=p3_given_no[i-1]
		if(test[i]=='4'):
			ppos*=p4_given_yes[i-1]
			pneg*=p4_given_no[i-1]
		
	#print(test)
	ppos*=pyes
	pneg*=(1-pyes)

	#print(ppos)
	return ppos>=pneg


if __name__ == '__main__':
	train=[]
	test=[]
	getInput("monks-1.train",train)
	getInput("monks-1.test",test)
	for i in range(len(train)):
		train[i].remove('')
	for i in range(len(test)):
		test[i].remove('')
	#print(test)
	correct=0
	for i in test:
		a=bayes(train,i)
		if(a and i[0]=='1'):
			correct+=1
		if(not(a) and i[0]=='0'):
			correct+=1
	ans=100*correct/(len(test))
	update=["MONK\'s Problems data set",ans]
	with open('Answer.csv', 'a') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(update)
	print(ans)