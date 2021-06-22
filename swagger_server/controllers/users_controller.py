import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def users_get():  # noqa: E501
    """Lista de usuários

    \&quot;Este endpoint retorna uma lista com **todos** os usuários cadastrados no sistema\&quot;  # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_id_delete(id):  # noqa: E501
    """Apaga um usuário

    Este endpoint apaga **apenas um** usuário através do id fornecido  # noqa: E501

    :param id: id do usuário
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def users_id_get(id):  # noqa: E501
    """Mostra apenas um usuário

    Este endpoint mostra **apenas um** usuário através do id fornecido  # noqa: E501

    :param id: id do usuário
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def users_patch(user):  # noqa: E501
    """Atualiza um usuário

    Este endpoint atualiza um usuário no sistema (O id deve ser informado)  # noqa: E501

    :param user: Usuário enviado
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_post(user):  # noqa: E501
    """Cria um usuário

    Este endpoint cadastra um usuário no sistema # noqa: E501

    :param user: Usuário enviado
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_put(user):  # noqa: E501
    """Atualiza um usuário

    Este endpoint atualiza um usuário no sistema (O id deve ser informado)  # noqa: E501

    :param user: Usuário enviado
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
