from requests import session
from .aternos_functions import hashPassword, apost
from .exceptions import loginError
from bs4 import BeautifulSoup


class Account():
	def __init__(self):
		self.session = session()
		self.servers = []

	def login(self, username, password):
		password = hashPassword(password)
		self.username = username
		arguments = {
			"user": username,
			"password": password
		}
		r = apost(
			self.session,
			'https://aternos.org/panel/ajax/account/login.php',
			arguments
		)
		data = r.json()
		if not data['success']:
			raise loginError(data['error'])

	def close(self):
		self.session.close()

	def fetch_servers(self):
		from .server import Server

		servers_page = self.session.get('https://aternos.org/servers/')
		soup = BeautifulSoup(servers_page.text, "html.parser")
		servers = soup.find_all("div", {"class": "server"})
		self.servers = []
		for server in servers:
			server_name = server.find("div", {"class": "server-name"}).text.strip()
			server_id = server.get_attribute_list("data-server_id")[0]
			server_version = server.find("div", {"class": "server-software"}).text.strip()
			try:
				server_author = server.find("div", {"class": "server-by-user"}).text.strip()
				server_author = server_author.split(" ")[-1:][0].strip()
			except AttributeError:
				server_author = self.username
			self.servers.append(
				Server(
					author=server_author,
					account=self,
					server_id=server_id,
					name=server_name
				)
			)
