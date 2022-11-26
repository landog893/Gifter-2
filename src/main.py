
from msilib.schema import ProgId
from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from account import Account
from account_info import AccountInfo
from item import item
from datetime import datetime
import re

email_sent = False

def initial_page():
    st.header("Gift Finder!")
    create = st.button('Create Account') 
    login = st.button('Log In')
    if create:
        st.session_state.runpage = 'createaccount'
        st.experimental_rerun()
    if login:
        st.session_state.runpage = 'login'
        st.experimental_rerun()

def login_page():
    form1 = st.form(key='Login form')
    userID = form1.text_input('UserID: ')
    but = form1.form_submit_button('Log in')
    if but:
        acc = Account(ID=int(userID))
        st.session_state.runpage = 'account'
        st.session_state.account = acc
        st.experimental_rerun()
    
def create_account():
    st.write('Please fill out the form')
    form = st.form(key='Create_form')
    name = form.text_input('Name:')
    surname = form.text_input('Surname:')
    birthday = form.text_input('Birthday (MM/DD/YYYY):')
    email = form.text_input('Email:')
    notifications = form.text_input('Email notifications (enter On or Off):')
    interest = form.text_input('Interests (please enter them comma seperated):')
    but1 = form.form_submit_button('Submit')

    # check if birthday is valid format
    format = "%m/%d/%Y"
    validB = True
    try:
        validB = bool(datetime.strptime(birthday, format))
    except ValueError:
        validB = False

    # check if email is valid format using regex
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    validE = True
    if not (re.fullmatch(regex, email)):
        validE = False
    
    # when create account button is clicked, check input before creating account
    if but1:
        error = False
        errorMessage = ""
        if (name == ""):
            error = True
            errorMessage += "Name cannot be empty.\n"
        if (surname == ""):
            error = True
            errorMessage += "Surname cannot be empty.\n"
        if (birthday == "" or validB == False):
            error = True
            errorMessage += "Birthday should be formatted MM/DD/YYYY.\n"
        if (email == "" or validE == False):
            error = True
            errorMessage += "Please enter a valid email.\n"
        if (notifications == "" or notifications != "On"):
            if (notifications != "Off"):
                error = True
                errorMessage += "Email notifications should be either 'On' or 'Off'.\n"
        # if there is an error, print the associated messages and allow for user to correct
        if (error == True):
            st.error(errorMessage)
        # if there is not an error, create the account
        else:
            acc = Account(name, surname, birthday, email, notifications, interest)
            acc = Account(ID = int(acc.ID))
            st.session_state.runpage = 'account'
            st.session_state.account = acc
            st.experimental_rerun()
    #return account

