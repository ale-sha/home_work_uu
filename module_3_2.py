def send_email(message, recipient, *, sender='university.help@gmail.com'):
    simbol = [".com", ".ru", ".net"]
    count = 0
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        if recipient.__contains__('@') and sender.__contains__('@'):
            for i in range(len(simbol)):
                if count < 2:
                    if recipient.__contains__(simbol[i]) == sender.__contains__(simbol[i]) == True:
                        count += 1
                    elif recipient.__contains__(simbol[i]) or sender.__contains__(simbol[i]):
                        count += 1
                    else:
                        continue
            if count == 2:
                if sender != 'university.help@gmail.com':
                    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
                else:
                    print(f"Письмо успешно отправлено c адреса {sender} на адрес {recipient}")
            else:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('jnjnj', 'hpm@ail.ru')
send_email('jnjnj', 'mail.ru')
send_email('jnjnj', 'university.help@gmail.com')
send_email('jnjnj', 'pm@ail.hgh')
send_email('jnjnj', 'university.hpm@ail.ru', sender='univerity.help@gmail.com')