# tabs/jokes.py - Jokes tab

import streamlit as st

# Jokes data
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call a parade of rabbits hopping backwards? A receding hare-line.",
    "Why can't you trust atoms? They make up everything!"
]

def render_jokes_tab():
    """Render the jokes tab content"""
    # Initialize joke index in session state if not present
    if 'joke_index' not in st.session_state:
        st.session_state.joke_index = 0
    
    st.subheader("Need a laugh?")
    
    if st.button("Tell me a joke"):
        st.session_state.joke_index = (st.session_state.joke_index + 1) % len(JOKES)
    
    st.info(JOKES[st.session_state.joke_index])
    st.caption("Laughter is a great stress reliever!")