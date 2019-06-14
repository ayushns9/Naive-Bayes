from numpy1 import *
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
		if(a==1 and data[i][-1]=='D1'):
			correct+=1
		if(a==2 and data[i][-1]=='D2'):
			correct+=1
		if(a==3 and data[i][-1]=='D3'):
			correct+=1
		if(a==4 and data[i][-1]=='D4'):
			correct+=1
	ans=correct/len(data)
	return (ans*100)


def bayes(train,test):
	d={1:0,2:0,3:0,4:0}

	for i in train:
		d[int(i[-1][1])]+=1

	p={'D1':[],'D2':[],'D3':[],'D4':[]}

	for i in p.keys():
		for j in range(6):
			p[i].append([0]*(len(train[0])-1))

	for j in range(len(train[0])-1):
		for i in train:
			#print(train[-1])
			p[i[-1]][int(i[j])-1][j]+=1

	for i in range(len(train[0])-1):
		for j in p.keys():
			for k in range(len(p[j])):
				p[j][k][i]/=d[int(j[1])]

	pd1=1
	pd2=1
	pd3=1
	pd4=1

	for i in range(len(test)-1):
		pd1*=p['D1'][int(test[i])-1][i]
		pd2*=p['D2'][int(test[i])-1][i]
		pd3*=p['D3'][int(test[i])-1][i]
		pd4*=p['D4'][int(test[i])-1][i]

	pd1*=d[1]/len(train)
	pd2*=d[2]/len(train)
	pd3*=d[3]/len(train)
	pd4*=d[4]/len(train)
	# print(pd1,pd2,pd3,pd4)
	if(pd1>0):
		return 1
	elif(pd2>0):
		return 2
	elif(pd3>0):
		return 3
	elif(pd4>0):
		return 4
	else:
		return 1


if __name__ == '__main__':
	data=[]
	getInput("soybean-small.data",data)
	ans=loocv(data)
	update=["Soybean (Small) Data Set",ans]
	with open('Answer.csv', 'a') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(update)
	print(ans)