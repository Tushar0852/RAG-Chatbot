from pydantic import BaseModel, Field
from datetime import datetime

# We don’t need Enum anymore since you are using only one model
MODEL_NAME = "gemini-2.5-flash"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: str = Field(default=MODEL_NAME)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: str = Field(default=MODEL_NAME)

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int
