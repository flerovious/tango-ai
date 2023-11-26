import streamlit as st
from views.logo import render_logo


# from llama_inery_engine imdex import VectorStoreIndex
# from llama_index.quport CitationQueryEngine


st.set_page_config(page_title="Chem 1A Assistant")
render_logo()
st.sidebar.markdown("### Configurations")

option = st.sidebar.radio(
    'Choose your chatbot mode',
    ('General', 'Specific', 'Absurd')
)

if option == 'General':
    # Render general page
    st.write('You selected General')
elif option == 'Specific':
    # Render specific page
    st.write('You selected Specific')
else:
    # Render absurd page
    st.write('You selected Absurd')
