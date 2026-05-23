import streamlit as st

def _render_footer():
    st.markdown("""
        <div style="margin-top: 3rem; padding: 1.2rem 0; border-top: 1px solid rgba(100, 80, 160, 0.2); display: flex; flex-direction: column; align-items: center; gap: 4px;">
            <p style="margin:0; font-size: 0.85rem; color: rgba(80, 60, 140, 0.7); letter-spacing: 0.5px;">
                © 2026 SnapClass · AI-Powered Smart Attendance
            </p>
            <p style="margin:0; font-size: 0.75rem; color: rgba(80, 60, 140, 0.5);">
            </p>
        </div>
    """, unsafe_allow_html=True)

def footer_home():
    _render_footer()

def footer_dashboard():
    _render_footer()