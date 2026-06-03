import streamlit as st

def header_home():
    
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    
    st.markdown(f"""
            
            <div style="display:flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom:30px; margin-top: 30px;">
                <img src='{logo_url}' style='height: 100px; filter: drop-shadow(0 4px 12px rgba(0,0,0,0.3));' />
                <h1 style='text-align: center; color: #FFFFFF; text-shadow: 0 2px 20px rgba(0,0,0,0.2);'>SNAP<br/>CLASS</h1>
                <p style="text-align: center; color: rgba(255,255,255,0.8); font-size: 1.1rem; font-weight: 400; letter-spacing: 0.05em; margin-top: 8px;">
                    AI-Powered Smart Attendance System
                </p>
            </div>
                
                """, unsafe_allow_html=True)
    
def header_dashboard():
    
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    
    st.markdown(f"""
            
            <div style="display:flex; align-items: center; justify-content: center; gap: 14px;">
                <img src='{logo_url}' style='height: 70px; filter: drop-shadow(0 2px 8px rgba(108,99,255,0.3));' />
                <div>
                    <h2 style='text-align: left; margin: 0 !important; background: linear-gradient(135deg, #6C63FF, #4F46E5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.6rem !important;'>SNAP<br/>CLASS</h2>
                </div>
            </div>
                
                """, unsafe_allow_html=True)