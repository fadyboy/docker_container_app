#!/usrs/bin/env python3
#-*- coding:UTF-8 -*-

import json
from dashboard.tests.base import BaseTestCase


class TestUsersService(BaseTestCase):
    """ Tests for the Users Service """


    def test_users(self):
        """ Ensure the /ping route behaves correctly """
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is another test message', data['message'])
        self.assertIn('success', data['status'])


    def test_add_user(self):
        """ Ensure a new user can be added to the database """
        with self.client:
            response = self.client.post(
                '/users',
                data = json.dumps(dict(
                    username = "Anthonyf",
                    email = "anthonyf@mycom.com"
                )),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn("anthonyf@mycom.com was added", data["message"])
            self.assertIn("success", data["status"])


    def test_add_user_invalid_json(self):
        """ Ensure error is thrown if the JSON object is empty """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type="application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400) # invalid request params
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])


    def test_duplicate_user(self):
        """ Check that duplicate user not created """

        with self.client:
            self.client.post(
                '/users',
                data=json.dumps(dict(
                    username="anthonyf",
                    email="anthonyf@mycom.com"
                )),
                content_type="application/json"
            )
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username="anthonyf",
                    email="anthonyf@mycom.com"
                )),
                content_type="application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Sorry. That email already exists.", data["message"])
            self.assertIn("fail", data["status"])


    def test_add_user_invalid_json_keys(self):
        """ Ensure error is thrown if the JSON object does not have a username key. """

        with self.client:
            self.client.post(
                '/users',
                data=json.dumps()
            )