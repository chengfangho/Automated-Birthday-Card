import pandas
import smtplib
import random
from datetime import datetime

username = "YOUR EMAIL"
password = "YOUR APP PASSWORD"

data = pandas.read_csv("birthdays.csv")
today = (datetime.now().month, datetime.now().day)

birthdays = { (row["month"], row["day"]) :row for (index, row) in data.iterrows()}
if today in birthdays:
    birthday_person = birthdays[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        template = file.read().replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=username, msg=f"Subject:Happy Birthday!\n\n{template}")


