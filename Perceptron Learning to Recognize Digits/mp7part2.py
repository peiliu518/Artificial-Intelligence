import pickle 
import numpy as np
import random

epoch = 1
while epoch != 0 :

	a = pickle.load(open("train.p"))
	test_data = pickle.load(open("test.p"))
	bias = 1
	#randomize the data
	train_data = [] 
	for i in range(len(a)): 
		element = random.choice(a) 
		a.remove(element) 
		train_data.append(element) 


	for i in range(len(train_data)):
		train_data[i][0].append(bias)

	for i in range(len(test_data)):
		test_data[i][0].append(bias)

	alpha = 0.6
	numVector, numDimension = 10, 785
	weight = [[0 for x in range(numDimension)] for y in range(numVector)] 



#train
	for traindataindex in range(len(train_data)):
		label = 0
		error = 0
		for perceptronindex in range(10):
			#update the label
			if perceptronindex == train_data[traindataindex][1]:
				label = 1
			else:
				label = 0
			#calculate the error
			if np.dot(train_data[traindataindex][0], weight[perceptronindex]) > 0: 
				error = label - 1
			else:
				error = label
			#update weight			
			if error != 0:
				for pixelindex in range(len(weight[perceptronindex])):
					weight[perceptronindex][pixelindex] = weight[perceptronindex][pixelindex] + alpha*train_data[traindataindex][0][pixelindex]*error

	epoch = epoch -1



correct = 0
incorrect = 0
for i in range(len(test_data)):
	result = np.zeros(10)
	for j in range(10):
		result[j] = np.dot(test_data[i][0], weight[j])
	maxlabel = np.argmax(result)
#	print maxlabel
	if maxlabel == test_data[i][1]: 
		correct = correct + 1
	else:
		incorrect = incorrect +1
#	print correct
#	print incorrect
print "number of correct:" ,correct, "number of incorrect:", incorrect
