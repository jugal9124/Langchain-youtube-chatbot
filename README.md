# 📺 YouTube Video Transcript Chatbot

This is a Streamlit-based chatbot application that allows users to interact with the transcript of any YouTube video. It uses OpenAI's GPT model, LangChain, FAISS vector search, and YouTube Transcript API to retrieve contextually accurate answers based on video content.

---

## 🚀 Features

- 🔗 Accepts YouTube **link or video ID**
- 🌐 Supports **multiple transcript languages** fallback (e.g. English, Hindi, Spanish)
- 🧠 Uses **LangChain** to augment LLM with retrieved transcript chunks
- 💬 Ask questions about the video content
- ⚡ Real-time answers powered by **OpenAI GPT-4o Mini**
- ✅ Automatic transcript fetching, chunking, embedding, and vector search

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) – for interactive UI
- [LangChain](https://www.langchain.com/) – for LLM pipeline
- [OpenAI](https://platform.openai.com/) – for LLM & Embeddings
- [FAISS](https://github.com/facebookresearch/faiss) – vector similarity search
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) – fetch YouTube video transcripts

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/jugal9124/Langchain-youtube-chatbot.git
cd youtube-transcript-chatbot
```

### 2. Run

```bash
streamlit run streamlit_app.py
```