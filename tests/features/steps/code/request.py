import requests as req
import uritools
import posixpath

OPENEDU_API_BASEPATH = "http://api.dev.npoed.ru"


class Request(object):

    """docstring for request"""

    def __init__(self, url):
        super(Request, self).__init__()
        global OPENEDU_API_BASEPATH

        self.url = OPENEDU_API_BASEPATH + url
        # self.url = "http://api.dev.npoed.ru" + url

    def get(self, params: str):
        if type(params) is str:
            self.url += params

        # else:
        #     if type(params) == type([]):
        #         params = params.join()

        return req.get(self.url)

    def _urlnormalize(self, url):
        n = uritools.urisplit(url)
        n.path = posixpath.normpath(n.path)
        return uritools.uriunsplit(n).geturl()

