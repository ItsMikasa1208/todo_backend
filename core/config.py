from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SUPABASE_S3_ACCESS_KEY : str
    SUPABASE_S3_SECRET_KEY : str
    SUPABASE_S3_URL : str
    SUPABASE_S3_REGION : str
    MONGODB_URI : str

settings = Settings()
