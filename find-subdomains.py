target_url = 'google.com'

def request(target_url):
	import requests
	try:
		return requests.get('http://' + target_url)
	except requests.exceptions.ConnectionError:
		pass

with open('find-subdomains.txt', 'r') as wordlist_file:
		for line in wordlist_file:
			word = line.strip()
			url = word + '.' + target_url
			response = request(url)
			if response:
				print('[+] Discovered Subdomain --> ' + url)
