import streamlit as st
import pandas as pd
from account import Account
from account_info import AccountInfo
from item import item
from datetime import datetime
import streamlit.components.v1 as components
import utils as utl
import requests
import re
from streamlit.components.v1 import html

extrajs = ''''''


def horizontalButtons():

    global extrajs
    extrajs += '''
        forms = window.parent.document.querySelectorAll('[data-testid="stFormSubmitButton"]');
        for (const element of forms) {
            element.classList.add("horizontalDiv");
            element.parentElement.classList.add("horizontalDiv");
            element.parentElement.parentElement.classList.add("horizontalDiv");
        }
    '''


email_sent = False


def initial_page():

    st.header("Gift Finder!")
    create = st.button('Create Account', type="primary")
    login = st.button('Log In', type="primary")
    if create:
        st.session_state.runpage = 'createaccount'
        st.experimental_rerun()
    if login:
        st.session_state.runpage = 'login'
        st.experimental_rerun()


def login_page():

    st.header("Login")
    form1 = st.form(key='Login form')
    f_name = form1.text_input('User Name')
    password = form1.text_input('Enter a password', type='password')
    but = form1.form_submit_button('Log in', type="primary")
    if but is True:
        accountMan = AccountInfo()
        info = accountMan.get_account(f_name, password)
        if isinstance(info, int) is True and info == -2:
            st.error("Password is wrong. Please put valid password!")
            st.session_state.runpage = 'login'
        elif isinstance(info, int) is True and info == -1:
            st.error("User Name is Incorrect. Please use correct user name!")
            st.session_state.runpage = 'login'
        else:
            acc = Account(ID=info[0], username=f_name, password=password)
            st.session_state.runpage = 'account'
            st.session_state.account = acc
            st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'initial'
        st.experimental_rerun()


def create_account():

    form = st.form(key='Create_form')
    f_name = form.text_input('First Name:')
    surname = form.text_input('Last Name:')
    birthday = form.text_input('Birthday (MM/DD/YYYY):')
    email = form.text_input('Email:')
    notifications = form.text_input('Email notifications (enter On or Off):')
    username = form.text_input('User Name:')
    password = form.text_input('Enter a password:', type='password')
    interest = form.text_input('Interests (please enter comma seperated):')

    but1 = form.form_submit_button('Submit', type="primary")
    but2 = form.form_submit_button("Back")
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

    # when create account button is clicked, check input before
    # creating account
    if but1 is True:
        error = False
        errorMessage = ""
        if (f_name == ""):
            error = True
            errorMessage += "Name cannot be empty.\n"
        if (surname == ""):
            error = True
            errorMessage += "Surname cannot be empty.\n"
        if (birthday == "" or validB is False):
            error = True
            errorMessage += "Birthday should be formatted MM/DD/YYYY.\n"
        if (email == "" or validE is False):
            error = True
            errorMessage += "Please enter a valid email.\n"
        if (notifications == "" or notifications != "On"):
            if (notifications != "Off"):
                error = True
                errorMessage += "Email notifications should be either 'On' or 'Off'.\n"
        # if there is an error, print the associated messages
        # and allow for user to correct
        if (error is True):
            st.error(errorMessage)
        # if there is not an error, create the account
        acc = Account(f_name, surname, birthday, email, notifications, username, password, interest)
        if int(acc.ID) == -2:
            st.session_state.runpage = 'createaccount'
        else:
            Account(ID=int(acc.ID))
            st.session_state.runpage = 'account'
            st.session_state.account = acc
            st.experimental_rerun()
    if but2:
        st.session_state.runpage = 'initial'
        st.experimental_rerun()
    horizontalButtons()


def account_page():

    acc = st.session_state.account
    st.header('Welcome ' + acc.name + '!')

    st.write("Quote of the day:")
    if 'response' not in st.session_state:
        st.session_state.response = requests.get('https://zenquotes.io/api/today')
    st.markdown(st.session_state.response.json()[0]["h"].replace('&mdash;', ''), unsafe_allow_html=True)

    # check if whether a notification email needs to be sent today
    # (is it 1 week before the account's birthday)
    global email_sent

    birthday = acc.birthday
    b = birthday.rpartition('/')[0] + birthday.rpartition('/')[1]
    b = b[:-1]
    month = b.rpartition('/')[0]
    day = b.rpartition('/')[2]
    currDate = datetime.now().date()

    birthdayDate = str(month) + "/" + str(day)

    if (int(currDate.month) > int(month) and int(currDate.day) > int(day)):
        birthdayDate += "/" + str(currDate.year + 1)
    else:
        birthdayDate += "/" + str(currDate.year)

    birthdayDate = datetime.strptime(birthdayDate, "%m/%d/%Y").date()

    if (birthdayDate - currDate).days == 7 and email_sent is False:
        email_sent = True
        if (acc.friendlist != 'NaN' and acc.wishlist != 'NaN'):
            acc.send_reminder_email()
            acc = Account(ID=int(acc.ID))
            st.session_state.account = acc
            st.session_state.runpage = 'profile'
        st.experimental_rerun()
    else:
        email_sent = False


