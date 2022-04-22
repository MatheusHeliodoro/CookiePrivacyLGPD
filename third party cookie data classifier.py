results = open("results.txt","r")
dataset = open("dataset_third_party.txt","a")
dictionary_1 = "http://"  
dictionary_2 = 0
dictionary = {}
cookies = False
once = False
for line in results:
	if cookies == True:
		if line.startswith("set()"):
			dictionary_2 = 0
		elif line.startswith("page down"):
			dictionary_2 = -1
		else:
			dictionary_2 = 1	
		cookies = False
		once = True
	elif line.startswith("http://"):
		if once == True:
			dictionary.update({dictionary_1:dictionary_2})
		dictionary_1 = line[11:-1]
		cookies = True		
	else:
		continue
dataset.write(str(dictionary))