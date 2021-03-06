from microWebSrv import MicroWebSrv


gapp = None

def set_app(app):
    global gapp
    gapp = app


@MicroWebSrv.route('/')
def _httpHandler_proceed_to_index(httpClient, httpResponse):
    httpResponse.WriteResponseRedirect('/index')

@MicroWebSrv.route('/notfound')
def _httpHandler_notfound(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/notfound.pyhtml', vars={'title':'Not Found'})



@MicroWebSrv.route('/index')
def _httpHandler_index(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/index.pyhtml', vars={
        'weight': str(gapp.waage.get_tared_weight()),
        'portion': str(gapp.get_portion()),
    })

"""@MicroWebSrv.route('/index/<command>')
def _httpHandler_index(httpClient, httpResponse, routeArgs):
    print(routeArgs)
    if 'start' in routeArgs['command']:
        gapp.start()
    elif 'stopor' in routeArgs['command']:
        gapp.start_one_portion()
    elif 'stop' in routeArgs['command']:
        gapp.stop()
    httpResponse.WriteResponseRedirect('/index')"""

@MicroWebSrv.route('/waage')
def _httpHandler_index(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/waage.pyhtml', vars={
        'weight': str(gapp.waage.get_tared_weight()),
        'portion': str(gapp.get_portion()),
    })

"""@MicroWebSrv.route('/waage/<command>')
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
    httpResponse.WriteResponseRedirect('/waage')"""


@MicroWebSrv.route('/info')
def _httpHandler_info(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/info.pyhtml', vars={'title': str(gapp.get_portion())})


@MicroWebSrv.route('/settings')
def _httpHandler_settings(httpClient, httpResponse):
    httpResponse.WriteResponsePyHTMLFile('www/settings.pyhtml')

@MicroWebSrv.route('/jquery.min.js')
def _httpHandler_getjquery(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/js/jquery.min.js', contentType='text/javascript')

@MicroWebSrv.route('/bootstrap.min.css')
def _httpHandler_getbootstrap(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/css/bootstrap.min.css', contentType='text/css')


@MicroWebSrv.route('/bootstrap.min.js')
def _httpHandler_getbootstrap(httpClient, httpResponse):
    httpResponse.WriteResponseFile('www/js/bootstrap.min.js', contentType='text/javascript')

@MicroWebSrv.route('/ajax_start.pyhtml')
def _httpHandler_start(httpClient, httpResponse):
    gapp.start()
    httpResponse.WriteResponseJSONOK(obj=None, headers=None)

@MicroWebSrv.route('/ajax_stop.pyhtml')
def _httpHandler_stop(httpClient, httpResponse):
    gapp.stop()
    httpResponse.WriteResponseJSONOK(obj=None, headers=None)

@MicroWebSrv.route('/ajax_start_one_portion.pyhtml')
def _httpHandler_stop(httpClient, httpResponse):
    gapp.start_one_portion()
    httpResponse.WriteResponseJSONOK(obj=None, headers=None)

@MicroWebSrv.route('/ajax_weight.pyhtml')
def _httpHandler_ajax_weight(httpClient, httpResponse):
    httpResponse.WriteResponseJSONOk(obj=str(gapp.waage.get_tared_weight()), headers=None)


def startWebServer():
    mws = MicroWebSrv()
    mws.SetNotFoundPageUrl('/notfound')
    mws.Start(threaded=True)
    return mws
