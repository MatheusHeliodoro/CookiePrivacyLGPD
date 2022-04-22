import ast
import matplotlib.pyplot as plt
x_axis = []
y_axis = []
dataset = open("dataset.txt","r")
dict_set = ast.literal_eval(dataset.readline())
national_dict = {}
percentage = 0
conta = 0
for key in dict_set:
	if key.endswith(".br"):
		national_dict[key] = dict_set[key]		
	
for count,item in enumerate(national_dict.values()):
	#print(dict_set.keys())
	if item == -1:
		conta -= 1
		pass
	conta += 1
	percentage += item
	x_axis.append(round((percentage/(conta+1)*100)))
	y_axis.append(conta)
x_axis = x_axis[10:]
y_axis = y_axis[10:]
plt.plot(y_axis, x_axis)
plt.show()