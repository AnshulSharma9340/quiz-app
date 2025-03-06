import os
from app import create_app

app = create_app()

if __name__ =='__main__':
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable or default to 8000
    app.run(port=port, debug = True)
