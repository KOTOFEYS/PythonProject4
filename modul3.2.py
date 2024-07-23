def send_mail(message, recipient, *, sender):
    if '@' not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if '@' not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if (all(x not in recipient for x in ['.com', '.net', '.ru'])):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if (all(x not in sender for x in ['.com', '.net', '.ru'])):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')