def account_page():
    acc = st.session_state.account
    st.header('Welcome ' + acc.name.to_string(index=False) + '!')
    st.write("What a beautiful day to gift!")
    if st.button('Profile'):
        st.session_state.runpage = 'profile'
        st.experimental_rerun()
    if st.button('Wishlist'): 
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()
    if st.button('Friendlist'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()
    if st.button('Logout'):
        st.session_state.runpage = 'initial'
        st.experimental_rerun()
    # check if whether a notification email needs to be sent today (is it 1 week before the account's birthday)
    global email_sent

    birthday = acc.birthday.item()
    b = birthday.rpartition('/')[0] + birthday.rpartition('/')[1]
    b = b[:-1]
    month = b.rpartition('/')[0]
    day = b.rpartition('/')[2]
    currDate = datetime.now().date()

    if (int(currDate.month) > int(month)):
        if (int(currDate.day) > int(day)):
            birthdayDate = b + "/" + str(currDate.year + 1)
    else:
        birthdayDate = b + "/" + str(currDate.year)

    birthdayDate = datetime.strptime(birthdayDate, "%m/%d/%Y").date()

    if (birthdayDate - currDate).days == 7 and email_sent == False:
            email_sent = True
            acc.send_reminder_email()
            acc = Account(ID = int(acc.ID))
            st.session_state.account = acc
            st.session_state.runpage = 'profile'
            st.experimental_rerun()
    else:
        email_sent = False

def profile_page():
    st.header('Profile')
    acc = st.session_state.account
    st.write('ID: ' + str(acc.ID))
    st.write('Name: ' + acc.name.to_string(index=False))
    st.write('Surname: ' + acc.surname.to_string(index=False))
    st.write('Birthday: ' + acc.birthday.to_string(index=False))
    st.write('Email: ' + acc.email.to_string(index=False))
    st.write('Email Notifications: ' + acc.notifications.to_string(index=False))
    st.write('Interests: ' + (acc.interests.to_string(index=False)).replace("\"", ""))
    if st.button("Edit Profile"):
        st.session_state.runpage = 'editprofile'
        st.experimental_rerun()
    if st.button("Back"):
        st.session_state.runpage = 'account'
        st.experimental_rerun()
    if st.button("Send Notifications"):
        acc.send_reminder_email()
        st.experimental_rerun()

def editprofile_page():
    st.header('Edit Profile')
    form = st.form(key='EditProfileForm')
    acc = st.session_state.account
    name = form.text_input('Name:', value= acc.name.to_string(index=False), placeholder= acc.name.to_string(index=False))
    surname = form.text_input('Surname:', value= acc.surname.to_string(index=False), placeholder= acc.surname.to_string(index=False))
    birthday = form.text_input('Birthday:', value= acc.birthday.to_string(index=False), placeholder= acc.birthday.to_string(index=False))
    email = form.text_input('Email:', value= acc.email.to_string(index=False), placeholder= acc.email.to_string(index=False))
    notifications = form.text_input('Email Notifications:', value= acc.notifications.to_string(index=False), placeholder= acc.notifications.to_string(index=False))
    ints = (acc.interests.to_string(index=False)).replace("\"", "")
    interests = form.text_input('Interest:', value=ints, placeholder=ints)
    if form.form_submit_button('Update'):
        # check if birthday is valid format
        format = "%m/%d/%Y"
        validB = True
        try:
            validB = bool(datetime.strptime(birthday, format))
        except ValueError:
            validB = False

        # check if email is valid format using regex
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        validE = True
        if not (re.fullmatch(regex, email)):
            validE = False
        
        error = False
        errorMessage = ""
        if (name == ""):
            error = True
            errorMessage += "Name cannot be empty.\n"
        if (surname == ""):
            error = True
            errorMessage += "Surname cannot be empty.\n"
        if (birthday == "" or validB == False):
            error = True
            errorMessage += "Birthday should be formatted MM/DD/YYYY.\n"
        if (email == "" or validE == False):
            error = True
            errorMessage += "Please enter a valid email.\n"
        if (notifications == "" or notifications != "On"):
            if (notifications != "Off"):
                error = True
                errorMessage += "Email notifications should be either 'On' or 'Off'.\n"
        # if there is an error, print the associated messages and allow for user to correct
        if (error == True):
            st.error(errorMessage)
        # if there is not an error, update the account
        else:
            acc.update_account(name, surname, birthday, email, notifications, interests, acc.wishlist.to_string(index=False), acc.friendlist.to_string(index=False))
            acc = Account(ID = int(acc.ID))
            st.session_state.account = acc
            st.session_state.runpage = 'profile'
            st.experimental_rerun()
    if st.button("Back"):
        st.session_state.runpage = 'profile'
        st.experimental_rerun()


def wishlist_page():
    acc = st.session_state.account
    st.header("Your Wishlist")
    items = (acc.wishlist.to_string(index=False))

    if items != 'NaN':
        items = (acc.wishlist.to_string(index=False)).replace("\"", "").split(",")
        items = [int(item) for item in items]
        item_objs = [item(ID=id) for id in items] 
        item_titles = [(i.title.to_string(index=False)).replace("\"", "") for i in item_objs]
        item_descs = [(i.desc.to_string(index=False)).replace("\"", "") for i in item_objs]
        item_links = [(i.link.to_string(index=False).replace("\"", "")) for i in item_objs]
        item_costs = [(i.cost.to_string(index=False).replace("\"", "")) for i in item_objs]

        df = pd.DataFrame(list(zip(items, item_titles, item_descs, item_links, item_costs)), columns=('ID', 'Title', 'Description', 'Link', 'Cost'))
        df.set_index('ID', inplace=True)
        st.table(df)

    if st.button('Add item'):
        st.session_state.runpage = 'additem'
        st.experimental_rerun()
    if st.button('Modify item'):
        st.session_state.runpage = 'modifyitem'
        st.experimental_rerun()
    if st.button('Remove item'):
        st.session_state.runpage = 'deleteitem'
        st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'account'
        st.experimental_rerun()        

def additem_page():
    form = st.form(key='AddItemForm')
    title = form.text_input('Title:')
    desc = form.text_input('Description')
    link = form.text_input('Link')
    cost = form.text_input('Cost')
    if form.form_submit_button('Add item'):
        i = item(title, desc, link, cost)
        acc = st.session_state.account
        a_name = acc.name.to_string(index=False)
        a_surname = acc.surname.to_string(index=False)
        a_birthday = acc.birthday.to_string(index=False)
        a_email = acc.email.to_string(index=False)
        a_interests = acc.interests.to_string(index=False)
        a_wishlist = acc.wishlist.to_string(index=False)
        a_friendlist = acc.friendlist.to_string(index=False)
        if a_wishlist == 'NaN':
            a_wishlist = str(i.itemID)
        else: 
            a_wishlist += "," + str(i.itemID)
        acc.update_account(a_name, a_surname, a_birthday, a_email, a_interests, a_wishlist, a_friendlist)
        acc = Account(ID = int(acc.ID))
        st.session_state.account = acc
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun() 


def modifyitem_page():
    acc = st.session_state.account
    items = (acc.wishlist.to_string(index=False)).replace("\"", "").split(",")
    items = [int(item) for item in items]
    id =st.text_input('Please enter ID of the item you want to modify', value=items[0])
    i = item(ID=int(id))
    form = st.form(key='ModifyItemForm')
    title = form.text_input('Title:', value= i.title.to_string(index=False), placeholder= i.title.to_string(index=False))
    desc = form.text_input('Description', value= i.desc.to_string(index=False), placeholder= i.desc.to_string(index=False))
    link = form.text_input('Link', value= i.link.to_string(index=False), placeholder= i.link.to_string(index=False))
    cost = form.text_input('Cost', value= i.cost.to_string(index=False), placeholder= i.cost.to_string(index=False))
    if form.form_submit_button('Modify item'):
        i.modify_item(title, desc, link, cost)
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun() 

def deleteitem_page():
    acc = st.session_state.account
    items = (acc.wishlist.to_string(index=False)).replace("\"", "").split(",")
    items = [int(item) for item in items]
    form = st.form(key='DeleteItemForm')
    id =form.text_input('Please enter ID of the item you want to delete', value=items[0])
    i = item(ID=int(id))
    if form.form_submit_button('Delete item'):
        acc = st.session_state.account
        a_name = acc.name.to_string(index=False)
        a_surname = acc.surname.to_string(index=False)
        a_birthday = acc.birthday.to_string(index=False)
        a_email = acc.email.to_string(index=False)
        a_notifications = acc.notifications.to_string(index=False)
        a_interests = acc.interests.to_string(index=False)
        a_wishlist = acc.wishlist.to_string(index=False)
        a_friendlist = acc.friendlist.to_string(index=False)

        a_wishlist = a_wishlist.split(",")
        a_wishlist.remove(str(i.itemID))
        a_wishlist = ','.join(a_wishlist)

        acc.update_account(a_name, a_surname, a_birthday, a_email, a_notifications, a_interests, a_wishlist, a_friendlist)
        acc = Account(ID = int(acc.ID))
        st.session_state.account = acc
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun() 

def friendlist_page():
    st.header('Friend List')
    acc = st.session_state.account
    friendlist = acc.friendlist.to_string(index=False)
    if friendlist != 'NaN':        
        friendlist = friendlist.split(',')
        friendobj = [Account(ID=int(f)) for f in friendlist]
        friendName = [f.name.to_string(index=False) for f in friendobj]
        friendSur = [f.surname.to_string(index=False) for f in friendobj]
        df = pd.DataFrame(list(zip(friendlist,friendName,friendSur)), columns=('ID', 'Name', 'Surname'))
        df.set_index('ID', inplace=True)
        st.table(df)
    if st.button('View Wishlist of friend'):
        st.session_state.runpage = 'friendwishlist'
        st.experimental_rerun() 
    if st.button('Add friend'):
        st.session_state.runpage = 'addfriend'
        st.experimental_rerun() 
    if st.button('Delete friend'):
        st.session_state.runpage = 'deletefriend'
        st.experimental_rerun() 
    if st.button('Back'):
        st.session_state.runpage = 'account'
        st.experimental_rerun()

def viewwishlist_page():
    acc = st.session_state.account
    friendlist = acc.friendlist.to_string(index=False)
    friendlist = friendlist.split(',')
    form = st.form(key='Viewwishlistform')
    id =form.text_input('Please enter ID of the friend', value=friendlist[0])
    friend = Account(ID=int(id))
    if form.form_submit_button('See wishlist'):
        items = (friend.wishlist.to_string(index=False)).replace("\"", "").split(",")
        items = [int(item) for item in items]
        item_objs = [item(ID=id) for id in items] 
        item_titles = [(i.title.to_string(index=False)).replace("\"", "") for i in item_objs]
        item_descs = [(i.desc.to_string(index=False)).replace("\"", "") for i in item_objs]
        item_links = [(i.link.to_string(index=False).replace("\"", "")) for i in item_objs]
        item_costs = [(i.cost.to_string(index=False).replace("\"", "")) for i in item_objs]

        df = pd.DataFrame(list(zip(items, item_titles, item_descs, item_links, item_costs)), columns=('ID', 'Title', 'Description', 'Link', 'Cost'))
        df.set_index('ID', inplace=True)
        st.dataframe(df)
    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun() 

def addfriend_page():
    acc = st.session_state.account
    friendlist = acc.friendlist.to_string(index=False)
    form = st.form(key='addfriend')
    id =form.text_input('Please enter ID of the friend')
    if form.form_submit_button('Add friend'):
        if friendlist != 'NaN':
            friendlist += ',' + str(id)
        else:
            friendlist = str(id)
        a_name = acc.name.to_string(index=False)
        a_surname = acc.surname.to_string(index=False)
        a_birthday = acc.birthday.to_string(index=False)
        a_email = acc.email.to_string(index=False)
        a_notification = acc.notifications.to_string(index=False)
        a_interests = acc.interests.to_string(index=False)
        a_wishlist = acc.wishlist.to_string(index=False)
        a_friendlist = acc.friendlist.to_string(index=False)
        acc.update_account(a_name, a_surname, a_birthday, a_email, a_notification, a_interests, a_wishlist, friendlist)
        acc = Account(ID = int(acc.ID))
        st.session_state.account = acc
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun() 
    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun() 


def deletefriend_page():
    acc = st.session_state.account
    friends = (acc.friendlist.to_string(index=False)).replace("\"", "").split(",")
    form = st.form(key='DeleteItemForm')

    id =form.text_input('Please enter ID of the friend want to delete', value=friends[0])
    if form.form_submit_button('Delete friend'):
        a_name = acc.name.to_string(index=False)
        a_surname = acc.surname.to_string(index=False)
        a_birthday = acc.birthday.to_string(index=False)
        a_email = acc.email.to_string(index=False)
        a_notifications = acc.notifications.to_string(index=False)
        a_interests = acc.interests.to_string(index=False)
        a_wishlist = acc.wishlist.to_string(index=False)
        a_friendlist = acc.friendlist.to_string(index=False)

        friends.remove(id)
        friends = ','.join(friends)

        acc.update_account(a_name, a_surname, a_birthday, a_email, a_notifications, a_interests, a_wishlist, friends)
        acc = Account(ID = int(acc.ID))
        st.session_state.account = acc
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun() 





if 'runpage' not in st.session_state:
    st.session_state.runpage = 'initial'

if 'account' not in st.session_state:
    st.session_state.account = 'None'

if st.session_state.runpage == 'initial':
    initial_page()
elif st.session_state.runpage == 'login':
    acc = login_page()
elif st.session_state.runpage == 'createaccount':
    acc = create_account()
elif st.session_state.runpage == 'account':
    account_page()
elif st.session_state.runpage == 'profile':
    profile_page()
elif st.session_state.runpage == 'editprofile':
    editprofile_page()
elif st.session_state.runpage == 'wishlist':
    wishlist_page()
elif st.session_state.runpage == 'additem':
    additem_page()
elif st.session_state.runpage == 'modifyitem':
    modifyitem_page()
elif st.session_state.runpage == 'deleteitem':
    deleteitem_page()
elif st.session_state.runpage == 'friendlist':
    friendlist_page()
elif st.session_state.runpage == 'friendwishlist':
    viewwishlist_page()
elif st.session_state.runpage == 'addfriend':
    addfriend_page()
elif st.session_state.runpage == 'deletefriend':
    deletefriend_page()