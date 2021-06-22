# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_users_get(self):
        """Test case for users_get

        Lista de usuários
        """
        response = self.client.open(
            '/v1/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_delete(self):
        """Test case for users_id_delete

        Apaga um usuário
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_get(self):
        """Test case for users_id_get

        Mostra apenas um usuário
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_patch(self):
        """Test case for users_patch

        Atualiza um usuário
        """
        user = User()
        response = self.client.open(
            '/v1/users',
            method='PATCH',
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Cria um usuário
        """
        user = User()
        response = self.client.open(
            '/v1/users',
            method='POST',
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_put(self):
        """Test case for users_put

        Atualiza um usuário
        """
        user = User()
        response = self.client.open(
            '/v1/users',
            method='PUT',
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
