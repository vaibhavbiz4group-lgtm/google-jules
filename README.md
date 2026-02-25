# AI Voice Chatbot Backend

An AI voice chatbot project with a FastAPI backend.

## Project Structure

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

## Technologies

- **Backend**: Python, FastAPI
- **Package Manager**: pip (backend)
