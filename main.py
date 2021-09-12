from app import App
import web_server

a = App()
web_server.set_app(a)
web_server.startWebServer()
