# AI Voice Chatbot

A full-stack AI voice chatbot project with a React frontend and a FastAPI backend.

## Project Structure

- `/frontend`: React (Vite) frontend application.
- `/backend`: FastAPI backend server.
- `/docs`: Project documentation.

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be running at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the React app:
   ```bash
   npm run dev
   ```
   The frontend will be running at `http://localhost:5173`.

## Technologies

- **Frontend**: React, Vite
- **Backend**: Python, FastAPI
- **Package Manager**: npm (frontend), pip (backend)
