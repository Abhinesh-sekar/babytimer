import streamlit as st

def render_monkey_tab():
    """Render the monkey tab content with communication buttons"""
    # Clear any previous content
    st.empty()
    
    # Container for monkey tab content
    with st.container():
        st.subheader("you can always talk to your monkey in this break ;)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Telegram video call button
            telegram_url = "https://t.me/abhxnesh"  # Replace with actual username
            st.markdown(f'''
            <a href="{telegram_url}" target="_blank">
                <button style="
                    background-color: #0088cc;
                    color: white;
                    padding: 10px 24px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                ">
                    <span>📞 Telegram Video Call</span>
                </button>
            </a>
            ''', unsafe_allow_html=True)
        
        with col2:
            # WhatsApp chat button
            # Replace the number with your actual phone number including country code (no + sign)
            whatsapp_url = "https://wa.me/+919444305277"
            st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    background-color: #25D366;
                    color: white;
                    padding: 10px 24px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                ">
                    <span>💬 WhatsApp Chat</span>
                </button>
            </a>
            ''', unsafe_allow_html=True)
        
        st.markdown("---")
        st.write("Click the buttons above to connect with your monkey!")