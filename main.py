# main.py
from bottle import Bottle, route, run
import os

app = Bottle()


@app.route("/")
def index():
    return """
    <h1>Hello from Bottle on Railway! 🚄</h1>
    <p>This is a minimal Python Bottle application template.</p>
    <p>Deploy your own in minutes!</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy", "message": "Bottle app is running"}


# For local development only - Railway uses gunicorn directly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    # Simple development server
    run(app, host="localhost", port=port, debug=debug)
