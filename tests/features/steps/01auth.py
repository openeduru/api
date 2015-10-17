# -*- coding: utf-8 -*-

from behave import *
from hamcrest import *
import requests as request

use_step_matcher("re")


@given("any user wants to be Vasiliy")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # pass
    context.scenario.skip(reason=u"в документации не определена процедура авторизации")


@when("request (?P<url>.+) with login (?P<login>.+) and password (?P<password>.+)")
def step_impl(context, url, login, password):
    """
    :type context: behave.runner.Context
    """
    pass


@then('server returns username "(?P<username>.+)" & role "(?P<role>.+)"')
def step_impl(context, username, role):
    """
    :type context: behave.runner.Context
    :type username: str
    :type role: str
    """
    pass
