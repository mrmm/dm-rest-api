"""
Gunicorn configuration file (all arguments can be overriden by passing CLI
arguments with similar names (maybe underscores become dashes but that's all)
"""
# Source IPs to accept
bind = ["0.0.0.0:8000"]
forwarded_allow_ips = "*"

# Backend timeout
timeout = 30

# DEBUG: TO BE REMOVED
access_logfile = "/dev/stdout"

# Graceful termination timeout (should simply be higher than the maximum
# request processing time, here, log uploads of say... five minutes)
graceful_timeout = 310

# Number of worker processes
worker_class = 'gevent'

# This will result in using x number of thread per worker to process requests
# (default 1)
threads = 2

# Max count of simultaneaous connections (default 1000)
worker_connections = 1000

# Maximum number of pending connections
backlog = 1024

# Maximum number of requests a worker will process before restarting
max_requests = 8192

# Randomize restarts by +/- a certain amount to prevent workers from restarting
# at the same time
max_requests_jitter = 512

# Preload the application code before worker processes are forked (decreases
# RAM consumption a bit)
preload = True

loglevel = "debug"
caputure_output = True

# FIXME delete these hooks after resolving the restart problem of gunicorn
REQUETS_COUNTER = {}
