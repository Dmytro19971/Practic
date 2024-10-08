def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'safonovdima2@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'safonovdima2@gmail.com', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре 26 сентября', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
