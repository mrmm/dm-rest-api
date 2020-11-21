from .common import *

DEBUG = True
ALLOWED_HOSTS= ["*"]
# Redis server informations
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 0))
REDIS_URL = "redis://%s:%s"%(REDIS_HOST, REDIS_PORT)

REDIS_CONNECTION = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

ACCESS_LOGS_CONFIG = {
    "MAX_BODY_SIZE": 5*1024,
    "DEBUG_REQUESTS": [],
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '(message) (asctime) (levelname) (module) (filename) (funcName) (pathname)',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'json': {
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.advanced_access_logs': {
            'level': 'INFO',
            'handlers': ['json'],
            'propagate': False,
        },
    },
}
