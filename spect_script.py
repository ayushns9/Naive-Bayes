import numpy
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

def bayes(train,test):
	pyes=0
	nyes=0
	for i in train:
		if(i[0]=='0'):
			pyes+=1
			nyes+=1

	pyes/=len(train)

	p1_given_1=[0]*(len(train[0])-1)	
	p1_given_0=[0]*(len(train[0])-1)
	p0_given_1=[0]*(len(train[0])-1)
	p0_given_0=[0]*(len(train[0])-1)

	for j in range(1,len(train[0])):
		for i in train:
			if(i[j]=='0' and i[0]=='0'):
				p0_given_0[j-1]+=1
			if(i[j]=='1' and i[0]=='0'):
				p1_given_0[j-1]+=1
			if(i[j]=='1' and i[0]=='1'):
				p1_given_1[j-1]+=1
			if(i[j]=='0' and i[0]=='1'):
				p0_given_1[j-1]+=1

	for i in range(len(train[0])-1):
		p0_given_1[i]/=nyes
		p0_given_0[i]/=len(train)-nyes
		p1_given_1[i]/=nyes
		p1_given_0[i]/=len(train)-nyes

	#print(pb_given_yes)
	ppos=1
	pneg=1

	#print(px_given_yes)

	for i in range(1,len(test)):
		if(test[i]=='0'):
			ppos*=p0_given_1[i-1]
			pneg*=p0_given_0[i-1]
		if(test[i]=='1'):
			ppos*=p1_given_1[i-1]
			pneg*=p1_given_0[i-1]

	#print(test)
	ppos*=pyes
	pneg*=(1-pyes)

	#print(pyes,1-pyes)

	return ppos>=pneg

if __name__ == '__main__':
	train=[]
	test=[]
	getInput("SPECT.train",train)
	getInput("SPECT.test",test)
	correct=0
	for i in test:
		a=bayes(train,i) 
		if(a and i[0]=='1'):
			correct+=1
		if(not(a) and i[0]=='0'):
			correct+=1
	ans=100*correct/len(test)
	update=["SPECT Heart Data Set",ans]
	with open('Answer.csv', 'a') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(update)
	print(ans)