# app.py - Main application file

import streamlit as st
import time
import random
from datetime import datetime, timedelta

# Import components
from tabs.monkey import render_monkey_tab
from tabs.jokes import render_jokes_tab
from tabs.breathing import render_breathing_tab
from tabs.facts import render_facts_tab
from tabs.music import render_music_tab
from utils.styling import load_css
from utils.timer import get_remaining_time, format_time

# Set page config
st.set_page_config(
    page_title="15-Minute Break",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load CSS
load_css()

# Initialize app state
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=15)

# Reset function
def reset_break():
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=15)

# Header
st.markdown('<div class="title-container"><h1>☕ 15-Minute Break App</h1><h3>Relax. Refresh. Return stronger.</h3></div>', unsafe_allow_html=True)

# Calculate remaining time
remaining_seconds = get_remaining_time()

# Check if break time is over
if remaining_seconds > 0:
    with st.expander("⏳ Show Timer", expanded=False):
        minutes, seconds = divmod(remaining_seconds, 60)
        progress = 1 - (remaining_seconds / (15 * 60))

        st.markdown('<div class="timer-container">', unsafe_allow_html=True)
        st.markdown(f"<h2>Time Left: {minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)
        st.progress(progress)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Create tabs for different activities
    tab1, tab4, tab5, tab6 = st.tabs(["🧘 Breathe", "💡 Fun Facts", "🎵 Music", "🐒 Call Your Monkey"])
    
    # Render each tab content using imported functions
    with tab1:
        render_breathing_tab()
        
    with tab4:
        render_facts_tab()
    
    with tab5:
        render_music_tab()
    
    with tab6:
        render_monkey_tab()
    
    # Reset button in sidebar
    with st.sidebar:
        st.subheader("Break Controls")
        if st.button("Reset 15-Minute Timer"):
            reset_break()
            st.rerun()
    
    # Auto-refresh to update timer
    time.sleep(1)
    st.rerun()

else:
    # Break over screen
    st.markdown("""
    <div class="break-over">
        <h1>🔥 Break Over!</h1>
        <h2>⏰ Time to get back to work.</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Add motivational quote
    from utils.quotes import get_random_quote
    st.markdown(f"<h3 style='text-align:center; margin-top: 30px;'>{get_random_quote()}</h3>", unsafe_allow_html=True)
    
    # Play sound (browser workaround)
    from utils.audio import get_alert_sound_html
    st.markdown(get_alert_sound_html(), unsafe_allow_html=True)
    
    # Reset button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Another 15-Minute Break", key="restart"):
            reset_break()
            st.rerun()

# Footer
st.markdown("---")
st.markdown("### Made with love for my baby kutty")
st.caption("Remember: Taking regular breaks improves overall productivity and mental well-being!")