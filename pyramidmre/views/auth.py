from pyramid.httpexceptions import (
    HTTPSeeOther,
    HTTPForbidden,
)

from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    forbidden_view_config,
    view_config,
)

from .. import models

@view_config(route_name='main_en', renderer='pyramidmre:templates/main-en.jinja2')
def main_en(request):
    print("in main")
    print(request.__dir__())
    print(request.is_authenticated)
    print("Identity of user: ")
    print(request.authenticated_userid)
    userid=request.authenticated_userid
    if userid is None:
        raise HTTPForbidden
    message = ''
    return dict(message=message)

@forbidden_view_config(renderer='pyramidmre:templates/403.jinja2')
def forbidden_view(exc, request):
#    if not request.is_authenticated:
 #       next_url = request.route_url('login_en', _query={'next': request.url})
  #      return HTTPSeeOther(location=next_url)

    request.response.status = 403
    return {}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
