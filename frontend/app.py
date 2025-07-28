import streamlit as st
from auth.login import login_page
from pages.home import home_page

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        home_page()
    else:
        login_page()

if __name__ == "__main__":
    main()