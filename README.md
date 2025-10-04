# 🤖 RAG Chatbot

A powerful Retrieval-Augmented Generation (RAG) chatbot built with FastAPI backend and Streamlit frontend, powered by Google's Gemini 2.5 Flash model and ChromaDB vector database.

## ✨ Features

- 📄 **Document Upload**: Support for PDF, DOCX, and HTML files
- 💬 **Interactive Chat Interface**: Real-time conversations with AI
- 🔍 **RAG Implementation**: Retrieval-Augmented Generation for accurate, context-aware responses
- 🗄️ **Vector Database**: ChromaDB for efficient document storage and retrieval
- 📊 **Session Management**: Track conversation history across sessions
- 🎯 **Model Selection**: Powered by Gemini 2.5 Flash
- 🗑️ **Document Management**: Upload, list, and delete documents easily

## 🏗️ Architecture

```
RAG Chatbot
├── Backend (FastAPI)
│   ├── Document Processing
│   ├── Vector Database (ChromaDB)
│   ├── RAG Chain (LangChain)
│   └── API Endpoints
│
└── Frontend (Streamlit)
    ├── Chat Interface
    ├── Document Upload
    └── Session Management
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API Key
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Tushar0852/RAG-Chatbot.git
cd RAG-Chatbot
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### Running the Application

#### Start the Backend (FastAPI)

```bash
# From the backend directory
uvicorn main:app --reload --port 8000
```

The backend API will be available at `http://localhost:8000`

#### Start the Frontend (Streamlit)

Open a new terminal and run:

```bash
# From the frontend directory
streamlit run streamlit_app.py
```

The Streamlit app will open automatically in your browser at `http://localhost:8501`

## 📁 Project Structure

```
RAG-Chatbot/
├── app/                          # Backend application
│   ├── main.py                   # FastAPI application
│   ├── langchain_utils.py        # RAG chain implementation
│   ├── chroma_utils.py           # ChromaDB utilities
│   ├── db_utils.py               # SQLite database utilities
│   ├── pydantic_models.py        # Data models
│   └── chroma_db/                # Vector database storage
│
├── frontend/                     # Streamlit frontend
│   ├── streamlit_app.py          # Main Streamlit app
│   ├── sidebar.py                # Sidebar component
│   ├── chat_interface.py         # Chat UI component
│   └── api_utils.py              # API communication
│
├── .env                          # Environment variables
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔧 API Endpoints

### Backend API (Port 8000)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat` | POST | Send a query and get AI response |
| `/upload-doc` | POST | Upload a document (PDF/DOCX/HTML) |
| `/list-docs` | GET | List all uploaded documents |
| `/delete-doc` | POST | Delete a specific document |

### Example API Request

```python
import requests

# Chat endpoint
response = requests.post(
    "http://localhost:8000/chat",
    json={
        "question": "What is this document about?",
        "model": "gemini-2.5-flash",
        "session_id": "optional-session-id"
    }
)
```

## 🛠️ Technologies Used

### Backend
- **FastAPI**: High-performance web framework
- **LangChain**: Framework for LLM applications
- **ChromaDB**: Vector database for document embeddings
- **Google Gemini 2.5 Flash**: Large Language Model
- **SQLite**: Session and log storage
- **PyPDF2**: PDF processing
- **python-docx**: DOCX processing
- **BeautifulSoup4**: HTML processing

### Frontend
- **Streamlit**: Interactive web application framework
- **Requests**: HTTP library for API calls

## 📝 Usage Guide

### 1. Upload Documents
- Click on "Choose a file" in the sidebar
- Select a PDF, DOCX, or HTML file
- Click "Upload" button
- Wait for confirmation

### 2. Chat with Your Documents
- Type your question in the chat input
- The AI will retrieve relevant context from uploaded documents
- Get accurate, context-aware responses

### 3. Manage Documents
- View all uploaded documents in the sidebar
- Click "Refresh Document List" to update
- Select a document and click "Delete" to remove it

### 4. View Response Details
- Expand the "Details" section after each response
- See the generated answer, model used, and session ID

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Tushar**
- GitHub: [@Tushar0852](https://github.com/Tushar0852)

## 🙏 Acknowledgments

- Google Gemini for the powerful LLM
- LangChain for the RAG framework
- ChromaDB for vector storage
- Streamlit for the amazing frontend framework

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
