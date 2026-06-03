import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="text-align: center;">
                <p style="color: rgba(255,255,255,0.9) !important; font-size: 1.1rem; font-weight: 600; margin-bottom: 4px; letter-spacing: 0.02em;">🎓</p>
                <h2 style="color: white !important; font-size: 1.4rem !important; margin-bottom: 8px !important;">I'm a Student</h2>
                <p style="color: rgba(255,255,255,0.7) !important; font-size: 0.85rem; margin-bottom: 16px;">Login with FaceID · Enroll in courses · Track attendance</p>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='student_portal_btn'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <p style="color: rgba(255,255,255,0.9) !important; font-size: 1.1rem; font-weight: 600; margin-bottom: 4px; letter-spacing: 0.02em;">👨‍🏫</p>
                <h2 style="color: white !important; font-size: 1.4rem !important; margin-bottom: 8px !important;">I'm a Teacher</h2>
                <p style="color: rgba(255,255,255,0.7) !important; font-size: 0.85rem; margin-bottom: 16px;">AI attendance · Manage subjects · View analytics</p>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='teacher_portal_btn'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()