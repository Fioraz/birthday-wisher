##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)
PLACEHOLDER = "[NAME]"
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "abcdefghijklmnop"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    name = birthday_dict[today]["name"]
    email_address = birthday_dict[today]["email"]

    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_format = letter.read().replace(PLACEHOLDER, name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_address,
            msg=f"Subject: Happy Birthday!\n\n{letter_format}"
        )



