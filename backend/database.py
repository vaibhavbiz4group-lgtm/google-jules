import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL", "")
key: str = os.getenv("SUPABASE_KEY", "")

# Initialize client only if credentials are present to avoid crashing if they're missing
# In production, you might want to require these.
supabase: Client = None
if url and key:
    supabase = create_client(url, key)
else:
    print("Warning: SUPABASE_URL or SUPABASE_KEY not found in environment variables.")

def get_supabase():
    return supabase
