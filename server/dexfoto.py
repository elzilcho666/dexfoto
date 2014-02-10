import json
from twisted.web import server, resource
from twisted.internet import reactor
settings = {}
publicsettings = {}
users = {}
class dex(resource.Resource):
	isLeaf = True
	def setHeaders(self, request):
		request.setHeader('Access-Control-Allow-Origin','*')
		request.setHeader('Access-Control-Allow-Methods','GET, POST')
		request.setHeader('Access-Control-Allow-Headers','x-prototype-version,x-requested-with')
		request.setHeader('Access-Control-Max-Age',2520)
		request.setHeader('Content-type','application/json')
	def render_GET(self, request):
		self.setHeaders(request)
		if(request.path == '/getID'):
			return json.dumps(publicsettings)
		if(request.path == '/load'):
			try:
				return json.dumps(users[request.args['id'][0]])
			except:
				error = {}
				error['uerror'] = 'no settings yet'
				return json.dumps(error)
	def render_POST(self, request):
		self.setHeaders(request)
		if(request.path == '/save'):
			users[request.args['id'][0]] = request.args['settings'][0]
			saveUsers()

			return 'done'
			
def getSettings():
	fileOb = open('settings.json', 'r')
	settings = json.loads(fileOb.read())
	publicsettings['Client_ID'] = settings['Client_ID']
	fileOb.close
def saveUsers():
	fileOb = open('users.json', 'w')
	fileOb.write(json.dumps(users))
	fileOb.close()
def loadUsers():
	try:
		fileOb = open('users.json', 'r')
		users = json.loads(fileOb.read())
		fileOb.close()
	except:
		print "no users yet"
getSettings()
loadUsers()
root = dex()
root.putChild('ajax', dex())
reactor.listenTCP(9090, server.Site(root))
reactor.run()