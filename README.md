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

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API key
Create a .env file in the root folder:

```bash
OPENAI_API_KEY=your_openai_key_here
```


### 5. Run

```bash
streamlit run streamlit_app.py
```

---
### How It Works
1. User enters YouTube video link or ID.

2. App fetches the transcript using the YouTube Transcript API.

3. Transcript is split into chunks and embedded using OpenAI.

4. FAISS vector store is built for fast similarity search.

5. User types a question.

6. LangChain retrieves relevant chunks and feeds them to the LLM.

7. ChatGPT generates a context-aware response.
---

---
### 🌍 Language Support
The app tries English first (en), and falls back to Hindi (hi), Spanish (es), or others. You can customize supported languages easily.
---


### 📬 Contact
Made with ❤️ by Jugal Kishore
---
Let me know if you want:
- A sample `requirements.txt`
- `screenshot.png` placeholder image
- Deployed on Streamlit Cloud or HuggingFace Spaces

I can also write a `Dockerfile` or `app.py` version if you ever plan to host it!

---