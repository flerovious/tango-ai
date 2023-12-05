import streamlit as st
from enums import Expertise, InputField, OutputField

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
for field in InputField:
    if field not in st.session_state:
        st.session_state[field] = ""

# uncomment this when citations and guiding questions are generated (work for integrating with backend)
# for field in OutputField:
#     if field not in st.session_state:
#         st.session_state[field] = ""

if OutputField.CITATIONS not in st.session_state:
    # replace this with empty string and add citations as they are generated on button click
    st.session_state[OutputField.CITATIONS] = "[1] Citation placeholder"
if OutputField.GUIDE not in st.session_state:
    # replace this with empty string and add guiding questions as they are generated on button click
    st.session_state[OutputField.GUIDE] = "Guiding questions will appear here"

input_validation = st.empty()
col1, col2, col3 = st.columns(3)

with col1:
    st.session_state[InputField.QUESTION] = st.text_area(
        "**Question**",
        value=st.session_state[InputField.QUESTION],
        placeholder="Enter the full question",
    ).strip()

with col2:
    st.session_state[InputField.OPTIONS] = st.text_area(
        "**Answer Options**",
        value=st.session_state[InputField.OPTIONS],
        placeholder="Enter possible answer options",
    ).strip()

with col3:
    st.session_state[InputField.ANSWER] = st.text_area(
        "**Answer**",
        value=st.session_state[InputField.ANSWER],
        placeholder="Enter the correct answer",
    ).strip()

if st.button("✏️ Generate Guiding Questions"):
    if not st.session_state[InputField.QUESTION]:
        input_validation.warning("Question cannot be empty")
    elif not st.session_state[InputField.OPTIONS]:
        input_validation.warning("Answer options cannot be empty")
    elif not st.session_state[InputField.ANSWER]:
        input_validation.warning("Answer cannot be empty")
    else:
        st.write("## 📚 Guiding Questions")
        if OutputField.GUIDE in st.session_state:
            st.caption(st.session_state[OutputField.GUIDE])

        # Show citations in accordion
        with st.expander("See citations"):
            if OutputField.CITATIONS in st.session_state:
                st.caption(st.session_state[OutputField.CITATIONS])
