from pyramid.authentication import AuthTktCookieHelper
from pyramid.authorization import (
    ACLHelper,
    Authenticated,
    Everyone,
)

from pyramid.csrf import CookieCSRFStoragePolicy
from pyramid.request import RequestLocalCache

from . import models

class MySecurityPolicy:
    def __init__(self, secret):
        print("in __init__")
        self.authtkt = AuthTktCookieHelper(secret)
        self.identity_cache = RequestLocalCache(self.load_identity)
        self.acl = ACLHelper()

    def load_identity(self, request):
        print("in load_identity")
        identity = self.authtkt.identify(request)
        print(identity)
        if identity is None:
            print("identity is none")
            return None

        userid=identity['userid']
        print("loadidentity: ")
        print(userid)
        if(userid is not None):
            return userid

    def identity(self, request):
        print("in identity func")
        return self.identity_cache.get_or_create(request)

    def authenticated_userid(self, request):
        print("in authenticated_userid func")
        user = self.load_identity(request)
        if user is not None:
            print("user was not none " + user)
            return user

    def remember(self, request, userid, **kw):
        print("in remember func")
        return self.authtkt.remember(request, userid, **kw)

    def forget(self, request, **kw):
        return self.authtkt.forget(request, **kw)

def includeme(config):
    settings = config.get_settings()
    config.set_csrf_storage_policy(CookieCSRFStoragePolicy())
    config.set_default_csrf_options(require_csrf=True)
    config.set_security_policy(MySecurityPolicy(settings['auth.secret']))
