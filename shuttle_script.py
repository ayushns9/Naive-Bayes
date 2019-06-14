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

def loocv(data):
	correct=0
	for i in range(len(data)):
		a=bayes(data[:i]+data[i+1:],data[i])
		if(a and data[i][0]=='1'):
			#print(data[i],i)
			#print(i)

			correct+=1
		if(not(a) and data[i][0]=='2'):
			#print(i)

			correct+=1
			#print(data[i],i)
	return (correct/(len(data)))


def bayes(train,test):
	pyes=0
	nyes=0

	for i in train:
		if(i[0]=='1'):
			pyes+=1
			nyes+=1

	pyes/=len(train)

	p1_given_yes=[0]*(len(train[0])-1)
	p1_given_no=[0]*(len(train[0])-1)
	p2_given_yes=[0]*(len(train[0])-1)
	p2_given_no=[0]*(len(train[0])-1)
	p3_given_yes=[0]*(len(train[0])-1)
	p3_given_no=[0]*(len(train[0])-1)
	p4_given_yes=[0]*(len(train[0])-1)
	p4_given_no=[0]*(len(train[0])-1)

	for j in range(1,len(train[0])):
		for i in train:
			if((i[j]=='1' or i[j]=='*') and i[0]=='1'):
				p1_given_yes[j-1]+=1
			if((i[j]=='1' or i[j]=='*') and i[0]!='1'):
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


	for i in range(len(train[0])-1):
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

	for i in range(1,len(test)):
		if(test[i]=='1' or test[i]=='*'):
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

	#print(ppos,pneg)
	return ppos>=pneg


if __name__ == '__main__':
	data=[]
	getInput("shuttle-landing-control.data",data)
	#print(data)
	ans=100*loocv(data)
	update=["Shuttle Landing Control Data Set",ans]
	with open('Answer.csv', 'a') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(update)
	print(ans)