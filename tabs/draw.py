# tabs/draw.py - Drawing tab

import streamlit as st
from streamlit_drawable_canvas import st_canvas

def render_draw_tab():
    """Render the drawing tab content"""
    st.subheader("Quick Sketch")
    
    # Canvas for drawing
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=3,
        stroke_color="#000000",
        background_color="#ffffff",
        height=300,
        width=700,
        drawing_mode="freedraw",
        key="canvas",
    )
    
    st.caption("Draw whatever comes to mind. No pressure - this is just for fun!")
    
    if st.button("Clear Canvas", key="clear_canvas"):
        st.session_state.canvas_cleared = True
        st.rerun()