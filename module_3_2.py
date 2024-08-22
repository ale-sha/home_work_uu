def send_email(message, recipient, *, sender='university.help@gmail.com'):
    simbol = (".com", ".ru", ".net")
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if not (recipient.__contains__('@') and sender.__contains__('@')
            and any(map(recipient.endswith, simbol)) and any(map(sender.endswith, simbol))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"Письмо успешно отправлено c адреса {sender} на адрес {recipient}")


send_email('jnjnj', 'hpm@ail.ru')
send_email('jnjnj', 'mail.ru')
send_email('jnjnj', 'university.help@gmail.com')
send_email('jnjnj', 'pm@ail.hgh')
send_email('jnjnj', 'university.hpm@ail.ru', sender='univerity.help@gmail.com')