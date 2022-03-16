from pyramid.csrf import new_csrf_token
from pyramid.httpexceptions import (
    HTTPSeeOther,
    HTTPFound,
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


@view_config(route_name='login_en', renderer='pyramidmre:templates/login-en.jinja2')
def login(request):
    next_url = request.route_url('main_en')
    message = ''
    login = ''
    if(request.method == 'POST'):
        login = request.params['login'] #This is the html element for the username
        password = request.params['password'] #Password
        user = (
            request.dbsession.query(models.CustomerUsers)
            .filter_by(USERNAME_EMAIL=login)
            .first() #Find user in db
        )
        if user is not None and user.check_password(password): #If user is in db
            headers = remember(request, user.USER_ID) #remember them
            return HTTPFound(location=next_url, headers=headers) #redirect them
        message = 'Failed login' #bad credentials
        request.response.status = 400

    return dict(
        message=message,
        url=request.route_url('login_en'),
        next_url=next_url,
        login=login,
    )

# @view_config(route_name='logout')
# def logout(request):
#     next_url = request.route_url('login_en')
#     if request.method == 'POST':
#         headers = forget(request)
#         return HTTPSeeOther(location=next_url, headers=headers)

#     return HTTPSeeOther(location=next_url)

