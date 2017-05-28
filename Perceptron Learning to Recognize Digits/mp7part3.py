import pickle 
import numpy as np
import random
from sklearn.neural_network import MLPClassifier


train_data = pickle.load(open("train.p"))
test_data = pickle.load(open("test.p"))
bias = 1
r = 0.001
epoch = 1

a = [w[0] for w in test_data]
b = [w[1] for w in test_data]

validation_data = []
validation_label = []
training_data = []
training_label = []

for j in range(epoch):
	for i in range(len(train_data)): 
		if i%5 == 0:
			validation_data.append(train_data[i][0])
			validation_label.append(train_data[i][1])
		else:
			training_data.append(train_data[i][0])
			training_label.append(train_data[i][1])

	clf = MLPClassifier(alpha=r, hidden_layer_sizes= (100,100), activation='relu', max_iter = 300)
	clf.fit(training_data,training_label)

	#validation
	score = clf.score(validation_data,validation_label)
	print "Validation accuracy:", score
	epoch = epoch - 1

#testing
score = clf.score(a, b)

print "Test accurarcy:", score 