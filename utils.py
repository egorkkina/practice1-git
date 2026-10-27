def greet(name):
    """Приветствие пользователя"""
    return f"Здравствуйте, {name}!"


def farewell(name):
    """Прощание с пользователем"""
    return f"До свидания, {name}!"


def get_name_length(name):
    """Возвращает количество символов в имени пользователя"""
    return len(name)


def get_initials(name, surname):
    """Возвращает инициалы пользователя по имени и отчеству"""
    return f"{name[0].upper()}.{surname[0].upper()}."