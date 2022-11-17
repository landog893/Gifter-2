from account_info import AccountInfo
from datetime import datetime, timedelta
import smtplib, ssl

class Account():
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
        

    def create_account(self):
        accountMan = AccountInfo()
        acc = accountMan.create_account(self.name, self.surname, self.birthday, self.email, self.notifications, self.interests, self.wishlist, self.friendlist)
        return acc
    
    def view_account(self):
        accountMan = AccountInfo()
        return accountMan.get_info(self.ID)

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

    def send_reminder_email(self):
            accountMan = AccountInfo()
            info = accountMan.get_info(self.ID)

            name = info['Name']
            birthday = info['Birthday']
            email = info['Email']
            friendlist = info['FriendList'].to_string(index=False)
            friendl = friendlist.split(',')
            friendobj = [Account(ID=int(f)) for f in friendl]
            wishlist = info['WishList'].to_string(index=False)
            notifications = info['Notifications'].item()

            if (notifications == "Off"):
                print("Please turn email notifications on.")
            else:
                # birthdayDate = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
                # currDate = datetime.datetime.now().date()
                # if (birthdayDate - currDate).days < 7: 
                    port = 587 
                    smtp_server = "outlook.office365.com"
                    sender_email = email
                    password = 'G1ft3r#212!'
                    for friend in friendobj:
                        print(friend.name)
                        # if (friend.notifications.item() == "On"):
                        #     print(friend.email)
                        #     receiver_email = friend.email
                        #     message = """\
                        #     Subject: """ + name + """'s Birthday is Coming Up

                        #     Buy """ + name + """ the perfect gift for their birthday on """ + birthday + """.
                        #     Here are some items on their wishlist: """ + wishlist + """."""
                            
                            # context = ssl.create_default_context()
                            # with smtplib.SMTP(smtp_server, port) as server:
                            #     server.ehlo()  # Can be omitted
                            #     server.starttls(context=context)
                            #     server.ehlo()  # Can be omitted
                            #     server.login(sender_email, password)
                            #     server.sendmail(sender_email, receiver_email, message)


# #acc = Account('Hannah', 'Montana', '05/05/1995', 'Singing, Dancing')
# #acc.view_account()
# acc = Account(ID=1)
# ints = (acc.interests.to_string(index=False)).replace("\"", "")
# ints += ", Ballet"
# # print(ints)
# wishes = (acc.wishlist.to_string(index=False))
# acc.update_account(acc.name.to_string(index=False), acc.surname.to_string(index=False), acc.birthday.to_string(index=False), ints, acc.wishlist.to_string(index=False), acc.friendlist.to_string(index=False))

        