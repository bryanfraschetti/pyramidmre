def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login_en', '/login-en')
    config.add_route('main_en', '/main-en')

