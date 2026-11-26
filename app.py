import streamlit as st
import importlib
import answer_engine

# Reload the latest answer engine
importlib.reload(answer_engine)

# Page configuration
st.set_page_config(
    page_title="Smart Document Intelligence",
    page_icon="📄",
    layout="wide"
)

# Application heading
st.title("📄 Smart Document Intelligence")

st.write(
    "Ask questions and retrieve relevant information "
    "from your uploaded PDF documents."
)

st.divider()

# Question input
question = st.text_input(
    "Your question",
    placeholder="Ask something about your PDF..."
)

# Search button
if st.button("Search document", type="primary"):

    if question.strip():

        with st.spinner("Searching your documents..."):

            try:
                response = answer_engine.generate_answer(question)

                st.session_state["search_response"] = response
                st.session_state["search_question"] = question

            except Exception as error:
                st.error(f"Something went wrong: {error}")

    else:
        st.warning("Please enter a question.")

# Display search results
if "search_response" in st.session_state:

    response = st.session_state["search_response"]

    st.divider()
    st.header("🔍 Search Results")

    # Display question
    st.subheader("Your question")
    st.write(st.session_state["search_question"])

    # Display answer
    st.subheader("📖 Retrieved Answer")
    st.write(response.get("answer", "No answer found."))

    # Source pages
    pages = response.get("pages", [])

    st.subheader("📑 Source Pages")

    if pages:
        st.write(", ".join(map(str, pages)))
    else:
        st.write("No source pages found.")

    # Relevance score
    score = float(response.get("similarity", 0))

    st.subheader("📊 Relevance Score")
    st.progress(max(0.0, min(score, 1.0)))
    st.caption(f"Similarity: {score:.3f}")

    # Individual retrieved passages
    passages = response.get("passages", [])

    st.divider()
    st.subheader("Retrieved Passages")

    if passages:

        for index, passage in enumerate(passages, start=1):

            page = passage.get("page", "Unknown")
            text = passage.get("text", "")
            similarity = passage.get("similarity", 0)

            with st.expander(
                f"Passage {index} | Page {page} | Similarity {similarity:.3f}"
            ):
                st.write(text)

    else:
        st.info("No individual passages were returned.")

# Footer
st.divider()

st.caption(
    "Smart Document Intelligence | GenAI Portfolio Project"
)