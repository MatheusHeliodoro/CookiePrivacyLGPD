import ast
import matplotlib.pyplot as plt
x_axis = []
y_axis = []
dataset = open("dataset.txt","r")
dict_set = ast.literal_eval(dataset.readline())
percentage = 0
conta = 0
for count,item in enumerate(dict_set.values()):
	if item == -1:
		conta -= 1
		continue
	conta += 1
	percentage += item
	x_axis.append(round((percentage/(conta+1)*100)))
	y_axis.append(conta)
x_axis = x_axis[10:]
y_axis = y_axis[10:]
plt.plot(y_axis, x_axis)
plt.show()