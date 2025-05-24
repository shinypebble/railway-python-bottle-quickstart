# main.py
from bottle import Bottle, route, run
import os

# Debug: Print environment info at startup
print(f"Starting app with PORT env var: {os.getenv('PORT', 'NOT SET')}")
print(f"All environment variables: {[k for k in os.environ.keys() if 'PORT' in k]}")

app = Bottle()


@app.route("/")
def index():
    port_info = os.getenv('PORT', 'NOT SET')
    return f"""
    <h1>Hello from Bottle on Railway! 🚄</h1>
    <p>This is a minimal Python Bottle application template.</p>
    <p>Deploy your own in minutes!</p>
    <hr>
    <p><small>Debug: PORT env var = {port_info}</small></p>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy", 
        "message": "Bottle app is running",
        "port": os.getenv('PORT', 'NOT SET'),
        "pid": os.getpid()
    }


# For local development only - Railway uses gunicorn directly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    # Simple development server
    run(app, host="localhost", port=port, debug=debug)
