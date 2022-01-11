
def txt_logger(check):
    """Декоратор для сохранения логов в logs.txt."""

    def wrapper(*args):
        check_result, class_var = check(*args)
        text = ''
        if class_var == 'check':
            if check_result:
                text = f'{args[1]} in blacklist.\n'
            if not check_result:
                text = f'{args[1]}  not in blacklist.\n'
        elif class_var == 'add':
            if check_result:
                text = f'{args[1]} added in blacklist.\n'
            if not check_result:
                text = f'{args[1]} cannot be added, because already in blacklist.\n'
        elif class_var == 'update':
            if check_result:
                text = f'Updated {args[1]} expire date : {args[2]}.\n'
            if not check_result:
                text = f'{args[1]} cannot be found in blacklist.\n'
        elif class_var == 'update del':
            text = f'{args[1]} deleted from blacklist.\n'
        elif class_var == 'del':
            if check_result:
                text = f'{args[1]} successfully deleted from blacklist.\n'
            if not check_result:
                text = f'{args[1]} cannot be found in blacklist.\n'
        elif class_var == 'fullname':
            if check_result:
                text = f'{args[1]} valid name, full_name.\n'
            if not check_result:
                text = f'{args[1]} not valid name, full_name.\n'
        elif class_var == 'phone':
            if check_result:
                text = f'{args[1]} is valid phone-number.\n'
            else:
                text = f'{args[1]} is not valid phone-number.\n'
        elif class_var == 'date':
            if check_result:
                text = f'{args[1]} is not valid date.\n'
        with open('logs.txt', 'a') as logs:
            logs.write(text)
        return check_result
    return wrapper
