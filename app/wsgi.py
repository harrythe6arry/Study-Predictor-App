from . import create_app
import os

app = create_app()  # Create the Flask app instance

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

