from behave import *
from hamcrest import *
from code.request import Request
import requests as req

use_step_matcher("re")


@given('step "(?P<desc>.+)"')
def step_impl(context, desc):
    """
    :type context: behave.runner.Context
    :type desc: str
    """
    pass


@when('Vasiliy (?P<method>.+) url "(?P<url>.+)" with params "(?P<params>.*)"')
def step_impl(context, method, url, params):
    """
    :type context: behave.runner.Context
    :type method: str
    :type url: str
    """
    method = method.lower()
    r = Request(url)
    r = r.get(params)
    assert_that(r.status_code, equal_to(req.codes.ok),
        'Error. server return code "%d"' % r.status_code
    )
    if 200 != r.status_code:
        print(context.scenario.steps)
        # context.scenario.steps.fail('server return code "%"' % r.status_code)

    assert True


@then('server response data according schema "(?P<schema>.+)"')
def step_impl(context, schema):
    """
    :type context: behave.runner.Context
    :type schema: str
    """
    pass
