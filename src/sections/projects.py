import streamlit as st
from personal_data.data import PROJECTS

def projects_section():
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")