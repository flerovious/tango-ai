import streamlit as st
from enums import Expertise, InputField, OutputField
from engine import TangoEngine
from utils import TANGO_ENGINE_ID, get_expertise_description
from citation import Citation
from typing import List

st.set_page_config(
    page_title="Tango AI",
    page_icon="💃",
    layout="wide",
)

st.sidebar.markdown("### ⚙️ Settings")
st.sidebar.selectbox("Expertise", [get_expertise_description(e) for e in Expertise])

st.markdown("# 💃 Tango AI")
st.markdown("Personalized teaching tool through effective guiding questions.")

# Initialize session state
for field in InputField:
    if field not in st.session_state:
        st.session_state[field] = ""

for field in OutputField:
    if field not in st.session_state:
        st.session_state[field] = ""

if TANGO_ENGINE_ID not in st.session_state:
    st.session_state[TANGO_ENGINE_ID] = TangoEngine(Expertise.INTRODUCTORY_CHEMISTRY)

input_validation = st.empty()
col1, col2 = st.columns(2)

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

if st.button("✏️ Generate Guiding Questions"):
    if not st.session_state[InputField.QUESTION]:
        input_validation.warning("Question cannot be empty")
    elif not st.session_state[InputField.OPTIONS]:
        input_validation.warning("Answer options cannot be empty")
    else:
        response = st.session_state[TANGO_ENGINE_ID].query(
            st.session_state[InputField.QUESTION],
            st.session_state[InputField.OPTIONS],
        )

        guiding_questions = response.response
        citations: List[Citation] = []
        for i, node in enumerate(response.source_nodes):
            page_label = node.node.metadata["page_label"]
            file_name = node.node.metadata["file_name"]
            file_path = (
                "/".join(node.node.metadata["file_path"].split("/")[6:])
                .replace(" ", "%20")
                .replace("!", "%21")
            )
            citations.append(
                Citation(
                    reference_index=i + 1,
                    page_label=page_label,
                    file_name=file_name,
                    url=f"https://github.com/flerovious/tango-ai/blob/main/src/{file_path}",
                )
            )

        # Set guiding questions and citations in session state
        st.session_state[OutputField.GUIDE] = guiding_questions
        st.session_state[OutputField.CITATIONS] = citations

        # Show guiding questions and citations
        st.write("## 📚 Guiding Questions")

        if OutputField.GUIDE in st.session_state:
            st.caption(st.session_state[OutputField.GUIDE])

        with st.expander("See citations"):
            if OutputField.CITATIONS in st.session_state:
                for citation in st.session_state[OutputField.CITATIONS]:
                    st.caption(
                        f"[[{citation.reference_index}] {citation.file_name} (page {citation.page_label})]({citation.url})"
                    )
