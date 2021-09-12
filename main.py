from app import App
import web_server
from microDNSSrv import MicroDNSSrv

a = App()

# ToDo: move domainList to separate config-file
domainList = {
    '*': '192.168.4.1',
    'biogas.*': '192.168.4.1',
}

dns = MicroDNSSrv()
dns.SetDomainsList(domainList)
dns.Start()

web_server.set_app(a)
web_server.startWebServer()
