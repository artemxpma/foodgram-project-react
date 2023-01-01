def check_input(username, email):
    """Проверяет, введен ли емейл и что длина имени больше 2 символов."""
    if not email:
        raise ValueError('Enter email address')
    if len(username) < 3:
        raise ValueError('Username is too short')
