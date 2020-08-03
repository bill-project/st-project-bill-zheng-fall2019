import pandas as pd
from sklearn import svm


dataset = pd.read_csv('DataForML.csv')
print(dataset)

listthings = dataset.drop('Student profiles', axis=1)
input1 = listthings.drop('Major 1', axis=1)
input2 = input1.drop('Major 2', axis=1)
input3 = input2.drop('Major 3', axis=1)
finalinput = input3.drop('Academic Profile', axis=1)

print(finalinput)

output_data1 = listthings['Major 1']
output_data2 = listthings['Major 2']
output_data3 = listthings['Major 3']
output_data4 = listthings['Academic Profile']

model1 = svm.SVC()
model1.fit(finalinput, output_data1)

model2 = svm.SVC()
model2.fit(finalinput, output_data2)

model3 = svm.SVC()
model3.fit(finalinput, output_data3)

model4 = svm.SVC()
model4.fit(finalinput, output_data4)


testprofile = []
result1 = model1.predict([testprofile])
result2 = model2.predict([testprofile])
result3 = model3.predict([testprofile])
result4 = model4.predict([testprofile])
if (str(result1) != str(result2)) and (str(result2) != str(result3)):
	print(result1)
	print(result2)
	print(result3)
	print(result4)
elif (str(result1) == str(result2)):
	print(result1)
	print(result3)
	print(result4)
elif (str(result1) == str(result3)):
	print(result1)
	print(result2)
	print(result4)
elif (str(result2) == str(result3)):
	print(result1)
	print(result2)
	print(result4)
