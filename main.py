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


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    host = os.getenv("HOST", "0.0.0.0")
    debug = os.getenv("DEBUG", "False").lower() == "true"

    # Configure Gunicorn options based on debug mode
    gunicorn_options = {
        "loglevel": "debug" if debug else "info",
        "errorlog": "-",  # Log errors to stderr
        "accesslog": "-" if debug else None,  # Log access in debug mode only
        "capture_output": debug,  # Capture app output in debug mode
        "log_file": "-",  # Log to stdout instead of stderr
    }

    run(app, host=host, port=port, server="gunicorn", **gunicorn_options)
