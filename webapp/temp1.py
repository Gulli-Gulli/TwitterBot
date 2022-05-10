
def extracturl():
	import re
	line="sssss "
	urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
	#print(urls)
	res=re.search("(?P<url>https?://[^\s]+)", line)
	print(res)
extracturl()





import requests
def extractfullurl():
	i="https://t.co/co1CI8IkUw"
	print(requests.head(i).headers['location'])
extractfullurl()

