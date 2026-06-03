import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = (
        f"<div style=\""
        "background: white;"
        "border-left: 5px solid #6C63FF;"
        "padding: 1.5rem 1.75rem;"
        "border-radius: 1rem;"
        "border: 1px solid rgba(108, 99, 255, 0.1);"
        "margin-bottom: 1rem;"
        "box-shadow: 0 2px 12px rgba(108, 99, 255, 0.06);"
        "transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);"
        "\">"
        f"<h3 style=\"margin:0; color: #1a1a2e; font-size: 1.35rem; font-weight: 700;\">{name}</h3>"
        "<p style=\"color:#64748b; margin: 10px 0; font-size: 0.9rem;\">"
        "Code: <span style=\""
        "background: linear-gradient(135deg, #EEF2FF, #E0E7FF);"
        "color: #4F46E5;"
        "padding: 3px 10px;"
        "border-radius: 6px;"
        "font-weight: 600;"
        "font-size: 0.85rem;"
        f"\">{code}</span>"
        "&nbsp;&middot;&nbsp; Section: <span style=\"font-weight: 600; color: #334155;\">"
        f"{section}</span>"
        "</p>"
    )
    
    if stats:
        html += "<div style=\"display:flex; gap:10px; flex-wrap:wrap; margin-top: 8px;\">"
        for icon, label, value in stats:
            html += (
                "<div style=\""
                "background: linear-gradient(135deg, #F5F3FF, #EDE9FE);"
                "padding: 6px 14px;"
                "border-radius: 10px;"
                "font-size: 0.85rem;"
                "color: #4F46E5;"
                "font-weight: 500;"
                "display: flex;"
                "align-items: center;"
                "gap: 4px;"
                f"\">{icon} <b style=\"color: #1a1a2e !important;\">{value}</b> {label}</div>"
            )
        
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()