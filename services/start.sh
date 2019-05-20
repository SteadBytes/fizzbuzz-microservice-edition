#!/bin/bash
set -e

if [ "${ENVIRONMENT}" = "dev" ]; then
    python "$1".py
else
    gunicorn --bind 0.0.0.0:5000 "$1":app
fi