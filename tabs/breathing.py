import streamlit as st
from datetime import datetime, timedelta

# Breathing exercise constants
BREATHING_STATES = ["Breathe in...", "Hold...", "Breathe out..."]
BREATHING_TIMES = [4, 7, 8]  # seconds for each state
BREATHING_COLORS = ["#a8e6cf", "#dcedc1", "#ffd3b6"]
MAX_CYCLES = 4

def render_breathing_tab():
    """Render the breathing exercise tab content"""
    st.subheader("Breathing Exercise")
    
    # Initialize breathing state variables if not present
    if 'breathing_active' not in st.session_state:
        st.session_state.breathing_active = False
        
    if 'breathing_step' not in st.session_state:
        st.session_state.breathing_step = 0
    
    if 'breathing_count' not in st.session_state:
        st.session_state.breathing_count = 0
    
    if 'breathing_timer' not in st.session_state:
        st.session_state.breathing_timer = BREATHING_TIMES[0]
    
    if 'breathing_start_time' not in st.session_state:
        st.session_state.breathing_start_time = None
    
    if 'breathing_step_start_time' not in st.session_state:
        st.session_state.breathing_step_start_time = None
    
    # Update timer if exercise is active
    if st.session_state.breathing_active:
        update_breathing_timer()
    
    # Display controls
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Breathing visualization
        animation_css = ""
        if st.session_state.breathing_active:
            if st.session_state.breathing_step == 0:  # Breathe in
                animation_css = "animation: expand 4s ease-in-out;"
            elif st.session_state.breathing_step == 1:  # Hold
                animation_css = "animation: hold 7s linear forwards;"
            else:  # Breathe out
                animation_css = "animation: contract 8s ease-in-out;"
        
        # Visual breathing circle
        st.markdown(f"""
        <style>
            @keyframes expand {{
                from {{ transform: scale(1); }}
                to {{ transform: scale(1.3); }}
            }}
            @keyframes hold {{
                from {{ transform: scale(1.3); }}
                to {{ transform: scale(1.3); }}
            }}
            @keyframes contract {{
                from {{ transform: scale(1.3); }}
                to {{ transform: scale(1); }}
            }}
            
            .breathing-circle {{
                background-color: {BREATHING_COLORS[st.session_state.breathing_step]};
                padding: 40px;
                border-radius: 50%;
                text-align: center;
                width: 200px;
                height: 200px;
                margin: 0 auto;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                font-weight: bold;
                {animation_css}
            }}
        </style>
        
        <div class="breathing-circle">
            {BREATHING_STATES[st.session_state.breathing_step]}
        </div>
        """, unsafe_allow_html=True)
        
        # Show countdown for current breathing state
        st.markdown(f"<h2 style='text-align: center; margin-top: 20px;'>{st.session_state.breathing_timer}s</h2>", unsafe_allow_html=True)
        
        # Show progress through the cycles
        cycle_progress = min(st.session_state.breathing_count + 1, MAX_CYCLES)
        st.caption(f"Cycle {cycle_progress}/{MAX_CYCLES}")
        
        # Progress bar
        if st.session_state.breathing_active:
            progress_pct = ((st.session_state.breathing_count * 3) + st.session_state.breathing_step) / (MAX_CYCLES * 3)
            st.progress(progress_pct)
    
    with col2:
        st.markdown("### 4-7-8 Technique")
        st.markdown("- **Inhale** for 4 seconds")
        st.markdown("- **Hold** for 7 seconds")
        st.markdown("- **Exhale** for 8 seconds")
        st.markdown("- Repeat 4 times")
        
        if st.session_state.breathing_active:
            status = "🟢 Active"
        else:
            status = "⚪ Inactive"
        st.markdown(f"**Status:** {status}")
    
    # Control buttons
    col1, col2 = st.columns(2)
    with col1:
        if not st.session_state.breathing_active:
            if st.button("Start Exercise", use_container_width=True):
                start_breathing_exercise()
        else:
            if st.button("Pause Exercise", use_container_width=True):
                st.session_state.breathing_active = False
    
    with col2:
        if st.button("Reset Exercise", use_container_width=True):
            reset_breathing_exercise()
    
    # If exercise complete, show completion message
    if st.session_state.breathing_active and st.session_state.breathing_count >= MAX_CYCLES:
        st.success("🎉 Exercise complete! You've finished all 4 cycles.")
        reset_breathing_exercise()

def start_breathing_exercise():
    """Start the breathing exercise"""
    st.session_state.breathing_active = True
    if st.session_state.breathing_start_time is None:
        st.session_state.breathing_start_time = datetime.now()
    st.session_state.breathing_step_start_time = datetime.now()

def reset_breathing_exercise():
    """Reset the breathing exercise"""
    st.session_state.breathing_active = False
    st.session_state.breathing_step = 0
    st.session_state.breathing_count = 0
    st.session_state.breathing_timer = BREATHING_TIMES[0]
    st.session_state.breathing_start_time = None
    st.session_state.breathing_step_start_time = None

def update_breathing_timer():
    """Update the breathing timer based on current time"""
    if not st.session_state.breathing_active or st.session_state.breathing_step_start_time is None:
        return
    
    # Calculate elapsed time for current step
    now = datetime.now()
    elapsed_seconds = (now - st.session_state.breathing_step_start_time).total_seconds()
    current_step_duration = BREATHING_TIMES[st.session_state.breathing_step]
    
    # Update timer display
    remaining = max(0, round(current_step_duration - elapsed_seconds))
    st.session_state.breathing_timer = remaining
    
    # If step is complete, move to next step
    if remaining <= 0:
        advance_breathing_step()

def advance_breathing_step():
    """Advance to the next breathing step"""
    st.session_state.breathing_step = (st.session_state.breathing_step + 1) % 3
    st.session_state.breathing_step_start_time = datetime.now()
    st.session_state.breathing_timer = BREATHING_TIMES[st.session_state.breathing_step]
    
    # If we've completed a full cycle (after breathing out)
    if st.session_state.breathing_step == 0:
        st.session_state.breathing_count += 1
        
    # Stop after MAX_CYCLES
    if st.session_state.breathing_count >= MAX_CYCLES:
        st.session_state.breathing_active = False