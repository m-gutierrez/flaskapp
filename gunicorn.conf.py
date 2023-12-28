import multiprocessing
import os



wsgi_app = "run:app"
bind = "localhost:8000"
workers = multiprocessing.cpu_count() * 2 + 1
#keyfile = os.environ.get('WEB_KEY')
#certfile = os.environ.get('WEB_CERT')


#accesslog = '/var/log/flaskapp/access.log'
#errorlog = '/var/log/flaskapp/error.log'

#disable_redirect_access_to_syslog = True
