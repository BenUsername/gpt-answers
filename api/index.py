import sys
import os

# Import the app directly from the api directory
from app_combined import app

# This is needed for Vercel
if __name__ == "__main__":
    app.run()

# Export the app for Vercel
app.debug = False 