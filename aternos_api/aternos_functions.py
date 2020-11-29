import hashlib
import random
import urllib.parse

from requests import session

from .aternos_vars import AJAX_TOKEN, COOKIE_PREFIX


def randomString(length):
	char36 = "0123456789abcdefghijklmnopqrstuvwxyz"
	base36 = "".join([random.choice(char36) for x in range(11)])
	char = "0." + base36 + '00000000000000000'
	return char[2:length + 2]


def hashPassword(password):
	return hashlib.md5(password.encode("utf8")).hexdigest()


def generateAjaxToken(asession: session, url):
	key = randomString(16)
	value = randomString(16)
	asession.cookies.set(COOKIE_PREFIX + "_SEC_" + key, value + ";path=" + url)
	asession.cookies.set("path", url)

	token = key + ":" + value
	return token


def buildURL(asession: session, url, data):
	data["SEC"] = generateAjaxToken(asession, url)
	data["TOKEN"] = AJAX_TOKEN
	return url + "?" + urllib.parse.urlencode(data)


def apost(asession: session, url, data={}):


	burp0_url = buildURL(asession, url, {})
	burp0_cookies = {"ATERNOS_SEC_7bawidcle0t00000": "3uayvfdrudm00000"}
	for cookie in asession.cookies.get_dict():
		if "_SEC_" in cookie:
			burp0_cookies = {
				cookie: asession.cookies.get(cookie),
			}
	burp0_headers = {
		"Connection": "close", "Accept": "*/*",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Origin": "https://aternos.org",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://aternos.org/go/",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	# burp0_data = {
	# 	"user": "rafalou38",
	# 	"password": "5f252feb881bd8952431f432703604bc"
	# }
	return asession.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=data)


def aget(asession: session, url, data):
	return asession.get(
		url=buildURL(url, {}),
	)
