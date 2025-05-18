import streamlit as st
import time
from datetime import datetime, timedelta

# Import components
from tabs.monkey import render_monkey_tab
from tabs.jokes import render_jokes_tab
from tabs.breathing import render_breathing_tab
from tabs.facts import render_facts_tab
from tabs.music import render_music_tab
from utils.styling import load_css
from utils.timer import get_remaining_time, format_time
from utils.quotes import get_random_quote
from utils.audio import get_alert_sound_html

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
if 'accepted' not in st.session_state:
    st.session_state.accepted = False
if 'break_minutes' not in st.session_state:
    st.session_state.break_minutes = 15
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
    st.session_state.end_time = None

# Reset function
def reset_break():
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=st.session_state.break_minutes)

# Function to handle break acceptance
def accept_break():
    duration = st.session_state.get('duration_input', 15)
    st.session_state.break_minutes = duration
    st.session_state.accepted = True
    reset_break()

# Welcome screen container
welcome_container = st.empty()

# Main app container
main_container = st.container()

# Step 1: Show welcome screen if not accepted
if not st.session_state.accepted:
    with welcome_container:
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", caption="Take a deep breath 🌿", use_container_width=True)

        st.markdown("## Welcome to Your Mindful Break")
        st.markdown("Take a break from the chaos. Choose your duration and relax.")

        # Use number_input with key
        st.number_input(
            "⏳ Enter your break time (minutes):", 
            min_value=1, 
            max_value=120, 
            value=15, 
            step=1,
            key="duration_input"
        )

        if st.button("✅ Accept & Start Break"):
            accept_break()
            welcome_container.empty()
            st.rerun()
else:
    # If we've accepted, clear the welcome container
    welcome_container.empty()

    # Step 2: Continue with the main app (existing code)
    with main_container:
        remaining_seconds = get_remaining_time()

        # Check if break time is over
        if remaining_seconds > 0:
            with st.expander("⏳ Show Timer", expanded=False):
                minutes, seconds = divmod(remaining_seconds, 60)
                progress = 1 - (remaining_seconds / (st.session_state.break_minutes * 60))

                st.markdown('<div class="timer-container">', unsafe_allow_html=True)
                st.markdown(f"<h2>Time Left: {minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)
                st.progress(progress)
                st.markdown('</div>', unsafe_allow_html=True)

            # Tabs
            tab1, tab4, tab5, tab6 = st.tabs(["🧘 Breathe", "💡 Fun Facts", "🎵 Music", "🐒 Call Your Monkey"])

            # Inject JS to hide the banner (optional, can be removed if banner is no longer shown)
            st.markdown("""
            <script>
            const tabs = parent.document.querySelectorAll('[data-baseweb="tab"]');
            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    const banner = parent.document.getElementById('break-banner');
                    if (banner) {
                        banner.style.display = 'none';
                    }
                });
            });
            </script>
            """, unsafe_allow_html=True)

            with tab1:
                render_breathing_tab()
            with tab4:
                render_facts_tab()
            with tab5:
                render_music_tab()
            with tab6:
                render_monkey_tab()

            # Sidebar
            with st.sidebar:
                st.subheader("Break Controls")
                if st.button("Reset Break"):
                    reset_break()
                    st.rerun()

            # Auto-refresh
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

            st.markdown(f"<h3 style='text-align:center; margin-top: 30px;'>{get_random_quote()}</h3>", unsafe_allow_html=True)
            st.markdown(get_alert_sound_html(), unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Start Another Break"):
                    st.session_state.accepted = False  # Go back to welcome page
                    st.rerun()

        st.markdown("---")
        st.markdown("### Made with love for my baby kutty")
        st.caption("Remember: Taking regular breaks improves overall productivity and mental well-being!")