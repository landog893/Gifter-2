import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS, FOOTER_PATHS, SETTINGS


def inject_custom_css():
    with open('src/assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def navbar_component(acc):
    with open("src/assets/images/profile.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="#" id="{value}">{key}</a>')

    settings_items = ''
    for key, value in SETTINGS.items():
        settings_items += (
            f'<a id="{value}" class="settingsNav" href="#">{key}</a>')

    nameTag = rf'''
            <div class="dropdown hide" id="settingsDropDown">
                    <p class="navName"></p>
                    <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
                    <div id="myDropdown" class="dropdown-content">
                        {settings_items}
                    </div>
                </div>
            '''
    if not acc == 'None':
        nameTag = rf'''
            <div class="dropdown" id="settingsDropDown">
                    <p class="navName">{acc.name} {acc.surname}</p>
                    <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
                    <div id="myDropdown" class="dropdown-content">
                        {settings_items}
                    </div>
                </div>
            '''
    component = rf'''
            <nav class="container navbar" id="navbar">
                <ul class="navlist">
                {navbar_items}
                </ul>
                {nameTag}
            </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)
    js = '''
    <script>
        window.parent.document.getElementById("home").onclick = function() {
            window.parent.document.querySelectorAll(".stTabs .stButton button")[0].click()
        }
        window.parent.document.getElementById("wishlist").onclick = function() {
            window.parent.document.querySelectorAll(".stTabs .stButton button")[1].click()
        }
        window.parent.document.getElementById("friendlist").onclick = function() {
            window.parent.document.querySelectorAll(".stTabs .stButton button")[2].click()
        }
        window.parent.document.getElementById("profile").onclick = function() {
            window.parent.document.querySelectorAll(".stTabs .stButton button")[3].click()
        }
        window.parent.document.getElementById("logout").onclick = function() {
            window.parent.document.querySelectorAll(".stTabs .stButton button")[4].click()
        }

        // navbar elements
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        var cleanNavbar = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }

        for (var i = 0; i < navigationTabs.length; i++) {
            cleanNavbar(navigationTabs[i]);
        }

        // Dropdown hide / show
        var dropdown = window.parent.document.getElementById("settingsDropDown");
        dropdown.onclick = function() {
            var dropWindow = window.parent.document.getElementById("myDropdown");
            if (dropWindow.style.visibility == "hidden"){
                dropWindow.style.visibility = "visible";
            }else{
                dropWindow.style.visibility = "hidden";
            }
        };

        var settingsNavs = window.parent.document.getElementsByClassName("settingsNav");
        var cleanSettings = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }

        for (var i = 0; i < settingsNavs.length; i++) {
            cleanSettings(settingsNavs[i]);
        }
    </script>
    '''
    html(js)


def footer_component():
    with open("src/assets/images/github-logo.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    footer_items = ''
    for key, value in FOOTER_PATHS.items():
        footer_items += (f'<a class="footeritem" href="{value} "target="_blank">{key}</a>')
    component = rf'''
            <footer class="container footer" id="footer">
                <ul class="footerlist">
                <a class="footeritem" href="https://github.com/landog893/Gifter-2"target="_blank">
                    <img class="gitHub" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
                    Github Repository
                </a>
                {footer_items}
                </ul>
            </footer>
            '''
    st.markdown(component, unsafe_allow_html=True)
    js = '''
    <script>
        footer = window.parent.document.getElementById("footer")
        parentDir = window.parent.document.querySelectorAll(".main")[0]
        oldfooter = window.parent.document.querySelectorAll(".main > footer")[0]
        if (window.parent.document.querySelectorAll(".main > footer").length < 2) {
            parentDir.insertBefore(footer, oldfooter)
            }

        buttons = window.parent.document.querySelectorAll(".stTabs .stButton button")


        // footer elements
        var footerTabs = window.parent.document.getElementsByClassName("footeritem");
        var cleanFooter = function(footer_element) {
            footer_element.removeAttribute('target')
        }

        for (var i = 0; i < footerTabs.length; i++) {
            cleanFooter(footerTabs[i]);
        }

    </script>
    '''
    html(js)