def profile_page():

    st.header('Profile')
    acc = st.session_state.account
    st.write('First Name: ' + acc.name)
    st.write('Last Name: ' + acc.surname)
    st.write('Birthday: ' + acc.birthday)
    st.write('User Name: ' + acc.username)
    st.write('Password: ' + acc.password)
    st.write('Email: ' + acc.email)
    st.write('Email Notifications: ' + acc.notifications)
    st.write('Interests: ' + (acc.interests).replace("\"", ""))
    col0, col1, col2 = st.columns((2, 2, 2))
    with col0:
        if st.button("Edit Profile", type="primary"):
            st.session_state.runpage = 'editprofile'
            st.experimental_rerun()
    with col1:
        if st.button("Send Notifications", type="primary"):
            if (acc.friendlist != 'NaN' and acc.wishlist != 'NaN'):
                acc.send_reminder_email()
            else:
                st.error("Please ensure you have added items to your wishlist and friends to your friendlist before attempting to send email notifications.")
            st.experimental_rerun()


def editprofile_page():

    st.header('Edit Profile')
    form = st.form(key='EditProfileForm')
    acc = st.session_state.account
    name = form.text_input('First Name:', value=acc.name, placeholder=acc.name)
    surname = form.text_input('Last Name:', value=acc.surname, placeholder=acc.surname)
    birthday = form.text_input('Birthday:', value=acc.birthday, placeholder=acc.birthday)
    email = form.text_input('Email:', value=acc.email, placeholder=acc.email)
    notifications = form.text_input('Email Notifications:', value=acc.notifications, placeholder=acc.notifications)
    username = form.text_input('User Name:', value=acc.username, placeholder=acc.username)
    password = form.text_input('Password:', value=acc.password, placeholder=acc.password)
    ints = (acc.interests).replace("\"", "")
    interests = form.text_input('Interest:', value=ints, placeholder=ints)

    case = -1
    chars = set("~!@#$%^&*()_+=")
    if form.form_submit_button('Update', type="primary"):
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
        if (birthday == "" or validB is False):
            error = True
            errorMessage += "Birthday should be formatted MM/DD/YYYY.\n"
        if (email == "" or validE is False):
            error = True
            errorMessage += "Please enter a valid email.\n"
        if (notifications == "" or notifications != "On"):
            if (notifications != "Off"):
                error = True
                errorMessage += "Email notifications should be either 'On' or 'Off'.\n"
        # if there is an error, print the associated messages
        # and allow for user to correct
        if (error is True):
            st.error(errorMessage)
        # if there is not an error, update the account
        else:
            acc.update_account(name, surname, birthday, email, notifications, username, password, interests)
            acc = Account(ID=int(acc.ID))
            st.session_state.account = acc
            st.session_state.runpage = 'profile'
            st.experimental_rerun()
    if st.button("Back"):
        st.session_state.runpage = 'profile'
        st.experimental_rerun()


