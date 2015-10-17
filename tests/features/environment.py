
from behave import *
# from WellBehavedPython.api import *
from hamcrest import *
# from hamcrest import assert_that, equal_to

from selenium import webdriver
import requests as request


OPENEDU_API_BASEPATH = "http://api.dev.npoed.ru"


'''Общее описание
'''

def before_feature(context, feature):
    context.OPENEDU_API_BASEPATH = "http://api.dev.npoed.ru"
    pass
    # model.init(environment='test')
    # if 'browser' in feature.tags:
    #     context.server = simple_server.WSGIServer(('', 8000))
    #     context.server.set_app(web_app.main(environment='test'))
    #     context.thread = threading.Thread(target=context.server.serve_forever)
    #     context.thread.start()
    #     context.browser = webdriver.Chrome()

def after_feature(context, feature):
    pass
    # if 'browser' in feature.tags:
    #     context.server.shutdown()
    #     context.thread.join()
    #     context.browser.quit()

# -- FILE: features/environment.py
# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)

BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    setup_debug_on_error(context.config.userdata)

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)
