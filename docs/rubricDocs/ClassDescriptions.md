#Class Description for Gifter

### Class: Account
Account class has six attributes, name, surname, birthday, interests, Wishlist and friend list. As the name implies, it keeps all the attributes regarding a user account. When an account gets created or gets updated, it creates an instance of Account Info class that functions as a manager for the accounts.
### Class: Account Info 
Account info carries only two attributes, the csv file that imitates the database and the data inside it. When triggered by the account class, Account Info class will update csv file as if it were updating the database.
### Class: Item
Account class has four attributes, title, description, link and cost. The item class it keeps all the attributes regarding an item instance, which is the objects accounts add to their Wishlist. When a new item is added to a Wishlist or item gets updated, it creates an instance of Item Manager class that functions as a manager for the items.
### Class: Item Manager
Item manager carries only two attributes, the csv file that imitates the database and the data inside it. When triggered by the item class, Account Info class will update csv file as if it were updating the database.
