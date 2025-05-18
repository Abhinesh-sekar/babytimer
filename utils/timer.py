# utils/timer.py - Timer related utilities

import streamlit as st
from datetime import datetime

def get_remaining_time():
    """Calculate the remaining time in seconds"""
    now = datetime.now()
    remaining_time = st.session_state.end_time - now
    return max(0, int(remaining_time.total_seconds()))

def format_time(seconds):
    """Format seconds into minutes:seconds format"""
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"