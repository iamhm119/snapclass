import streamlit as st

def _render_footer():
    st.markdown("""
        <div style="
            margin-top: 4rem;
            padding: 1.5rem 0;
            border-top: 1px solid rgba(108, 99, 255, 0.1);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        ">
            <p style="margin:0; font-size: 0.8rem; color: #94A3B8; letter-spacing: 0.04em; font-weight: 500;">
                © 2026 SnapClass · AI-Powered Smart Attendance
            </p>
            <p style="margin:0; font-size: 0.7rem; color: #CBD5E1;">
                Built with Face Recognition & Voice AI
            </p>
        </div>
    """, unsafe_allow_html=True)

def footer_home():
    _render_footer()

def footer_dashboard():
    _render_footer()