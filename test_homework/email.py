from datetime import datetime

# 1. Создайте словарь email
email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "lead_dev@icloud.com ",
    "body": (
        "Hello,\n"
        "We are interested in a partnership.\t"
        "Please reply soon.\n"
        "Regards,\n"
        "Team"
    ),
}

# 2. Добавьте дату отправки
send_date = datetime.now().strftime("%Y-%m-%d")
email5["date"] = send_date

# 3. Нормализуйте e-mail адреса
email5["from"] = email5["from"].strip().lower()
email5["to"] = email5["to"].strip().lower()

# 4. Извлеките логин и домен отправителя
login, domain = email5["from"].split("@")

# 5. Создайте сокращённую версию текста
email5["short_body"] = email5["body"][:10] + "..."

# 6. Списки доменов
personal_domains = list(
    {
        "gmail.com",
        "list.ru",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "icloud.com",
        "yandex.ru",
        "mail.ru",
        "list.ru",
        "bk.ru",
        "inbox.ru",
    }
)

corporate_domains = list(
    {
        "company.ru",
        "corporation.com",
        "university.edu",
        "organization.org",
        "company.ru",
        "business.net",
    }
)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
no_common_domains = set(personal_domains).isdisjoint(set(corporate_domains))
assert no_common_domains

# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains

# 9. Соберите «чистый» текст сообщения
email5["clean_body"] = email5["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма
email5["sent_text"] = f"""Кому: {email5["to"]}, от {email5["from"]}
Тема: {email5["subject"]}, дата {email5["date"]}
{email5["clean_body"]}"""

# 11. Рассчитайте количество страниц печати
pages = (len(email5["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма
is_subject_empty = not email5["subject"].strip()
is_body_empty = not email5["body"].strip()

# 13. Создайте «маску» e-mail отправителя
email5["masked_from"] = login[:2] + "***@" + domain

# 14. Удалите из списка личных доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

print(email5)
print(no_common_domains, is_corporate, pages, is_subject_empty, is_body_empty)
print(personal_domains)
