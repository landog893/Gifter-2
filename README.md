# CSC510_Project1 - Gifter

[![DOI](https://zenodo.org/badge/541408861.svg)](https://zenodo.org/badge/latestdoi/541408861)
[![GitHub license](https://img.shields.io/github/license/yagmurbbayraktar/CSC510_Project1)](https://github.com/yagmurbbayraktar/CSC510_Project1/blob/main/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/yagmurbbayraktar/CSC510_Project1)](https://github.com/yagmurbbayraktar/CSC510_Project1/network)
[![GitHub license](https://img.shields.io/github/license/yagmurbbayraktar/CSC510_Project1)](https://github.com/yagmurbbayraktar/CSC510_Project1/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/yagmurbbayraktar/CSC510_Project1/branch/main/graph/badge.svg?token=3SR30MKCUD)](https://codecov.io/gh/yagmurbbayraktar/CSC510_Project1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build](https://github.com/yagmurbbayraktar/CSC510_Project1/actions/workflows/python-app.yml/badge.svg)](https://github.com/yagmurbbayraktar/CSC510_Project1/actions/workflows/python-app.yml)

# Gifter-2
[![DOI](https://zenodo.org/badge/535341071.svg)](https://zenodo.org/badge/latestdoi/535341071)
[![License](https://img.shields.io/github/license/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/blob/main/LICENSE.md)
[![java](https://img.shields.io/badge/Made%20with-Java-brightgreen?style=plastic)](https://www.oracle.com/java/technologies/downloads/)
[![size](https://img.shields.io/github/languages/code-size/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2)
[![lang](https://img.shields.io/github/languages/count/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/search?l=Java&type=code)
[![contrib](https://img.shields.io/github/contributors/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/graphs/contributors)
[![issue op](https://img.shields.io/github/issues/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/issues)
[![issue cl](https://img.shields.io/github/issues-closed/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/issues?q=is%3Aissue+is%3Aclosed)
[![pull](https://img.shields.io/github/issues-pr/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/pulls?q=is%3Aopen+is%3Apr)
[![pull_closed](https://img.shields.io/github/issues-pr-closed/landog893/Gifter-2?style=plastic)](https://github.com/landog893/Gifter-2/pulls?q=is%3Apr+is%3Aclosed)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/landog893/Gifter-2/Build%20Workflow?style=plastic)](https://github.com/landog893/Gifter-2/actions/workflows/build.yml)

<br>
<p align="center"><img width="400" src="https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/15883/christmas-gifts-clipart-xl.png"></p>


Gifter-2 is a social platform built on the idea of gift giving and receiving! This application is deployed on the web and is available for individuals of all ages to use! 

## Description

Gifter-2 is a social platform built on the idea of gift giving and receiving! The goal of this application is to aid in the process of picking out a gift for friends. Users can create wishlists for themselves and add items/gifts that they would like to receive for their birthday. Users can proceed to add friends and view their wishlists as well. Gifter-2 also allows users to opt-in to email notifications which send a user's friends a reminder email regarding their upcoming birthday (if their email notifications are on as well). Items in the wishlists contain the cost of the item as well as the website where it can be purchased.

To start using Gifter-2, a user must first register by creating an account. The system collects information about a user's name, birthday, email, and interests. All of this information is stored in Gifter-2's database, and is not used by Gifter-2 in any other way. 

## Technologies
<p align="left">
  <a href="https://www.python.org/" target="_blank"> 
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="python" height="60"/>
  </a>
  <a href="https://streamlit.io/" target="_blank">
    <img src="https://res.cloudinary.com/dyd911kmh/image/upload/v1640050215/image27_frqkzv.png" alt="streamlit" height="60"/>
  </a>
  <a href="https://www.postgresql.org/" target="_blank"> 
    <img src="https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_251be2af3ae607c45c14e816eaa1cf41/postgresql.png" alt="postgresql" height="65"/>
      <a href="https://docs.anaconda.com/navigator/index.html" target="_blank"> 
    <img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png" alt="anaconda" height="65"/>
</p> 

* Python
* StreamLit
* PostgreSQL

## Features

All new features are in bold. 

* Register as a user.
* Add, edit, and delete items from a wishlist.
* Dashboard displaying friendlist with their associated wishlists.
* **Significantly improved UI experience.**
* **Login using username.**
* **Search for friends using usernames.**
* **Search for items using keywords.**
* **Send reminder emails for upcoming birthdays (if email notifications are on).**
* **Usage of PostgreSQL database to persist information.** 
* **Application deployed to web.**

## Installation

You will need the following programs and packages installed on your local machine.

Programs:

* Python 
* StreamLit
* PostgreSQL
* Anaconda Navigator

 1) Setup and launch Anaconda Navigator.
 2) Navigate to the location of the application and use the command ```streamlit run src/main.py```.
 
 ** DATABASE?? **

Note: In order to use the "Email Notification" functionality for this project, your team must set up an **Outlook** email account, and add the username and password to the send_reminder_email() method in account.py. You cannot use Gmail for this feature because Google set up a new restriction this year that doesn't allow third-party apps to send emails from Gmail accounts. 

## Documentation

This project is a refactoring of the [Gifter](https://github.com/yagmurbbayraktar/CSC510_Project1) project from 2022. We have added several functionalities to significantly enhance the scope and user experience of this application. 

* The video displaying the functionalities of the original project Gifter can be found [here]().
* The video displaying the new functionalities of Gifter-2 in comparison to the original project Gifter can be found [here]().

** ADD VIDEO LINKS **

### Use Cases
In order to learn more about how to run Gifter-2 and use its features, check out our [USAGE.md]() file!
** ADD USAGE.MD FILE **

### Documentation
**Still need to complete** 

### Code Coverage
Gifter-2 uses CodeCov to generate the code coverage of the source code. Additionally, we use [blackbox tests](https://github.com/landog893/Gifter-2/blob/main/docs/BlackBoxTest.md) on the UI to supplement the coverage and ensure that the functionality works as expected. 

## Future Features

While Gifter-2 is ready for users, there are several enhancements that could be made to amplify user experience. Below, we have listed several scopes of future improvements to Gifter-2 with a brief description. 

* **Smart phone application:** Create an application for mobile devices that allows users to use Gifter-2 on the go.
* **APIs enhancement:** Incorporate the use of APIs from larger e-commerce stores such as Amazon or Target.
* **Machine Learning:** Introduce machine learning algorithms to suggest gifts for users based on interests and previous gifts. 
* **Chrome extension:** Create a Chrome extension so users can add items to their wishlist while browsing online.  
* **Calendar:** Develop a calendar feature to display user birthdays. 

## Contribution

Please see the CONTRIBUTING.md for instructions on how to contribute to our repository.

## License

This project is licensed under MIT.

## Team Members
The team members who developed Gifter-2 are:
* Huang-Xing (Jesse) Chen
* Landon Gaddy
* Li-Chia (Jerry) Chang 
* Saminur (Sami) Islam
* Shruti Marota

We communicated via Discord and through weekly in-person meetings. 
<br>
<img width="500" alt="Screenshot (531)" src="https://user-images.githubusercontent.com/70153150/194780113-6e6c8a0c-6233-4883-b294-fdfddb96469a.png">
