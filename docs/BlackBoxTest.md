# Black Box Tests for Gifter
## Test Description Table
<table width="100%" border=0 align=center>
<tr>
<td align=center><b>Test ID</b></td>
<td align=center><b>Description</b></td>
<td align=center><b>Expected Results</b></td>
<td align=center><b>Actual Results</b> </td>
</tr>

    
<tr>
<td valign=top>
    T1: Invalid Login
</td>
<td valign=top>
    Preconditions: LoginPage has loaded
    <br><br>
    UserID: invalid userid
    <br><br>
    Click Log in
</td>
<td valign=top>
    There will be a notificaion saying: "No saved data found".
</td>
<td valign=top>
    There is a notificaion saying: "UserId is not exist".
    <br><br>
    Remain on the LoginScreen page without navigating.
</td>
</tr>

    
<tr>
<td valign=top>
    T2: Valid Login
</td>
<td valign=top>
    Preconditions: LoginPage has loaded
    <br><br>
    UserID: Valid userid
    <br><br>
    Click Log in
</td>
<td valign=top>
    After clicking the "Log in", the page will jump to the Main page with the user logged in.
</td>
<td valign=top>
    After clicking the "Log in", the page jumps to the Main page with the user logged in.
</td>
</tr>
    
    
<tr>
<td valign=top>
    T3: Registration
</td>
<td valign=top>
    Preconditions: CreateAccount page has loaded
    <br><br>
    Input new account infomation in the popped up modal.
    <br><br>
    &nbsp&nbsp   Info: <br><br>
    &nbsp&nbsp&nbsp&nbsp   Name: Ayrak<br><br>
    &nbsp&nbsp&nbsp&nbsp   Surname: Bayraktar<br><br>
    &nbsp&nbsp&nbsp&nbsp   Birthday: 11/15/1990<br><br>
    &nbsp&nbsp&nbsp&nbsp   Interest: Dancing, Reading, Cooking, Ballet, Writing<br><br>
    Click "Submit"
</td>
<td valign=top>
    The modal will pop up.
    <br><br>
    After clicking the "Submit", the page will jump to the MainPage with the created account logged in. A notification saying "Welcome Ayrak!". 
</td>
<td valign=top>
    The modal pops up successfully.
    <br><br>
    After clicking the "Submit", the page jumps to the MainPage with the created account logged in. A notification saying "Welcome Ayrak!". 
</td>
</tr>

    
<tr>
<td valign=top>
    T4: Invalid registration
</td>
<td valign=top>
    Preconditions: CreateAccount page has loaded
    <br><br>
    Input new account infomation in the popped up modal.
    <br><br>
    &nbsp&nbsp   Info: <br><br>
    &nbsp&nbsp&nbsp&nbsp   Name: Ayrak (an exist username)<br><br>
    &nbsp&nbsp&nbsp&nbsp   Surname: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp   Birthday: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp   Interest: (whatever)<br><br>
    Click "Submit"
</td>
<td valign=top>
    The modal will keep on screen.
    <br><br>
    After clicking the "Submit", a notification saying "Registeration failed! User already exists." will show up. 
</td>
<td valign=top>
    The modal keeps on screen.
    <br><br>
    After clicking the "Submit", a notification saying "User already exists." shows up. 
</td>
</tr>
    
    
<tr>
<td valign=top>
    T5: Edit Profile
</td>
<td valign=top>
    Preconditions: EditProfile page has loaded
    <br><br>
    Input edited profile infomation in the popped up modal.
    <br><br>
    &nbsp&nbsp   Info: <br><br>
    &nbsp&nbsp&nbsp&nbsp   Name: Yrak<br><br>
    &nbsp&nbsp&nbsp&nbsp   Surname: Raktar<br><br>
    &nbsp&nbsp&nbsp&nbsp   Birthday: 11/18/1990<br><br>
    &nbsp&nbsp&nbsp&nbsp   Interest: Ballet, Writing<br><br>
    Click "Submit"
</td>
<td valign=top>
    The modal will pop up.
    <br><br>
    After clicking the "Update", the page will jump to the Profile page with the user information updated.
</td>
<td valign=top>
    The modal pops up successfully.
    <br><br>
    After clicking the "Update", the page jump to the Profile page with the user information updated.
</td>
</tr>

  
<tr>
<td valign=top>
    T6: Fail to Edit Profile
</td>
<td valign=top>
    Preconditions: EditProfile page has loaded
    <br><br>
    Input edited profile infomation in the popped up modal.
    <br><br>
    &nbsp&nbsp   Info: <br><br>
    &nbsp&nbsp&nbsp&nbsp   Name: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp   Surname: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp   Birthday: 15/18/1990 (invalid date format)<br><br>
    &nbsp&nbsp&nbsp&nbsp   Interest: (whatever)<br><br>
    Click "Submit"
</td>
<td valign=top>
    The modal will keep on screen.
    <br><br>
    After clicking the "Update", a notification saying "Failed to edit! Birthday format is wrong." will show up. 
</td>
<td valign=top>
    The modal keeps on screen.
    <br><br>
    After clicking the "Update", a notification saying "Birthday date is not valid (MM/DD/YYYY)" shows up. 
</td>
</tr>
    

<tr>
<td valign=top>
    T7: Modify Item
</td>
<td valign=top>
    Preconditions: ModifyItem page has loaded
    <br><br>
    Input item id we want to modify, and edit infomation in the popped up modal.
    <br><br>
    &nbsp&nbsp   UserID: <br><br>
    &nbsp&nbsp&nbsp&nbsp   ID: 2<br><br>
    &nbsp&nbsp   Info: <br><br>
    &nbsp&nbsp&nbsp&nbsp   Name: Yrak<br><br>
    &nbsp&nbsp&nbsp&nbsp   Surname: Raktar<br><br>
    &nbsp&nbsp&nbsp&nbsp   Birthday: 11/18/1990<br><br>
    &nbsp&nbsp&nbsp&nbsp   Interest: Ballet, Writing<br><br>
    Click "Submit"
</td>
<td valign=top>
    The modal will pop up.
    <br><br>
    After clicking the "Modify item", the page will jump to the WishList page.
</td>
<td valign=top>
    The modal pops up.
    <br><br>
    After clicking the "Modify item", the page jumps to the WishList page.
</td>
</tr>

    
<tr>
<td valign=top>
    T7: Fail to Modify Item
</td>
<td valign=top>
    Preconditions: ModifyItem page has loaded
    <br><br>
    Input item id we want to modify, and edit infomation in the popped up modal.
    <br><br>
    &nbsp&nbsp   UserID: <br><br>
    &nbsp&nbsp&nbsp&nbsp   ID: 99(id is not exist)<br><br>
    &nbsp&nbsp   Info: <br><br>
    &nbsp&nbsp&nbsp&nbsp   Name: Yrak<br><br>
    &nbsp&nbsp&nbsp&nbsp   Surname: Raktar<br><br>
    &nbsp&nbsp&nbsp&nbsp   Birthday: 11/18/1990<br><br>
    &nbsp&nbsp&nbsp&nbsp   Interest: Ballet, Writing<br><br>
    Click "Submit"
</td>
<td valign=top>
    The modal will keep on screen.
    <br><br>
    After clicking the "Modify item", a notification saying "Failed to modify! UserID is not exist." will show up. 
</td>
<td valign=top>
    The modal keeps on screen.
    <br><br>
    After clicking the "Modify item", a notification saying "UserId is not exist" shows up. 
</td>
</tr>
</table>
