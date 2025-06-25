import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import re

load_dotenv()

def extract_video_id(link_or_id):
    """
    Extract YouTube video ID from full URL or return the ID if already given.
    """
    # Match common YouTube URL formats
    match = re.search(r"(?:v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})", link_or_id)
    if match:
        return match.group(1)
    elif len(link_or_id) == 11:
        return link_or_id
    else:
        return None


st.set_page_config(page_title="📺 YouTube Video Chatbot", layout="centered")

st.title("📺 YouTube Video Transcript Chatbot")
user_input_link = st.text_input("🔗 Enter YouTube Video Link or ID")
video_id = extract_video_id(user_input_link)

if user_input_link and not video_id:
    st.error("❌ Could not extract a valid YouTube video ID. Please check your link or ID.")


if video_id:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi', 'es', 'fr', 'de', 'ur', 'ta', 'bn'])
        transcript = " ".join(chunk["text"] for chunk in transcript_list)

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.create_documents([transcript])

        # Embed and store in FAISS
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        vector_store = FAISS.from_documents(chunks, embeddings)
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

        # Define LLM & Prompt
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

        prompt = PromptTemplate(
            template="""
            You are a helpful assistant.
            Answer ONLY from the provided transcript context.
            If the context is insufficient, just say you don't know.

            {context}
            Question: {question}
            """,
            input_variables=["context", "question"]
        )

        # Chain setup
        def format_docs(retrieved_docs):
            return "\n\n".join(doc.page_content for doc in retrieved_docs)

        parallel_chain = RunnableParallel({
            'context': retriever | RunnableLambda(format_docs),
            'question': RunnablePassthrough()
        })

        parser = StrOutputParser()
        main_chain = parallel_chain | prompt | llm | parser

        # Chat input
        user_input = st.text_input("💬 Ask something about the video:")

        if user_input:
            with st.spinner("Generating answer..."):
                result = main_chain.invoke(user_input)
                st.success(result)

    except TranscriptsDisabled:
        st.error("❌ Transcripts are disabled for this video.")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

