import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
                .stApp {
                    background: linear-gradient(135deg, #4F46E5 0%, #6C63FF 40%, #8B5CF6 100%) !important;
                    min-height: 100vh;
                }

                .stApp div[data-testid="stColumn"]{
                    background: rgba(255, 255, 255, 0.12) !important;
                    backdrop-filter: blur(20px) !important;
                    -webkit-backdrop-filter: blur(20px) !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    border: 1px solid rgba(255, 255, 255, 0.2) !important;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15) !important;
                    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
                    display: flex !important;
                    flex-direction: column !important;
                    align-items: center !important;
                    text-align: center !important;
                    }
                
                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-4px) !important;
                    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2) !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(160deg, #F0F2FF 0%, #E8EAFF 50%, #F5F3FF 100%) !important;
                    min-height: 100vh;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    


def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            :root {
                color-scheme: light;
            }

            .stApp {
                color-scheme: light;
                color: #1a1a2e;
            }

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            /* ---- Typography ---- */

            h1 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 800 !important;
                font-size: 3rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0.5rem !important;
                color: #FFFFFF;
            }
                

            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                font-size: 1.8rem !important;
                line-height: 1.2 !important;
                margin-bottom: 0.5rem !important;
                color: #1e1b4b;
            }
                
            h3 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                color: #1a1a2e;
            }
            
            h4, p, label, li {
                font-family: 'Inter', 'Outfit', sans-serif !important;
                color: #334155 !important;
            }

            /* ---- Buttons ---- */

            .stButton button {
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #6C63FF 0%, #4F46E5 100%) !important;
                color: white !important;
                padding: 8px 16px !important;
                border: none !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.85rem !important;
                letter-spacing: 0.02em !important;
                box-shadow: 0 4px 14px rgba(108, 99, 255, 0.35) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                white-space: nowrap !important;
            }

            .stButton button p, .stButton button span {
                color: inherit !important;
            }

            .stButton button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(108, 99, 255, 0.45) !important;
            }
            
            .stButton button:active {
                transform: translateY(0px) !important;
            }

            .stButton button[kind="secondary"] {
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%) !important;
                color: white !important;
                padding: 8px 16px !important;
                border: none !important;
                box-shadow: 0 4px 14px rgba(236, 72, 153, 0.35) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }

            .stButton button[kind="secondary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(236, 72, 153, 0.45) !important;
            }

            .stButton button[kind="tertiary"] {
                border-radius: 0.85rem !important;
                background: rgba(30, 30, 60, 0.9) !important;
                color: white !important;
                padding: 8px 16px !important;
                border: none !important;
                box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }

            .stButton button[kind="tertiary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
            }

            /* ---- Inputs ---- */

            input, .stTextInput > div > div > input {
                border-radius: 0.75rem !important;
                border: 2px solid #E2E8F0 !important;
                padding: 12px 16px !important;
                font-family: 'Inter', sans-serif !important;
                transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
                background: white !important;
            }

            input:focus, .stTextInput > div > div > input:focus {
                border-color: #6C63FF !important;
                box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15) !important;
                outline: none !important;
            }

            /* ---- Containers & Cards ---- */

            div[data-testid="stExpander"],
            .stContainer[data-testid="stVerticalBlockBorderWrapper"] {
                border-radius: 1rem !important;
                border: 1px solid rgba(108, 99, 255, 0.1) !important;
                background: white !important;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04) !important;
            }

            /* ---- Metrics ---- */

            div[data-testid="stMetric"] {
                background: white !important;
                padding: 1.25rem !important;
                border-radius: 1rem !important;
                border: 1px solid rgba(108, 99, 255, 0.08) !important;
                box-shadow: 0 2px 12px rgba(108, 99, 255, 0.06) !important;
            }

            div[data-testid="stMetric"] label {
                font-family: 'Inter', sans-serif !important;
                font-weight: 500 !important;
                font-size: 0.8rem !important;
                text-transform: uppercase !important;
                letter-spacing: 0.08em !important;
                color: #94A3B8 !important;
            }

            div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                font-size: 2rem !important;
                color: #1a1a2e !important;
            }

            /* ---- Dataframes ---- */

            .stDataFrame {
                border-radius: 1rem !important;
                overflow: hidden !important;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04) !important;
            }

            /* ---- Selectbox ---- */

            div[data-baseweb="select"] > div {
                border-radius: 0.75rem !important;
                border: 2px solid #E2E8F0 !important;
                background: white !important;
                overflow: hidden !important;
            }

            div[data-baseweb="select"] > div > div:last-child,
            div[data-baseweb="select"] div[role="combobox"] > div:last-child {
                background: transparent !important;
                border-left: none !important;
                box-shadow: none !important;
            }

            div[data-baseweb="select"] > div > div {
                border: none !important;
            }

            div[data-baseweb="select"] div[role="combobox"] {
                border: none !important;
                box-shadow: none !important;
            }

            div[data-baseweb="select"] svg {
                background: transparent !important;
            }

            /* ---- Dividers ---- */

            hr {
                border: none !important;
                height: 1px !important;
                background: linear-gradient(90deg, transparent, rgba(108, 99, 255, 0.15), transparent) !important;
                margin: 1.5rem 0 !important;
            }

            /* ---- Toast / Alerts ---- */

            div[data-testid="stAlert"] {
                border-radius: 0.85rem !important;
                font-family: 'Inter', sans-serif !important;
            }

            /* ---- Smooth page transitions ---- */

            .main .block-container {
                animation: fadeInUp 0.4s ease-out;
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(12px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* ---- Download button ---- */

            .stDownloadButton button {
                background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
                box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35) !important;
            }

            .stDownloadButton button:hover {
                box-shadow: 0 8px 25px rgba(16, 185, 129, 0.45) !important;
            }

            /* ---- Camera input ---- */
            
            div[data-testid="stCameraInput"] {
                border-radius: 1rem !important;
                overflow: hidden !important;
            }

        </style>  

                """
            ,unsafe_allow_html=True)