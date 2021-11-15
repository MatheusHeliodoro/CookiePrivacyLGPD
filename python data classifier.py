results = open("results.txt","r")
dataset = open("dataset.txt","a")
dictionary_1 = "http://"  
dictionary_2 = 0
dictionary = {}
cookies = False
once = False
cookie_identificacao = ["NID","VISITOR_INFO1_LIVE","cna","sb","session-token","session_token","ADVC","ebay","A3","A1S","token_v2","_TRACERT_COOKIE__SESSION","uh","AuthV1","wa_ul","i","t","GuestData","mbox","bm_mi","_pin_unauth","bkng_sso_ses","locGuestData","settings","analytics_session_token","grauth","tmgioct","_pbjs_userid_consent_data","locDataV3","analytics_token","DEVICE_TOKEN"]
contains = ["visitor", "id","Id","ID"]
does_not_start_with = ["_g","__c"]
for line in results:
	if cookies == True:
		if line.startswith("set()"):
			dictionary_2 = 0
		elif line.startswith("page down"):
			dictionary_2 = -1
		else:
			line_dict_1 = (line[3:-3])
			line_dict = dict(item.split("', '") for item in line_dict_1.split("'), ('"))
			for key in line_dict.keys():
				if key in cookie_identificacao:
					dictionary_2 = 1
					break
				elif any(substring in key for substring in contains):
					if list(filter(key.startswith, does_not_start_with)):
						continue
					else:
						dictionary_2 = 1
						break
				else:
					dictionary_2 = 0 	
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