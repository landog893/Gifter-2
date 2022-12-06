from account_info import AccountInfo
from datetime import datetime, timedelta
import smtplib
import ssl
from item import item
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st


# This class represents an account object that a user creates to interact with the code.
class Account:
    def __init__(
        self,
        name="",
        surname="",
        birthday="",
        email="",
        notifications="",
        username="",
        password="",
        interests="",
        wishlist="",
        friendlist="",
        ID=None,
    ):
        if ID is not None:
            accountMan = AccountInfo()
            info = accountMan.get_info(ID)
            if info:
                self.name = info[0]
                self.surname = info[1]
                self.birthday = info[2]
                self.email = info[3]
                self.notifications = info[4]
                self.username = info[5]
                self.password = info[6]
                self.interests = info[7]
                self.wishlist = info[8]
                self.friendlist = info[9]
                self.ID = ID
            else:
                raise ValueError
        else:
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.email = email
            self.notifications = notifications
            self.username = username
            self.password = password
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            acc = self.create_account()
            print(acc)
            if not acc:
                st.error("Registration failed, please try again!")
                self.ID = -2
            else:
                self.ID = acc[0]
                print(self.ID)

    def create_account(self):
        accountMan = AccountInfo()
        acc = accountMan.create_account(
            self.name,
            self.surname,
            self.birthday,
            self.email,
            self.notifications,
            self.username,
            self.password,
            self.interests,
            self.wishlist,
            self.friendlist,
        )
        return acc

    # This method pulls the account to allow the user the view information.
    def view_account(self):
        accountMan = AccountInfo()
        return accountMan.get_info(self.ID)

    def update_account(
        self,
        name="",
        surname="",
        birthday="",
        email="",
        notifications="",
        username="",
        password="",
        interests="",
        wishlist="",
        friendlist="",
    ):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = email
        self.notifications = notifications
        self.username = username
        self.password = password
        self.interests = interests
        self.wishlist = wishlist
        self.friendlist = friendlist
        accountMan = AccountInfo()
        accountMan.update_account(
            self.ID,
            name,
            surname,
            birthday,
            email,
            notifications,
            username,
            password,
            interests,
            wishlist,
            friendlist,
        )

    # This method is used to send birthday reminder emails if a user has their email notification
    # preferences on. The method loops through the friends list, and if the friend has their email
    # preferences on as well, an email is sent using SMTP. The method runs every time the program is
    # loaded (checks if the birthday is in 1 week) or when the user clicks the "Send Notification" button
    # in the profile.
    def send_reminder_email(self):
        name = self.name
        birthday = self.birthday
        print(birthday)
        b = birthday.rpartition("/")[0] + birthday.rpartition("/")[1]
        b = b[:-1]

        friendlist = self.friendlist
        friendl = friendlist.split(",")
        friendobj = [Account(ID=int(f)) for f in friendl if f.isnumeric()]

        items = (self.wishlist).replace('"', "").split(",")
        items = [int(item) for item in items if item.isnumeric()]
        item_objs = [item(ID=id) for id in items]

        notifications = self.notifications
        port = 587
        smtp_server = "smtp.office365.com"
        sender_email = "gifter-2@outlook.com"
        password = "G1ft3r#212!"

        if notifications == "Off":
            print("Please turn email notifications on.")
        elif password == "REPLACE":
            print(
                "Please replace the password field with your Outlook account's password."
            )
        else:
            # construct wishlist string
            wishlistString = "\n"
            for i in item_objs:
                wishlistString += (
                    " - " + i.title + " ($" + str(i.cost) + "): " + i.link + "\n"
                )

            message = (
                """Buy """
                + name
                + """ the perfect gift for their birthday on """
                + b
                + """.\nHere are some items on their wishlist:\n """
                + wishlistString
            )

            for friend in friendobj:
                if friend.notifications == "On":
                    receiver_email = friend.email
                    msg = MIMEMultipart()
                    msg["Subject"] = "Gifter-2: " + name + "'s Birthday is Coming Up"
                    msg["From"] = sender_email
                    msg["To"] = receiver_email

                    body = MIMEText(message, "plain")
                    msg.attach(body)

                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.ehlo()
                        server.login(sender_email, password)
                        print("logged in")
                        print("attempting to send mail")
                        server.sendmail(sender_email, receiver_email, msg.as_string())
                        print("message sent")
                        server.quit()
