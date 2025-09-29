"""Simple runtime configuration via environment variables."""
import os
APP_MODE = os.getenv("APP_MODE", "prod")
