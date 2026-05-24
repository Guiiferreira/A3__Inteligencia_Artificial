# components/sidebar.py
import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-title">☰ Menu</div>',
            unsafe_allow_html=True
        )

        pagina = option_menu(
            menu_title=None,

            options=[
                "Início",
                "Dashboard",
                "Análise de Cliente",
                "Métricas",
                "Dataset"
            ],

            icons=[
                "house",
                "bar-chart-line",
                "person-check",
                "graph-up",
                "database"
            ],

            default_index=0,

            styles={
                "container": {
                    "padding": "0",
                    "background-color": "#000000",
                    "box-shadow": "none",
                    "border": "none",
                },
                "icon": {
                    "color": "#94a3b8",
                    "font-size": "16px",
                },
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "2px 0px",
                    "padding": "10px 14px",
                    "border-radius": "8px",
                    "color": "#94a3b8",
                    "background-color": "#000000",
                    "--hover-color": "#111827",
                },
                "nav-link-selected": {
                    "background-color": "#000000",
                    "color": "white",
                    "font-weight": "600",
                    "border-left": "3px solid #ff4b4b",
                    "border-radius": "0px 8px 8px 0px",
                },
            }
        )

        st.markdown("""
            <style>
                div[data-testid="stSidebar"] div.menu,
                div[data-testid="stSidebar"] div.container-xxl,
                div[data-testid="stSidebar"] ul.nav-pills,
                div[data-testid="stSidebar"] ul.nav {
                    background-color: #000000 !important;
                    box-shadow: none !important;
                    border: none !important;
                    padding: 0 !important;
                }
            </style>
        """, unsafe_allow_html=True)

    return pagina