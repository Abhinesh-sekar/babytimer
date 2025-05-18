# tabs/music.py - Music suggestions tab

import streamlit as st

# Music options data
MUSIC_OPTIONS = [
    {"name": "Lo-Fi Beats", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk", "emoji": "🎧"},
    {"name": "Sumeru OST", "url": "https://www.youtube.com/watch?v=VrP3lO3aGDg&list=RDVrP3lO3aGDg&start_radio=1", "emoji": "🌿"},
    {"name": "Classical Relax Music", "url": "https://www.youtube.com/watch?v=jKL2vCGdkuE", "emoji": "🎻"},
    {"name": "Adorable Puppies", "url": "https://www.youtube.com/watch?v=VAH-ixdFWFs", "emoji": "🐶"}
]

def render_music_tab():
    """Render the music tab content"""
    st.subheader("Music and videos for Relaxation")
    
    for i, option in enumerate(MUSIC_OPTIONS):
        st.markdown(f"### {option['emoji']} {option['name']}")
        st.markdown(f"[Open in a new tab]({option['url']})")
        st.markdown("---")