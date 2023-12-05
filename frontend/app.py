import streamlit as st
from enum import Enum


class Expertise(Enum):
    INTRODUCTORY_CHEMISTRY = "Introductory Chemistry 🧪"


st.set_page_config(
    page_title="Tango AI",
    page_icon="💃",
    layout="wide",
)

st.sidebar.markdown("### ⚙️ Settings")
st.sidebar.selectbox("Expertise", [e.value for e in Expertise])

st.markdown("# 💃 Tango AI")
st.markdown(
    "The ultimate teaching planning tool for generating guided questions and answers for your students."
)

# Initialize session state
if "question" not in st.session_state:
    st.session_state["question"] = ""
if "answer" not in st.session_state:
    st.session_state["answer"] = ""
if "citations" not in st.session_state:
    # replace this with empty string and add citations as they are generated on button click
    st.session_state["citations"] = "[1] Citation placeholder"
if "guide" not in st.session_state:
    # replace this with empty string and add guiding questions as they are generated on button click
    st.session_state["guide"] = "Guiding questions will appear here"

input_validation = st.empty()
col1, col2 = st.columns(2)

with col1:
    st.session_state["question"] = st.text_area(
        "**Question**",
        value=st.session_state["question"],
        placeholder="Enter the full question with possible options",
    ).strip()

with col2:
    st.session_state["answer"] = st.text_area(
        "**Answer**",
        value=st.session_state["answer"],
        placeholder="Enter the correct answer",
    ).strip()

if st.button("✏️ Generate Guiding Questions"):
    if not st.session_state["question"] or not st.session_state["answer"]:
        input_validation.warning("Question and answer cannot be empty")
    else:
        st.write("## 📚 Guiding Questions")
        if "guide" in st.session_state:
            st.caption(st.session_state["guide"])

        # Show citations in accordion
        with st.expander("See citations"):
            if "citations" in st.session_state:
                st.caption(st.session_state["citations"])
