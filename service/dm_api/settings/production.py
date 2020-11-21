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
INSTALLED_APPS.extend(['health_check', 'health_check.contrib.redis'])

# MIDDLEWARE.insert(0, 'django_access_logger.AccessLogsMiddleware')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)-5.5s] %(message)s'
        },
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '(message) (asctime) (levelname) (module) (filename) (funcName) (pathname)',
        },
    },
    'handlers': {
        'mycustomlogfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'development.log',
            'level': 'DEBUG',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 2,
            'encoding': 'utf-8'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.advanced_access_logs': {
            'level': 'DEBUG',
            'handlers': ['mycustomlogfile'],
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['mycustomlogfile'],
        },
    },
}
