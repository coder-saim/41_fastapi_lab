def individual_seriallizer_user(user) -> dict:
    return {
        'id': str(user['_id']),
        'username': user['username'],
        'email': user['email'],
        'password': user['password'],
        'phone': str(user['phone'])
    }


def list_seriallizer_user(users) ->  list:
    return [individual_seriallizer_user(user) for user in users]