# utils/styling.py - CSS and styling utilities

import streamlit as st

def load_css():
    """Load custom CSS for styling the app"""
    st.markdown("""
    <style>
        .main {
            background-color: #f5f7ff;
            padding: 20px;
        }
        .title-container {
            background-color: #e3e8ff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
        }
        .timer-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .expander-header {
            font-size: 18px;
            font-weight: bold;
        }
        .break-over {
            background-color: #ff5252;
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(255,82,82,0.4);
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% {transform: scale(1);}
            50% {transform: scale(1.03);}
            100% {transform: scale(1);}
        }
    </style>
    """, unsafe_allow_html=True)