def wishlist_page():

    acc = st.session_state.account
    st.header("Your Wishlist")
    items = (acc.wishlist)

    if items != 'NaN':
        items = (acc.wishlist).replace("\"", "").split(",")
        items = [int(item) for item in items if item.isnumeric()]
        item_objs = [item(ID=id) for id in items]
        colms = st.columns((2, 2, 3, 1, 1, 2))
        fields = ["Item Number", "Title", 'Description', 'Cost', "Edit Item", "Remove Item"]
        for col, field_name in zip(colms, fields):
            col.write(field_name)
        j = 0
        for i in item_objs:
            col0, col1, col2, col4, col5, col6 = st.columns((2, 2, 3, 1, 1, 2))
            col0.write(j+1)
            col1.write((i.title).replace("\"", ""))
            col2.write((i.desc).replace("\"", ""))
            # col3.write(i.link.replace("\"", ""))
            col4.write(str(i.cost))
            button_phold = col5.empty()
            do_action = button_phold.button("Edit", key=items[j], type="primary")
            if do_action:
                st.session_state['edit_key'] = items[j]
                st.session_state.runpage = 'modifyitem'
                st.experimental_rerun()
            button_remove = col6.empty()
            do_remove_action = button_remove.button("Delete", key=str(items[j])+str(items[j]), type="primary")
            if do_remove_action:
                st.session_state['delete_key'] = items[j]
                st.session_state.runpage = 'deleteitem'
                st.experimental_rerun()
            j = j + 1
    if st.button('Add item', type="primary"):
        st.session_state.runpage = 'additem'
        st.experimental_rerun()
    global extrajs
    extrajs += '''
        document.addEventListener('DOMContentLoaded', function(event) {
        //the event occurred
        window.parent.document.querySelector('[data-testid="stHorizontalBlock"]').classList.add("colHeader");
        })
    '''


def additem_page():

    form = st.form(key='AddItemForm')
    title = form.text_input('Title:')
    desc = form.text_input('Description')
    link = form.text_input('Link')
    cost = form.text_input('Cost')

    case = -1
    chars = set("~!@#$%^&*()_+=")
    if form.form_submit_button('Add item', type="primary"):
        if title == "":
            case = 0
        else:
            if any((c in chars) for c in title):
                case = 1

        if cost != "":
            try:
                float(cost)
            except ValueError:
                case = 2

        if case == 0:
            st.error("Title is not nullable")
        elif case == 1:
            st.error("Title can not contain symbols")
        elif case == 2:
            st.error("Cost must be a number")
        else:
            i = item(title, desc, link, cost)
            acc = st.session_state.account
            a_name = acc.name
            a_surname = acc.surname
            a_birthday = acc.birthday
            a_email = acc.email
            a_notifications = acc.notifications
            a_username = acc.username
            a_password = acc.password
            a_interests = acc.interests
            a_wishlist = acc.wishlist
            a_friendlist = acc.friendlist
            if a_wishlist:
                a_wishlist += "," + str(i.itemID)
            else:
                a_wishlist = str(i.itemID)

            acc.update_account(a_name, a_surname, a_birthday, a_email, a_notifications, a_username, a_password, a_interests, a_wishlist, a_friendlist)

            acc = Account(ID=int(acc.ID))
            st.session_state.account = acc
            st.session_state.runpage = 'wishlist'
            st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()


def modifyitem_page():

    acc = st.session_state.account
    items = (acc.wishlist).replace("\"", "").split(",")
    items = [int(item) for item in items]
    id = st.session_state['edit_key']
    i = item(ID=int(id))

    form = st.form(key='ModifyItemForm')
    title = form.text_input('Title:', value=i.title, placeholder=i.title)
    desc = form.text_input('Description', value=i.desc, placeholder=i.desc)
    link = form.text_input('Link', value=i.link, placeholder=i.link)
    cost = form.text_input('Cost', value=i.cost, placeholder=i.cost)
    chars = set("~!@#$%^&*()_+=")
    if form.form_submit_button('Modify item', type="primary"):
        if title == "":
            st.error("Title is not nullable")
        elif any((c in chars) for c in title):
            st.error("Title can not contain symbols")
        elif cost != "":
            try:
                float(cost)
                print("modifying item")
                i.modify_item(title, desc, link, cost)
                st.session_state.runpage = 'wishlist'
                st.experimental_rerun()
            except ValueError:
                st.error("Cost must be a number")

    if st.button('Back', type="primary"):
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()


def deleteitem_page():

    id = st.session_state["delete_key"]
    acc = st.session_state.account
    items = (acc.wishlist).replace("\"", "").split(",")
    items = [int(item) for item in items]
    form = st.form(key='DeleteItemForm')
    i = item(ID=int(id))

    acc = st.session_state.account
    a_name = acc.name
    a_surname = acc.surname
    a_birthday = acc.birthday
    a_email = acc.email
    a_notifications = acc.notifications
    a_username = acc.username
    a_password = acc.password
    a_interests = acc.interests
    a_wishlist = acc.wishlist
    a_friendlist = acc.friendlist
    a_wishlist = a_wishlist.split(",")
    a_wishlist.remove(str(i.itemID))
    a_wishlist = ','.join(a_wishlist)

    i.delete_item()
    acc.update_account(a_name, a_surname, a_birthday, a_email, a_notifications, a_username, a_password, a_interests, a_wishlist, a_friendlist)
    acc = Account(ID=int(acc.ID))

    st.session_state.account = acc
    st.session_state.runpage = 'wishlist'
    st.experimental_rerun()


