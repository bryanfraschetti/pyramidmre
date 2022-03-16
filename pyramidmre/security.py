from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .models import Customers,CustomerUsers

class pyramidmreAuthPol(AuthTktAuthenticationPolicy):
    def authenticated_userid(self, request):
        user = request.user
        if user is not None:
            return user.USER_ID
    
def get_user(request):
    customer_id = request.unauthenticated_userid
    if customer_id is not None:
        customer = request.dbsession.query(Customers).get(customer_id)
        if ('login' in request.params and customer is not None):
            user_id = request.params['login']
            if user_id is not None:
                user = request.dbsession.query(CustomerUsers).get(customer.CUST_ID, user_id)
            return user

def includeme(config):
    settings = config.get_settings()
    authn_policy = pyramidmreAuthPol(
        settings['auth.secret'],
        hashalg='sha512',
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, 'user', reify=True)
