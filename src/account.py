from account_info import AccountInfo
from datetime import datetime, timedelta
import smtplib, ssl
from item import item
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# This class represents an account object that a user creates to interact with the code.
class Account():
    # Initialization of an account object.
    def __init__(self, name='', surname='', birthday='', email='', notifications='', interests='', wishlist='', friendlist='', ID = None):
        if ID != None:
            accountMan = AccountInfo()
            info = accountMan.get_info(ID)
            self.name = info['Name']
            self.surname = info['Surname']
            self.birthday = info['Birthday']
            self.email = info['Email']
            self.notifications = info['Notifications']
            self.interests = info['Interests']
            self.wishlist = info['WishList']
            self.friendlist = info['FriendList']
            self.ID = ID
        else: 
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.email = email
            self.notifications = notifications
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            self.ID = self.create_account()['ID']

    # This method creates an account. 
    def create_account(self):
        accountMan = AccountInfo()
        acc = accountMan.create_account(self.name, self.surname, self.birthday, self.email, self.notifications, self.interests, self.wishlist, self.friendlist)
        return acc
    
    # This method pulls the account to allow the user the view information. 
    def view_account(self):
        accountMan = AccountInfo()
        return accountMan.get_info(self.ID)

    # This method is used to update the account based on the supplied information. Input validation
    # occurs on the frontend. 
    def update_account(self, name='', surname='', birthday='', email='', notifications='', interests='', wishlist='', friendlist=''):
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.email = email
            self.notifications = notifications
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            accountMan = AccountInfo()
            accountMan.update_account(self.ID, name, surname, birthday, email, notifications, interests, wishlist, friendlist)
    
    # This method is used to send birthday reminder emails if a user has their email notification
    # preferences on. The method loops through the friends list, and if the friend has their email
    # preferences on as well, an email is sent using SMTP. The method runs every time the program is
    # loaded (checks if the birthday is in 1 week) or when the user clicks the "Send Notification" button
    # in the profile.
    def send_reminder_email(self):
            accountMan = AccountInfo()
            info = accountMan.get_info(self.ID)

            name = info['Name']
            birthday = info['Birthday'].item()
            b = birthday.rpartition('/')[0] + birthday.rpartition('/')[1]
            b = b[:-1]
            friendlist = info['FriendList'].to_string(index=False)
            friendl = friendlist.split(',')
            friendobj = [Account(ID=int(f)) for f in friendl]

            wishlist = info['WishList'].to_string(index=False)
            items = wishlist.replace("\"", "").split(",")
            items = [int(item) for item in items]
            item_objs = [item(ID=int(id)) for id in items]
    
            notifications = info['Notifications'].item()               

            if (notifications == "Off"):
                print("Please turn email notifications on.")
            else:
                port = 587 
                smtp_server = "smtp.office365.com"
                sender_email = "gifter-2@outlook.com"
                password = "G1ft3r#212!"

                # construct wishlist string
                wishlistString = "\n"
                for i in item_objs:
                    wishlistString += " - " + i.title.item() + " ($" + i.cost.item() + "): " + i.link.item() + "\n"
                
                message = """Buy """ + name.item() + """ the perfect gift for their birthday on """ + b + """.\nHere are some items on their wishlist:\n """ + wishlistString

                for friend in friendobj:
                    if (friend.notifications.item() == "On"):
                        receiver_email = friend.email.item()

                        msg = MIMEMultipart()
                        msg['Subject'] = "Gifter-2: " + name.item() + "'s Birthday is Coming Up"
                        msg['From'] = sender_email
                        msg['To'] = receiver_email

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

# #acc = Account('Hannah', 'Montana', '05/05/1995', 'Singing, Dancing')
# #acc.view_account()
# acc = Account(ID=1)
# ints = (acc.interests.to_string(index=False)).replace("\"", "")
# ints += ", Ballet"
# # print(ints)
# wishes = (acc.wishlist.to_string(index=False))
# acc.update_account(acc.name.to_string(index=False), acc.surname.to_string(index=False), acc.birthday.to_string(index=False), ints, acc.wishlist.to_string(index=False), acc.friendlist.to_string(index=False))

        