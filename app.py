import streamlit as st
from backend.rag import get_contextual_response, create_index
from backend.sentiment import analyze_sentiment

st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Support Chat")

# Run once to create index
if "index_created" not in st.session_state:
    create_index()
    st.session_state.index_created = True

query = st.text_input("Ask a mental health question:")

if query:
    response = get_contextual_response(query)
    sentiment = analyze_sentiment(query)

    st.markdown("**🤖 AI Response:**")
    st.success(response)

    st.markdown("**🧭 Sentiment of Your Message:**")
    st.info(sentiment)

