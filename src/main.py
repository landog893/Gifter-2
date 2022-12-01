
from msilib.schema import ProgId
from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from account import Account
from account_info import AccountInfo
from item import item
from datetime import datetime


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
    interest = form.text_input('Interests (please enter them comma seperated):')
    but1 = form.form_submit_button('Submit')
    case = -1
    chars = set("~!@#$%^&*()_+=")
    
    
    if but1:
        if f_name == "":
            case = 0
        else:
            if any((c in chars) for c in f_name):
                case = 1
                
        if any((c in chars) for c in surname):
            case = 2
        
        if birthday != "":
            try: datetime.strptime(birthday, "%m/%d/%Y")
            except ValueError: case = 3
        
        if username == "":
            case = 4
        
        if password == "":
            case = 5
        
        if case == 0: st.error("First Name is not nullable")
        elif case == 1: st.error("First Name can not contain symbols")
        elif case == 2: st.error("Surname can not contain symbols")
        elif case == 3: st.error("Birthday date is not valid (MM/DD/YYYY)") 
        elif case == 4: st.error("User Name is not nullable") 
        elif case == 5: st.error("Password is not nullable") 
        else:
            try:        
                acc = Account(f_name, surname, birthday,username,password, interest)
                if int(acc.ID)==-2:
                    st.session_state.runpage = 'createaccount'
                    # st.write('Please fill out the form with unique user name')
                    # st.experimental_rerun()
                else:
                    Account(ID = int(acc.ID))
                    st.session_state.runpage = 'account'
                    st.session_state.account = acc
                    st.experimental_rerun()
            except Exception as errorMsg:
                st.error(errorMsg)
            
    if st.button('Back'):
        st.session_state.runpage = 'initial'
        st.experimental_rerun() 

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


def profile_page():
    st.header('Profile')
    acc = st.session_state.account
    st.write('ID: ' + str(acc.ID))
    st.write('Name: ' + acc.name.to_string(index=False))
    st.write('Surname: ' + acc.surname.to_string(index=False))
    st.write('Birthday: ' + acc.birthday.to_string(index=False))
    st.write('Interests: ' + (acc.interests.to_string(index=False)).replace("\"", ""))
    if st.button("Edit Profile"):
        st.session_state.runpage = 'editprofile'
        st.experimental_rerun()
    if st.button("Back"):
        st.session_state.runpage = 'account'
        st.experimental_rerun()

