from microWebSrv import MicroWebSrv


gapp = None

def set_app(app):
    global gapp
    gapp = app

@MicroWebSrv.route('/notfound')
def _httpHandler_notfound(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/notfound.pyhtml', vars={'title':'Not Found'})



@MicroWebSrv.route('/index')
def _httpHandler_index(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/index.pyhtml', vars={
        'weight': str(gapp.waage.get_tared_weight()),
        'portion': str(gapp.get_portion()),
    })

@MicroWebSrv.route('/index/<command>')
def _httpHandler_index(httpClient, httpResponse, routeArgs):
    print(routeArgs)
    if 'start' in routeArgs['command']:
        gapp.start()
    elif 'stopor' in routeArgs['command']:
        gapp.start_one_portion()
    elif 'stop' in routeArgs['command']:
        gapp.stop()
    httpResponse.WriteResponsePyHTMLFile('www/index.pyhtml', vars={
        'weight': str(gapp.waage.get_tared_weight()),
        'portion': str(gapp.get_portion()),
    })

@MicroWebSrv.route('/waage')
def _httpHandler_index(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/waage.pyhtml', vars={
        'weight': str(gapp.waage.get_tared_weight()),
        'portion': str(gapp.get_portion()),
    })

@MicroWebSrv.route('/waage/<command>')
def _httpHandler_index(httpClient, httpResponse, routeArgs):
    print(routeArgs)
    if 'zeropoint' in routeArgs['command']:
        gapp.waage.set_zeropoint()
    elif 'calibrate' in routeArgs['command']:
        gapp.waage.set_calibration(65)
    elif 'tara' in routeArgs['command']:
        gapp.waage.set_tara()
    elif 'reset' in routeArgs['command']:
        gapp.waage.reset_all_data()
    httpResponse.WriteResponsePyHTMLFile('www/waage.pyhtml', vars={
        'weight': str(gapp.waage.get_tared_weight()),
        'portion': str(gapp.get_portion()),
    })


@MicroWebSrv.route('/info')
def _httpHandler_test(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/info.pyhtml', vars={'title': str(gapp.get_portion())})


@MicroWebSrv.route('/settings')
def _httpHandler_test(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/settings.pyhtml')


@MicroWebSrv.route('/bootstrap.min.css')
def _httpHandler_getbootstrap(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/css/bootstrap.min.css', contentType='text/css')


@MicroWebSrv.route('/bootstrap.min.js')
def _httpHandler_getbootstrap(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/js/bootstrap.min.js', contentType='text/javascript')

@MicroWebSrv.route('/start.pyhtml')
def _httpHandler_start(httpClient, httpResponse):
    gapp.start()
    httpResponse.WriteResponseOK()


def startWebServer():
    mws = MicroWebSrv()
    mws.SetNotFoundPageUrl('/notfound')
    mws.Start(threaded=True)
    return mws
