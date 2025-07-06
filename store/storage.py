from supabase import create_client, Client
from core.config import settings

url: str = settings.SUPABASE_S3_URL
key: str = settings.SUPABASE_S3_SECRET_KEY
supabase: Client = create_client(url, key)