def friendlist_page():

    st.header('Friend List')
    acc = st.session_state.account
    friendlist = acc.friendlist
    if friendlist != 'NaN' or friendlist is not None:
        friendlist = friendlist.split(',')
        friendobj = [Account(ID=int(f)) for f in friendlist if f.isnumeric()]

        colms = st.columns((5, 5, 5, 5, 5, 5))
        fields = ["#Friend", "First Name", "Last Name", "Birthday", "Friend's Wishlist", "Delete Friend"]
        for col, field_name in zip(colms, fields):
            col.write(field_name)

        j = 0
        for i in friendobj:
            col0, col1, col2, col5, col3, col4 = st.columns((5, 5, 5, 5, 5, 5))
            col0.write(j+1)
            col1.write((i.name).replace("\"", ""))
            col2.write((i.surname).replace("\"", ""))
            col5.write((i.birthday))
            button_phold = col3.empty()
            do_action = button_phold.button("View Wishlist", key=j+1, type="primary")
            if do_action:
                st.session_state['freindId'] = friendlist[j]
                st.session_state.runpage = 'friendwishlist'
                st.experimental_rerun()
            button_remove = col4.empty()
            do_remove_action = button_remove.button("Delete friend", key=str(j+1)+str(j+1), type="primary")
            if do_remove_action:
                st.session_state['delete_friend'] = friendlist[j]
                st.session_state.runpage = 'deletefriend'
                st.experimental_rerun()
            j = j + 1

    if st.button('Add friend', type="primary"):
        st.session_state.runpage = 'addfriend'
        st.experimental_rerun()
    global extrajs
    extrajs += '''
        document.addEventListener('DOMContentLoaded', function(event) {
    //the event occurred
        forms = window.parent.document.querySelectorAll('.stButton');
        for (const element of forms) {
            element.classList.add("horizontalDiv");
            element.parentElement.classList.add("horizontalDiv");

        }
        forms[forms.length - 1].parentElement.classList.add("back");
        window.parent.document.querySelector('[data-testid="stHorizontalBlock"]').classList.add("colHeader");
        })
    '''


def viewwishlist_page():

    acc = st.session_state.account
    friendlist = acc.friendlist
    friendlist = friendlist.split(',')
    form = st.form(key='Viewwishlistform')
    id = st.session_state['freindId']
    item_objs = None

    try:
        friend = Account(ID=int(id))
        items = (friend.wishlist).replace("\"", "").split(",")
        items = [int(item) for item in items]
        item_objs = [item(ID=id) for id in items]
    except ValueError:
        st.error("This ID doesn't have any wishlist")

    if (item_objs is not None):
        item_titles = [(i.title).replace("\"", "") for i in item_objs]
        item_descs = [(i.desc).replace("\"", "") for i in item_objs]
        item_links = [(i.link.replace("\"", "")) for i in item_objs]
        item_costs = [i.cost for i in item_objs]

        df = pd.DataFrame(list(zip(items, item_titles, item_descs, item_links, item_costs)), columns=('#Wish', 'Title', 'Description', 'Link', 'Cost'))
        df.set_index('#Wish', inplace=True)
        st.dataframe(df)

    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()


def addfriend_page():

    acc = st.session_state.account
    friendlist = acc.friendlist
    print("Friend list for the account:")
    print(friendlist)
    form = st.form(key='addfriend')
    user_list = None
    username = form.text_input('Search friend by Name')
    id = -1
    form_submit = form.form_submit_button('Search friend', type="primary")
    if form_submit:
        form_submit = False
        accountMan = AccountInfo()
        user_list = accountMan.find_friend(username)
        if len(user_list) == 0 or user_list is None:
            st.error("There no user with that Name! Please look for valid User.")
        else:
            st.session_state.account = acc
            st.session_state['user_list'] = user_list
            st.session_state.runpage = 'savefriend'
            st.experimental_rerun()

    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()


