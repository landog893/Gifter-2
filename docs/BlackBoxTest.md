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
    T2: Registration
</td>
<td valign=top>
    Preconditions: CreateAccount page has loaded
    <br><br>
    Input new account infomation, in the popped up modal.
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
    After clicking the "Submit", the page jumps to the MainPage with the created account logged in
</td>
</tr>

<tr>
<td valign=top>
    T3: Invalid Registration
</td>
<td valign=top>
    Preconditions: LoginScreen has loaded
    <br><br>
    Click "Don't have an account? Register now!"
    <br><br>
    Input registration infomation, in the popped up modal.
    <br><br>
    &nbsp&nbsp  Info: 
    &nbsp&nbsp&nbsp&nbsp  Full Name: Test Name (A name we used before)<br><br>
    &nbsp&nbsp&nbsp&nbsp  Email address: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp  Age: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp  Year of Experience: (whatever)<br><br>
    &nbsp&nbsp&nbsp&nbsp  Job Keywords: (whatever)<br><br>
    <br><br>
    Click "Create User"
</td>
<td valign=top>
    The modal will pop up.
    <br><br>
    After clicking the "Create User", a notification saying "Registeration failed! User already exists." will show up.
</td>
<td valign=top>
    The modal pops up successfully.
    <br><br>
    After clicking the "Create User", a notification saying "Registeration failed! User already exists." shows up.
</td>
</tr>

<tr>
<td valign=top>
    T4: Valid Login
</td>
<td valign=top>
    Preconditions: LoginScreen has loaded
    <br><br>
    User Name: Test Name
    <br><br>
    Click Login
</td>
<td valign=top>
    The app will be navigated to the Job Board.
    <br><br>
    There will be a header saying: "Hello, Test Name!"
</td>
<td valign=top>
    The app is navigated to the Job Board.
    <br><br>
    There is a header saying: "Hello, Test Name!"
</td>
</tr>

<tr>
<td valign=top>
    T5: Profile auto populated
</td>
<td valign=top>
    Preconditions: Logged in with a valid username. (Here is "Test Name")
    <br><br>
    Click "My profile" in the navigation bar.
</td>
<td valign=top>
    The app will be navigated to the Profile view.
    <br><br>
    The infomation of the user will be auto populated in the Profile view.
</td>
<td valign=top>
    The app is navigated to the Profile view.
    <br><br>
    The following is the auto populated infomation in the Profile view:
        Info: 
            Full Name: Test Name
            Email address: test@gmail.com
            Age: 24
            Year of Experience: 1
            Job Keywords: Software Engineer

</td>
</tr>

<tr>
<td valign=top>
    T6: Application Search
</td>
<td valign=top>
    Preconditions: Logged in with a valid username. (Here is "Test Name")
    <br><br>
    Click "Application Search" in the navigation bar.
    <br><br>
    Input keyword:"software" in the input field and click the "Search for more applications" button.
    <br><br>
    Click the "Go To Job" button.
    <br><br>
    Click the "Apply here" button.
    <br><br>
    Input the relevant infomation
    <br><br>
    Click the "Save" button.
    <br><br>
    Go to the "My Application" view by clicking the button in the navigation bar.

</td>
<td valign=top>
    In the "Application Search View", 5 default jobs will show up.<br><br>
    After clicking the "Search for more applications" button. 5 New jobs with the search keywords will show up.
    <br><br>
    After clicking the "Go To Job" button. The job website will be opened in a new tab.
    <br><br>
    After clicking the "Apply here" button. A form with information of the corresponding job will show up.
    <br><br>
    After clicking the "Save" button and navigating to the MyApplication view, a corresponding record will show up.
    <br><br>

</td>
<td valign=top>
    In the "Application Search View", 5 default jobs shows up.<br><br>
    After clicking the "Search for more applications" button. 5 New jobs with the search keywords(here is "software") shows up.
    <br><br>
    After clicking the "Go To Job" button. The job website is opened in a new tab.
    <br><br>
    After clicking the "Apply here" button. A form with information of the corresponding job shows up.(Here is "Software Engineer - Entry Level" @ Lockheed Martin)
    <br><br>
    After clicking the "Save" button and navigating to the MyApplication view, a new record with Job Title = "Software Engineer - Entry Level" and company = "Lockheed Martin" showed up.
    <br><br>
</td>
</tr>

<tr>
<td valign=top>
    T7: My applications
</td>
<td valign=top>
    Preconditions: Logged in with a valid username. (Here is "Test Name")
    <br><br>
    Navigate to the My application view by clicking the "My Applications" button in the navigation bar.
    <br><br>
    Click the "+ New Application" button.
    <br><br>
    Input the informations.
    <br><br>
    Click the "Save" button.
    <br><br>
    Click on one of the records in the grid.
    <br><br>
    Click the "Delete" button.
</td>
<td valign=top>
    The app will be navigated to the "My Applications" view.
    <br><br>
    All the applications of the User will show up.
    <br><br>
    After clicking the "Save" button, a new record will be added.
    <br><br>
    After clicking the "Delete" button, the corresponding record will be removed from the grid.
</td>
<td valign=top>
    The app is navigated to the "My Applications" view.
    <br><br>
    All the applications of the User shows up.
    <br><br>
    After clicking the "Save" button, a new record is added.
    <br><br>
    After clicking the "Delete" button, the corresponding record is removed from the grid.

</td>
</tr>

<tr>
<td valign=top>
    T8: Dashboard
</td>
<td valign=top>
    Preconditions: Logged in with a valid username. (Here is "Test Name")
    <br><br>
    Navigate to the Dashboard view by clicking the "Dashboard"
    button in the navigation bar.
    <br><br>
    Click the "+ Send reminder email" button.
</td>
<td valign=top>
    The app will be navigated to the "Dashboard" view.
    <br><br>
    At most 5 default applications of the User will show up in the gird.
    <br><br>
    After clicking the "+ Send reminder email" button, a reminder email including deadline information will be sent to the User's email(if the email address is valid).
</td>
<td valign=top>
    The app is navigated to the "Dashboard" view.
    <br><br>
    5 default applications of the User show up in the grids while there are 7 applications in total of that User.
    <br><br>
     After clicking the "+ Send reminder email" button and providing a valid email in registration, a reminder email including deadline information shows up in the mailbox of that email address.

</td>
</tr>

</table>
