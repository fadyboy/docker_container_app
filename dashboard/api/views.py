#!/usr/bin/env python3
#-*- coding:UTF-8 -*-


from flask import Blueprint, jsonify, request, make_response
from dashboard import db
from dashboard.api.models import User

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route("/ping", methods=["GET"])
def ping():
    return jsonify({
    "status":"success",
    "message":"This is another test message"
})


@users_blueprint.route("/users", methods=["POST"])
def add_user():
    post_data = request.get_json()
    username = post_data.get('username')
    email = post_data.get('email')
    db.session.add(User(username=username, email=email))
    db.session.commit()
    response_object = {
        "status": "success",
        "message": f"{email} was added!"
    }

    return make_response(jsonify(response_object)), 201