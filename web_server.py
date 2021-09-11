from microWebSrv import MicroWebSrv

@MicroWebSrv.route('/notfound')
def _httpHandler_notfound(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/notfound.pyhtml', vars={'title':'Not Found'})

@MicroWebSrv.route('/index')
def _httpHandler_index(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/index.pyhtml')

@MicroWebSrv.route('/info')
def _httpHandler_test(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/info.pyhtml', vars={'title':'Info'})

@MicroWebSrv.route('/settings')
def _httpHandler_test(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/settings.pyhtml')

@MicroWebSrv.route('/bootstrap.min.css')
def _httpHandler_getbootstrap(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/css/bootstrap.min.css', contentType='text/css')

@MicroWebSrv.route('/bootstrap.min.js')
def _httpHandler_getbootstrap(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/js/bootstrap.min.js', contentType='text/javascript')

def startWebServer():
    mws = MicroWebSrv()
    mws.SetNotFoundPageUrl('/notfound')
    mws.Start(threaded=True)
    return mws