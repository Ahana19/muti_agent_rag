# Enterprise Multi-Agent RAG Platform

## Client

Acme Insurance (Fictional)

---

## Business Problem

Acme Insurance stores thousands of internal documents including:

- HR Policies
- Insurance Policies
- Employee Handbook
- Compliance Documents
- SOPs
- Technical Manuals

Employees spend a lot of time searching through these documents manually.

The company wants an AI assistant that can answer questions accurately using only company documents.

---

## Objectives

The application should:

- Allow secure login
- Upload PDF documents
- Search documents intelligently
- Answer questions using RAG
- Show citations for every answer
- Maintain chat history
- Log every interaction
- Evaluate AI responses
- Detect hallucinations
- Provide an admin dashboard

---

## Functional Requirements

### Authentication

- Login
- Logout
- JWT Authentication

---

### Document Management

- Upload PDFs
- Delete PDFs
- View uploaded files

---

### Chat

- Ask questions
- Retrieve relevant documents
- Generate answers
- Display citations

---

### Evaluation

- Measure faithfulness
- Measure groundedness
- Measure relevance
- Detect hallucinations

---

### Monitoring

- Response latency
- Number of requests
- Error logs

---

## Non Functional Requirements

- Fast responses
- Secure
- Modular
- Easy to maintain
- Dockerized
- Well documented