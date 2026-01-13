import streamlit as st
from query import answer_question

st.set_page_config(page_title="Internal Knowledge Assistant")

st.title("🤖 RoboQuery")

question = st.text_input("Good day to you! Ask me a question about our company policies:")

if question:
    with st.spinner("Searching knowledge base..."):
        answer = answer_question(question)
        st.markdown("### Answer")
        st.write(answer)
