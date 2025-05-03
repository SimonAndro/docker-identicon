#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec python "docker_hello.py"
else
    echo "Running Production Server"
     exec gunicorn -b 0.0.0.0:9090 docker_hello:app
fi