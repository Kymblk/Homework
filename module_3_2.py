def send_email(message, recipient, *, sender='university.help@gmail.com'):
    is_true = True
    lst1 = ['.com', '.ru', '.net']  # Список для проверки окончания почты

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        is_true = False

    elif '@' not in recipient or '@' not in sender:     # Проверка на наличие '@' в переменных sender и recipient
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        is_true = False

    elif not any(i in recipient for i in lst1) or not any(i in sender for i in lst1):   # Проверка на наличие хотя бы одного элемента из списка lst1 в переменных sender и recipient
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        is_true = False

    elif is_true:       # Если хотя бы один print() выше сработал, то данный блок не будет работать
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешо отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
