from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def get_cookies(domain):
	results = open("results.txt", "a")
	results.write("\n")
	results.write(domain)
	print(domain)
	driver = webdriver.Chrome(options=options)
	try:
    		driver.get(domain)
	except WebDriverException:
		results.write("page down")
		results.write("\n")
		driver.quit()
		return	
	cookies_list1 = driver.get_cookies()
	cookies_visita1 = {}
	for cookie in cookies_list1:
		cookies_visita1[cookie['name']] = cookie['value']	
	driver.quit()
	#revisita
	driver = webdriver.Chrome(options=options)
	try:
    		driver.get(domain)
	except WebDriverException:
		results.write("page down")
		results.write("\n")
		driver.quit()
		return	
	cookies_list2 = driver.get_cookies()
	cookies_visita2 = {}
	for cookie in cookies_list2:
		cookies_visita2[cookie['name']] = cookie['value']
	cookies_persistentes = set( cookies_visita1.items() ) & set( cookies_visita2.items() )
	results.write(str(cookies_persistentes))
	results.write("\n")	
	driver.quit()
		
#configurar perfil de usuario em uma pasta selenium
options = Options()
options.add_argument("user-data-dir=test")
options.add_argument("enable-automation")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disable-gpu")
 
#configurar o webdriver
sites_txt = open("top 100000.txt", "r")
for site in sites_txt:
	get_cookies("http://www."+ site)


