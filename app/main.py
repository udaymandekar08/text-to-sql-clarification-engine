
from fastapi import FastAPI

app = FastAPI(
    title="Text-to-SQL Clarification Engine",
    description="A natural language interface for querying relational databases.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Text-to-SQL Clarification Engine API is running"
    }