def save_friendList():

    acc = st.session_state.account
    friendlist = acc.friendlist
    user_list = st.session_state['user_list']
    colms = st.columns((5, 5, 5, 5, 5))
    fields = ["#User", "First Name", "Last Name", "Birthday", "Add Friend"]
    for col, field_name in zip(colms, fields):
        col.write(field_name)
    j = 0
    for i in range(len(user_list)):
        col0, col1, col2, col3, col4 = st.columns((5, 5, 5, 5, 5))
        col0.write(j+1)
        col1.write((user_list[i][1]))
        col2.write((user_list[i][2]))
        col3.write((user_list[i][3]))
        button_phold = col4.empty()
        do_action = button_phold.button("ADD", key=j + 1, type="primary")
        if do_action:
            if friendlist:
                friendlist += ','+str(user_list[i][0])
            else:
                friendlist = str(user_list[i][0])

            a_name = acc.name
            a_surname = acc.surname
            a_birthday = acc.birthday
            a_email = acc.email
            a_notifications = acc.notifications
            a_username = acc.username
            a_password = acc.password
            a_interests = acc.interests
            a_wishlist = acc.wishlist
            acc.update_account(a_name, a_surname, a_birthday, a_email, a_notifications, a_username, a_password, a_interests, a_wishlist, friendlist)
            acc = Account(ID=int(acc.ID))

            st.session_state.account = acc
            st.session_state.runpage = 'friendlist'
            st.experimental_rerun()
        j = j + 1

    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()
    print("Inside save friend list function")


def deletefriend_page():

    acc = st.session_state.account
    friends = (acc.friendlist).replace("\"", "").split(",")
    form = st.form(key='DeleteItemForm')
    id = st.session_state['delete_friend']
    print("friend id")
    print(id)

    a_name = acc.name
    a_surname = acc.surname
    a_birthday = acc.birthday
    a_email = acc.email
    a_notifications = acc.notifications
    a_username = acc.username
    a_password = acc.password
    a_interests = acc.interests
    a_wishlist = acc.wishlist

    friends.remove(id)
    friends = ','.join(friends)

    acc.update_account(a_name, a_surname, a_birthday, a_email, a_notifications, a_username, a_password, a_interests, a_wishlist, friends)
    acc = Account(ID=int(acc.ID))
    st.session_state.account = acc
    st.session_state.runpage = 'friendlist'
    st.experimental_rerun()
    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()


if 'account' not in st.session_state or st.session_state.runpage == 'initial':
    st.session_state.account = 'None'


if 'runpage' not in st.session_state or (st.session_state.account == 'None' and not st.session_state.runpage == 'login' and not st.session_state.runpage == 'createaccount'):
    st.session_state.runpage = 'initial'

st.set_page_config(page_title='Gifter 2', page_icon='src/assets/images/gift-flat.ico')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component(st.session_state.account)


navtab, tab2 = st.tabs(["Navtab", "test"])

with navtab:
    if st.button('home'):
        st.session_state.runpage = 'account'
        st.experimental_rerun()
    if st.button('wishlist'):
        st.session_state.runpage = 'wishlist'
        st.experimental_rerun()
    if st.button('friendlist'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun()
    if st.button('acount'):
        st.session_state.runpage = 'profile'
        st.experimental_rerun()
    if st.button('logout'):
        st.session_state.runpage = 'initial'
        del st.session_state["account"]
        st.experimental_rerun()
with tab2:
    st.header("Placeholder")


extrajs = '''
        buttonDivs = window.parent.document.querySelectorAll('[data-testid="stVerticalBlock"] > [data-stale="false"] > .stButton');
        while (!buttonDivs) {
            buttonDivs = window.parent.document.querySelectorAll('[data-testid="stVerticalBlock"] > [data-stale="false"] > .stButton');
        }
        for (const element of buttonDivs) {
            element.parentElement.classList.add("but");
        }
    '''


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
elif st.session_state.runpage == 'savefriend':
    save_friendList()
elif st.session_state.runpage == 'deletefriend':
    deletefriend_page()

extrajs += '''
    </script>
'''
js = '''
    <script>
        body = window.parent.document.querySelectorAll("body")[0]
        body.className = "''' + st.session_state.runpage + '''";
        buttonDivs = window.parent.document.querySelectorAll('[data-testid="stVerticalBlock"] > [data-stale="false"] > .stButton');
        for (const element of buttonDivs) {
            element.parentElement.classList.add("buttonDiv");
        }
        ''' + extrajs + '''
    '''
html(js)
utl.footer_component()
