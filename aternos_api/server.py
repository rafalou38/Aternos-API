from .account import Account
from .player import Player


class Server(object):
	def __init__(self, author: str, account: Account, server_id: str = None, name: str = None):
		self.account = account
		self._status: str = ""
		self.version_type: str = ""
		self.version: str = ""
		self.author: str = author
		self.id: str = server_id
		self._connect_ip: str = ""
		self.port: int = 0
		self.name: str = name
		self.ip: str = ""
		self.max_players: int = 0
		self._player_count: int = 0
		self._players: [Player] = []
		self._countdown: int = 0
		self.motd: str = ""
		self.ram: int = 0

	@property
	def players(self):
		# self.fetch()
		return self._players

	@property
	def status(self):
		# self.fetch()
		return self._status

	@property
	def player_count(self):
		# self.fetch()
		return self._players

	@property
	def connect_ip(self):
		# self.fetch()
		return self._connect_ip

	@property
	def countdown(self):
		# self.fetch()
		return self._countdown

	def fetch(self):
		result = {}

		self.version_type = result["type"]
		self.version = result["version"]
		self.id = result["server_id"]
		self._connect_ip = result["host"]
		self.port = result["port"]
		self.name = result["name"]
		self.ip = result["ip"]
		self.max_players = result["slots"]
		self._player_count = result["players"]
		self._players = [Player(name) for name in result["playerlist"]]
		self._countdown = result["countdown"]
		self.motd = result["motd"]
		self.ram = result["ram"]
		self._status = result["lang"]

	def __str__(self):
		return f"server {self.name} from {self.author}"

	def __repr__(self):
		return f"<{self.__str__()}>"

	def start(self):
		# TODO start the server
		pass
