# Text-to-SQL Clarification Engine

A natural language database querying system that converts user questions into SQL queries and asks clarification questions when the user's request is ambiguous or incomplete.

## Project Status

🚧 Under active development.

## Problem Statement

Writing SQL queries can be difficult for users who are not familiar with relational databases.

A natural language interface can make database querying easier by allowing users to describe what they want in plain English.

However, natural language queries can be ambiguous or incomplete.

For example:

> Show me the students who scored highest.

The system may need additional information such as:

- Which subject?
- Which semester?
- How many students should be displayed?

The goal of this project is to build a system that understands natural language questions, identifies ambiguity when necessary, asks appropriate clarification questions, and generates a valid SQL query.

## Planned Features

- Natural language query input
- Database schema understanding
- Text-to-SQL generation
- Ambiguity detection
- Clarification question generation
- User clarification handling
- SQL validation
- Safe SQL execution
- Query result display
- Error handling
- Query history

## Technology Stack

- Python
- FastAPI
- MySQL
- SQL
- Large Language Model
- HTML
- CSS
- JavaScript

## Project Structure

The project structure will evolve as development progresses.

## Project Status

Initial project setup.