import os
from dotenv import load_dotenv

# Load .env file if present
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)

class Config:
    ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = ENV == "development"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "5001"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Paths
    BASE_DIR = BASE_DIR
    TEST_IMAGES_DIR = os.path.join(BASE_DIR, "test_images")
    MODELS_DIR = os.path.join(BASE_DIR, "models")
    LOGS_DIR = os.path.join(BASE_DIR, "logs")

config = Config()
