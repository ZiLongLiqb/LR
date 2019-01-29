import math
import copy


global Result
Result=[]
global count
count=0


#################function area####################
def func1(n):
	if n==1:
		return n
	else:
		return func1(n-1)*n


def func2(n1,n2):
	return func1(n1+n2)/(func1(n1)*func1(n2))


def multi(L):
	Mu=1
	for item in L:
		Mu=Mu*item
	return Mu


def Sum(l1):
	sum=0
	for item in l1:
		sum=sum+item
	return sum


def whether_suit(l1):
	if len(l1)==1:
		return True
	for i in range(len(l1)-1):
		if len(l1[i])<len(l1[i+1]):
			return False
	return True


def format_lc(l1,l2):
	l_1=[]
	for item in l1:
		l_1.append([0]*item)
	l_2=[]
	for i in range(len(l2)):
		l_2=l_2+[i+1]*l2[i]
	lc(l_1,l_2)



def lc(l1,l2):
	if len(l2)==0:
		result=[]
		for i in range(len(l1)):
			result.append(len(l1[i]))
		global Result
		Result.append(l1)
		#print(result)
		return 
	length=len(l1)
	for i in range(length+1):
		l11=copy.deepcopy(l1)
		l22=[item for item in l2]
		l11[i].append(l22[0]) if i<length else l11.append([l22[0]])
		if (whether_suit(l11))==False:
			continue
		if i!=0:
			if l11[i][len(l11[i])-1]==l11[i-1][len(l11[i])-1]:
				continue
		forma={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
		prime=True
		for j in range(len(l11)):
			for k in range(len(l11[j])-1,-1,-1):
				forma[l11[j][k]]=forma[l11[j][k]]+1
				global count
				count=count+1
				if l11[j][k]<=1:
					continue
				else:
					if forma[l11[j][k]-1]>=forma[l11[j][k]]:
						continue
					else:
						prime=False
						break
			if prime==False:
				break
		if prime==False:
			continue
		else:
			del l22[0]
			lc(l11,l22)



def hook(sequence):
	length=len(sequence)
	if length==0:
		return 1
	hook_num=[]
	for i in range(sequence[0]):
		hook_num.append(sequence[0]-i)
		for j in range(1,length):
			if i+1<=sequence[j]:
				hook_num[i]=hook_num[i]+1
			else:
				break
	del sequence[0]
	return multi(hook_num)*hook(sequence)


def dimen(L):
	sum=0
	for item in L:
		sum=sum+item
	return func1(sum)/hook(L)
############function area end#########


############parameter area###########
'''format_lc([5,4,3,2,1],[2,1])
Result_final=[]
for item in Result:
	if item in Result_final:
		continue
	else:
		Result_final.append(item)
Result_final_divide=[]
for item in Result_final:
	Result_final_divide.append([len(item1) for item1 in item])

print(len(Result_final_divide))
#print(Result_final_divide)
Dimension=0
for item in Result_final_divide:
	Dimension=Dimension+dimen(item)'''
###########parameter area end###########



##########output area###############

def refer(l1,l2):
	format_lc(l1,l2)
	Result_final=[]
	for item in Result:
		if item in Result_final:
			continue
		else:
			Result_final.append(item)
	Result_final_divide=[]
	for item in Result_final:
		Result_final_divide.append([len(item1) for item1 in item])
		return len(Result_final_divide)