# The db_utils.py file contains functions for interacting with our SQLite database.
# We use SQLite for its simplicity and ease of setup, making it perfect for prototyping and 
# small to medium-scale applications. Let's break down the key components of this file:
import sqlite3
from datetime import datetime

DB_NAME = "rag_app.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
# We start by importing the necessary modules and defining our database name. 
# The get_db_connection() function creates a connection to our SQLite database, setting 
# the row factory to sqlite3.Row for easier data access.



# Creating Database Tables
def create_application_logs():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS application_logs
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     session_id TEXT,
                     user_query TEXT,
                     geminai_response TEXT,
                     model TEXT,
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.close()

def create_document_store():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS document_store
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     filename TEXT,
                     upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.close()
# These functions create our two main tables:
# 1. application_logs: Stores chat history and model responses.
# 2. document_store: Keeps track of uploaded documents.


# Managing Chat Logs
def insert_application_logs(session_id, user_query, geminai_response, model):
    conn = get_db_connection()
    conn.execute('INSERT INTO application_logs (session_id, user_query, geminai_response, model) VALUES (?, ?, ?, ?)',
                    (session_id, user_query, geminai_response, model))
    conn.commit()
    conn.close()

def get_chat_history(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT user_query, geminai_response FROM application_logs WHERE session_id = ? ORDER BY created_at', (session_id,))
    messages = []
    for row in cursor.fetchall():
        messages.extend([
            {"role": "human", "content": row['user_query']},
            {"role": "ai", "content": row['geminai_response']}
        ])
    conn.close()
    return messages
# These functions handle inserting new chat logs and retrieving chat history for a given session.
# The chat history is formatted to be easily usable by our RAG system.


# Managing Document Records
def insert_document_record(filename):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO document_store (filename) VALUES (?)', (filename,))
    file_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return file_id

def delete_document_record(file_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM document_store WHERE id = ?', (file_id,))
    conn.commit()
    conn.close()
    return True

def get_all_documents():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, filename, upload_timestamp FROM document_store ORDER BY upload_timestamp DESC')
    documents = cursor.fetchall()
    conn.close()
    return [dict(doc) for doc in documents]
# These functions handle CRUD operations for document records:
# Inserting new document records
# Deleting document records
# Retrieving all document records

# Initialize the database tables
create_application_logs()
create_document_store()


