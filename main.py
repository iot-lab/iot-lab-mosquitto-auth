"""Mosquitto HTTP auth backend."""

import os
import json
import logging

import requests

from flask import Flask, request, Response, abort


app = Flask(__name__.split(".")[0])
app.config["DEBUG"] = True


API_URL = os.getenv("API_URL", "https://www.iot-lab.info/api")


@app.route("/user", methods=["POST"])
def user():
    """Check user credentials."""
    app.logger.info(f"user request from {request.environ['REMOTE_ADDR']}")

    try:
        data = json.loads(request.data.decode())
    except:
        return Response('{"OK": false}')

    username = data["username"]
    password = data["password"]

    try:
        req = requests.get(f"{API_URL}/user", auth=(username, password))
        ret = "true" if req.status_code == 200 else "false"
    except:
        ret = "false"

    if ret == "true":
        app.logger.info(f"Connection accepted for user '{username}'")
    else:
        app.logger.info(f"Connection refused for user '{username}'")

    return Response(f'{{"OK": {ret}}}')


@app.route("/acls", methods=["POST"])
def acls():
    """Check acls."""
    app.logger.info(f"acl request from {request.environ['REMOTE_ADDR']}")

    try:
        data = json.loads(request.data.decode())
    except:
        return Response('{"OK": false}')

    username = data["username"]
    topic = data["topic"]

    ret = "false" 
    if topic.startswith(f"iotlab/{username}") or\
        topic.startswith(f"localisation/") :
        ret = "true"
    if ret == "true":
        app.logger.info(
            f"ACL accepted for user '{username}' on topic '{topic}'"
        )
    else:
        app.logger.info(
            f"ACL rejected for user '{username}' on topic '{topic}'"
        )

    return Response(f'{{"OK": {ret}}}')
