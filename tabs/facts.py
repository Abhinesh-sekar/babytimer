import streamlit as st
import requests

FACT_API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    try:
        response = requests.get(FACT_API_URL)
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "Couldn't fetch a fact right now.")
        else:
            return "Oops! Something went wrong while fetching a fact."
    except Exception as e:
        return f"An error occurred: {e}"

def render_facts_tab():
    """Render the fun facts tab content using an API"""
    st.subheader("Random Fun Facts")

    if st.button("Show me a random fact"):
        st.session_state.random_fact = get_random_fact()

    # Display fact from session state or fetch one initially
    if 'random_fact' not in st.session_state:
        st.session_state.random_fact = get_random_fact()

    st.success(st.session_state.random_fact)
    st.caption("I got these random facts from an open-source API, so check their authenticity—not now, maybe later. UwU")
