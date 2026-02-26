from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables at the entry point
load_dotenv()

# Import the database module to initialize Supabase
import database

app = FastAPI(title="AI Voice Chatbot API")

# Add CORS middleware to allow requests from frontend clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Voice Chatbot API"}

@app.get("/health")
async def health_check():
    # Basic check to see if Supabase client is initialized
    supabase_status = "initialized" if database.supabase else "not_initialized"
    return {
        "status": "healthy",
        "supabase": supabase_status
    }
