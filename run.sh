#!/bin/bash
set -e

FLASK_DEBUG=1 FLASK_APP=/usr/local/bin/main.py flask run --host 0.0.0.0
