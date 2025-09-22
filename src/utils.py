from flask import jsonify


def make_response(message=None, data=None, status=200):
    payload = {}
    if message:
        payload["message"] = message
    if data is not None:
        payload["data"] = data
    return jsonify(payload), status
