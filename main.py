# main.py
from bottle import Bottle, route, run
import os


app = Bottle()


@app.route("/")
def index():
    return f"""
    <h1>Hello from Bottle on Railway! 🚄</h1>
    <p>This is a minimal Python Bottle application template.</p>
    <p>Deploy your own in minutes!</p>
    <hr>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "message": "Bottle app is running",
        "port": os.getenv("PORT", "NOT SET"),
        "log_level": os.getenv("LOG_LEVEL", "NOT SET"),
    }


# For local development only - Railway uses gunicorn directly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("LOG_LEVEL", "info").lower() == "debug"

    # Simple development server
    run(app, host="localhost", port=port, debug=debug)
