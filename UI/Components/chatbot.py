import streamlit as st
from src.ai.chatbot import get_response
from src.ai.embedder import create_vector_store

st.set_page_config(page_title="CodeSense.AI", layout="wide")
st.title("💬 CodeSense.AI – Dev Assistant")

# Load or create vectorstore from dummy docs
demo_docs = [
    "CustomerService connects to OracleDB using xyz string.",
    "OrderProcessor exposes API /order/create and /order/status",
]
vectorstore = create_vector_store(demo_docs)

query = st.text_input("Ask me about your application:")

if query:
    with st.spinner("Thinking..."):
        answer = get_response(query, vectorstore)
        st.markdown("**Answer:**")
        st.success(answer)
