from multiprocessing import cpu_count

wsgi_app = "run:app"
bind = "localhost:8000"
workers = cpu_count() * 2 + 1
accesslog = '/var/log/flaskapp/access.log'
errorlog = '/var/log/flaskapp/error.log'
disable_redirect_access_to_syslog = True