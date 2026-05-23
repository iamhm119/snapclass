import streamlit as st

def _render_footer():
    st.markdown("""
        <div style="margin-top: 3rem; padding: 1.2rem 0; border-top: 1px solid rgba(255,255,255,0.1); display: flex; flex-direction: column; align-items: center; gap: 4px;">
            <p style="margin:0; font-size: 0.85rem; color: rgba(255,255,255,0.5); letter-spacing: 0.5px;">
                © 2026 SnapClass · AI-Powered Smart Attendance
            </p>
            <p style="margin:0; font-size: 0.75rem; color: rgba(255,255,255,0.3);">
                v1.0.0 · All rights reserved
            </p>
        </div>
    """, unsafe_allow_html=True)

def footer_home():
    _render_footer()

def footer_dashboard():
    _render_footer()