def editprofile_page():
    st.header('Edit Profile')
    form = st.form(key='EditProfileForm')
    acc = st.session_state.account
    name = form.text_input('First Name:', value= acc.name, placeholder= acc.name)
    surname = form.text_input('Last Name:', value= acc.surname, placeholder= acc.surname)
    birthday = form.text_input('Birthday:', value= acc.birthday, placeholder= acc.birthday)
    username = form.text_input('User Name:', value= acc.username, placeholder= acc.username)
    password = form.text_input('Password:', value= acc.password, placeholder= acc.password, type="password")
    ints = (acc.interests).replace("\"", "")
    interests = form.text_input('Interest:', value=ints, placeholder=ints)

    case = -1
    chars = set("~!@#$%^&*()_+=")
    if form.form_submit_button('Update'):
        if name == "":
            case = 0
        else:    
            if any((c in chars) for c in name):
                case = 1
                
        if any((c in chars) for c in surname):
            case = 2
        
        if birthday != "":
            try: datetime.strptime(birthday, "%m/%d/%Y")
            except ValueError: case = 3
        
        if username == "":
            case = 4
        
        if password == "":
            case = 5
        
        if case == 0: st.error("First Name is not nullable")
        elif case == 1: st.error("First Name can not contain symbols")
        elif case == 2: st.error("Surname can not contain symbols")
        elif case == 3: st.error("Birthday date is not valid (MM/DD/YYYY)") 
        elif case == 4: st.error("User Name is not nullable") 
        elif case == 5: st.error("Password is not nullable") 
        else:   
            try:
                acc.update_account(name, surname, birthday, username, password,interests)
                acc = Account(ID = int(acc.ID))
                st.session_state.account = acc
                st.session_state.runpage = 'profile'
                st.experimental_rerun()
            except Exception as errorMsg:
                st.error(errorMsg)           

            
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
    
    case = -1
    chars = set("~!@#$%^&*()_+=")
    if form.form_submit_button('Add item'):
        if title == "":
            case = 0
        else:    
            if any((c in chars) for c in title):
                case = 1
        
        if cost != "":
            try: float(cost)    
            except ValueError: case = 2
        
        if case == 0: st.error("Title is not nullable")
        elif case == 1: st.error("Title can not contain symbols")
        elif case == 2: st.error("Cost must be a number")
 
        else:  
            i = item(title, desc, link, cost)
            acc = st.session_state.account
            a_name = acc.name.to_string(index=False)
            a_surname = acc.surname.to_string(index=False)
            a_birthday = acc.birthday.to_string(index=False)
            a_interests = acc.interests.to_string(index=False)
            a_wishlist = acc.wishlist.to_string(index=False)
            a_friendlist = acc.friendlist.to_string(index=False)
            if a_wishlist == 'NaN':
                a_wishlist = str(i.itemID)
            else: 
                a_wishlist += "," + str(i.itemID)
            acc.update_account(a_name, a_surname, a_birthday, a_interests, a_wishlist, a_friendlist)
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
    id = st.session_state['edit_key']
    i = item(ID=int(id))
    form = st.form(key='ModifyItemForm')
    title = form.text_input('Title:', value= i.title, placeholder= i.title)
    desc = form.text_input('Description', value= i.desc, placeholder= i.desc)
    link = form.text_input('Link', value= i.link, placeholder= i.link)
    cost = form.text_input('Cost', value= i.cost, placeholder= i.cost)
    chars = set("~!@#$%^&*()_+=")
    case = -1
    
    if form.form_submit_button('Modify item'):
        if title == "":
            case = 0

        if cost != "":
            try:
                float(cost)
            except ValueError:
                case = 1
                
        if case == 0: st.error("Item does not exist")
        elif case == 1:  st.error("Cost must be a number")
        
        else:
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
    case = -1
    
    if form.form_submit_button('Delete item'):
        try: 
            i = item(ID=int(id))
        except ValueError:
            case = 0
        
        try: int(id)
        except ValueError: 
            case = 1
        
        if case == 0: st.error("Item ID does not exist")
        elif case == 1: st.error("Item ID must be an integer")
        else:
            acc = st.session_state.account
            a_name = acc.name.to_string(index=False)
            a_surname = acc.surname.to_string(index=False)
            a_birthday = acc.birthday.to_string(index=False)
            a_interests = acc.interests.to_string(index=False)
            a_wishlist = acc.wishlist.to_string(index=False)
            a_friendlist = acc.friendlist.to_string(index=False)
    
            a_wishlist = a_wishlist.split(",")
            a_wishlist.remove(str(i.itemID))
            a_wishlist = ','.join(a_wishlist)
    
            acc.update_account(a_name, a_surname, a_birthday, a_interests, a_wishlist, a_friendlist)
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
    id =st.session_state['freindId']
    item_objs = None
    
    try:
        friend = Account(ID=int(id))
        items = (friend.wishlist).replace("\"", "").split(",")
        items = [int(item) for item in items]
        item_objs = [item(ID=id) for id in items] 
        item_titles = [(i.title).replace("\"", "") for i in item_objs]
        item_descs = [(i.desc).replace("\"", "") for i in item_objs]
        item_links = [(i.link.replace("\"", "")) for i in item_objs]
        item_costs = [i.cost for i in item_objs]
        
        df = pd.DataFrame(list(zip(items, item_titles, item_descs, item_links, item_costs)), columns=('#Wish', 'Title', 'Description', 'Link', 'Cost'))
        df.set_index('#Wish', inplace=True)
        st.dataframe(df)
        
    except TypeError:
        st.error("This ID doesn't have any wishlist")
    except ValueError:
        st.error("This ID doesn't have any wishlist")
    

    if st.button('Back'):
        st.session_state.runpage = 'friendlist'
        st.experimental_rerun() 

def addfriend_page():
    acc = st.session_state.account
    friendlist = acc.friendlist.to_string(index=False)
    form = st.form(key='addfriend')
    id =form.text_input('Please enter ID of the friend')
    case = -1
    
    if form.form_submit_button('Add friend'):
        try: 
            friend = Account(ID=int(id))
        except ValueError:
            case = 0
        
        try: int(id)
        except ValueError: 
            case = 1
        
        if case == 0: st.error("Friend ID does not exist")
        elif case == 1: st.error("Friend ID must be an integer")
        else:
            if friendlist != 'NaN':
                friendlist += ',' + str(id)
            else:
                friendlist = str(id)
            a_name = acc.name.to_string(index=False)
            a_surname = acc.surname.to_string(index=False)
            a_birthday = acc.birthday.to_string(index=False)
            a_interests = acc.interests.to_string(index=False)
            a_wishlist = acc.wishlist.to_string(index=False)
            a_friendlist = acc.friendlist.to_string(index=False)
            acc.update_account(a_name, a_surname, a_birthday, a_interests, a_wishlist, friendlist)
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
    id = form.text_input('Please enter ID of the friend want to delete', value=friends[0])
    case = -1
    
    if form.form_submit_button('Delete friend'):
        try: 
            Account(ID=int(id))
        except ValueError:
            case = 0
        
        try: int(id)
        except ValueError: 
            case = 1
        
        if case == 0: st.error("Friend ID does not exist")
        elif case == 1: st.error("Friend ID must be an integer")
        else:
            a_name = acc.name.to_string(index=False)
            a_surname = acc.surname.to_string(index=False)
            a_birthday = acc.birthday.to_string(index=False)
            a_interests = acc.interests.to_string(index=False)
            a_wishlist = acc.wishlist.to_string(index=False)
            a_friendlist = acc.friendlist.to_string(index=False)
    
            friends.remove(id)
            friends = ','.join(friends)
    
            acc.update_account(a_name, a_surname, a_birthday, a_interests, a_wishlist, friends)
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