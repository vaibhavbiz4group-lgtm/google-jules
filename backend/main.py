from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"status": "healthy"}
