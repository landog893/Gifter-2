
from msilib.schema import ProgId
from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from account import Account
from account_info import AccountInfo
from item import item


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
    if but1:
        acc = Account(name, surname, birthday, interest)
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
    name = form.text_input('Name:', value= acc.name.to_string(index=False), placeholder= acc.name.to_string(index=False))
    surname = form.text_input('Surname:', value= acc.surname.to_string(index=False), placeholder= acc.surname.to_string(index=False))
    birthday = form.text_input('Birthday:', value= acc.birthday.to_string(index=False), placeholder= acc.birthday.to_string(index=False))
    ints = (acc.interests.to_string(index=False)).replace("\"", "")
    interests = form.text_input('Interest:', value=ints, placeholder=ints)
    if form.form_submit_button('Update'):
        acc.update_account(name, surname, birthday, interests, acc.wishlist.to_string(index=False), acc.friendlist.to_string(index=False))
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
        items = [item.replace(" ","") for item in items]
        items = [int(item) for item in items if item.isnumeric()]
        item_objs = [item(ID=id) for id in items]
        item_titles = [i.title for i in item_objs if len(i.title)>0]
        item_descs = [i.desc for i in item_objs if len(i.desc)>0]
        item_links = [i.link for i in item_objs if len(i.link)>0]
        item_costs = [i.cost for i in item_objs if i.cost]
        # item_titles = [(i.title.to_string(index=False)).replace("\"", "") for i in item_objs]
        # item_descs = [(i.desc.to_string(index=False)).replace("\"", "") for i in item_objs]
        # item_links = [(i.link.to_string(index=False).replace("\"", "")) for i in item_objs]
        # item_costs = [(i.cost.to_string(index=False).replace("\"", "")) for i in item_objs]

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
        new_item = item(title, desc, link, cost)
        acc = st.session_state.account
        a_name = acc.name.to_string(index=False)
        a_surname = acc.surname.to_string(index=False)
        a_birthday = acc.birthday.to_string(index=False)
        a_interests = acc.interests.to_string(index=False)
        a_wishlist = acc.wishlist.to_string(index=False)
        a_friendlist = acc.friendlist.to_string(index=False)
        if a_wishlist == 'NaN':
            a_wishlist = str(new_item.itemID)
        else: 
            a_wishlist += "," + str(new_item.itemID)
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
    id =st.selectbox('Please select ID of the item you want to modify',items)
    i = item(ID=int(id))
    form = st.form(key='ModifyItemForm')
    title = form.text_input('Title:', value= i.title, placeholder= i.title)
    desc = form.text_input('Description', value= i.desc, placeholder= i.desc)
    link = form.text_input('Link', value= i.link, placeholder= i.link)
    cost = form.text_input('Cost', value= i.cost, placeholder= i.cost)
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
    id =st.selectbox('Please enter ID of the item you want to delete', items)
    print(id)
    i = item(ID=int(id))
    form = st.form(key='DeleteItemForm')
    if form.form_submit_button('Delete item'):
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

    id =form.text_input('Please enter ID of the friend want to delete', value=friends[0])
    if form.form_submit_button('Delete friend'):
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