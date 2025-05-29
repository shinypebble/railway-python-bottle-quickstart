# Deploy and Host Bottle on Railway

 [Bottle](https://bottlepy.org/docs/dev/) is a fast, simple and lightweight WSGI micro web-framework for Python. Perfect for building small web applications, REST APIs, and prototypes with minimal overhead and zero dependencies beyond the Python standard library.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/template/e2fvmQ?referralCode=rq6lF8)

## About Hosting Bottle

Hosting Bottle applications requires a WSGI server for production deployments. This template provides a pre-configured setup with Gunicorn as the WSGI server, automatic port binding, health check endpoints, and environment variable configuration. Railway handles the infrastructure automatically - no server management, manual scaling, or complex deployment pipelines needed. Just push your code and Railway builds, deploys, and scales your Bottle app instantly.

## Common Use Cases

- Quick API prototypes and microservices
- Lightweight webhook handlers and integrations  
- Simple REST APIs that need to scale
- Learning Python web development
- Minimal web scrapers and data processors

## Dependencies for Bottle Hosting

- Python 3.13+ runtime environment
- Gunicorn WSGI server for production serving
- Environment variable support for configuration
- Health check endpoint for monitoring

### Deployment Dependencies

- [Bottle Documentation](https://bottlepy.org/docs/dev/) - Framework documentation and tutorials
- [Gunicorn Documentation](https://docs.gunicorn.org) - WSGI server configuration guide
- [Railway Python Guide](https://docs.railway.com/guides/python) - Platform-specific Python deployment tips

### Implementation Details

This template includes a minimal `main.py` with two routes:

```python
# Health check endpoint for Railway monitoring
@app.route('/health')
def health_check():
    return {"status": "healthy", "timestamp": time.time()}

# Main route
@app.route('/')
def index():
    return '<h1>Hello from Bottle!</h1>'
```

The app automatically binds to Railway's provided PORT environment variable with IPv4/IPv6 dual-stack support.

## Why Deploy Bottle on Railway?

Railway is a singular platform to deploy your infrastructure stack. Railway will host your infrastructure so you don't have to deal with configuration, while allowing you to vertically and horizontally scale it.

By deploying Bottle on Railway, you are one step closer to supporting a complete full-stack application with minimal burden. Host your servers, databases, AI agents, and more on Railway.

## ✨ Features

- **Python 3.13** - Latest stable Python version
- **Bottle** - Lightweight WSGI micro web-framework
- **Gunicorn** - Production-ready Python WSGI HTTP Server
- **uv** - Ultra-fast Python package manager
- **Health Check** - Built-in `/health` endpoint for monitoring
- **Environment Configuration** - Easy configuration through environment variables
- **Zero Config Deployment** - Works out of the box with Railway

## 🚀 Deploy

### One-Click Deploy

Click the button above to deploy directly to Railway!

### Manual Deploy

```bash
# Install Railway CLI
# https://docs.railway.com/guides/cli

# Deploy to Railway
railway login
railway link
railway up
```

## 💻 Local Development

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (optional, but recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone git@github.com:shinypebble/railway-python-bottle-quickstart.git
   cd railway-python-bottle-quickstart
   ```

2. **Create a virtual environment**
   
   Using uv (recommended):
   ```bash
   uv venv --python 3.13
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
   
   Or using standard Python:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   
   Using uv (recommended):
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install -e .
   ```

4. **Run the application**
   
   Development server:
   ```bash
   python main.py
   ```
   
   Production-like with Gunicorn:
   ```bash
   gunicorn main:app --bind "0.0.0.0:8080"
   ```

5. **Visit** http://localhost:8080

## 🌐 Environment Variables

Configure your application using these environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Port number for the server (automatically provided by Railway) | `8080` |
| `LOG_LEVEL` | Gunicorn log level (debug, info, warning, error, critical) | `info` |

### Setting Environment Variables

**Local Development:**
```bash
# Application defaults to port 8080 if PORT not set
python main.py

# Or specify a custom port
PORT=3000 python main.py

# Enable debug mode
DEBUG=True python main.py
```

**On Railway:**
Railway automatically provides the PORT variable - you don't need to set it! Only configure other variables as needed:
```bash
# Only set DEBUG if needed (defaults to False for production)
railway variables set DEBUG=False
```

## 📦 Adding Dependencies

1. **Add to `pyproject.toml`:**
   ```toml
   dependencies = [
       "bottle>=0.12.25",
       "gunicorn>=21.2.0",
       "your-package>=1.0.0",
   ]
   ```

2. **Update your local environment:**
   ```bash
   uv sync
   # or
   pip install -e .
   ```

Railway automatically detects and installs dependencies during deployment.

## 🏗️ Project Structure

```
railway-python-bottle-quickstart/
├── README.md          # This file
├── pyproject.toml     # Python project configuration
├── uv.lock           # Locked dependencies (auto-generated)
├── railway.json       # Railway deployment configuration
├── .gitignore        # Git ignore rules
└── main.py           # Application entry point
```

## 🔧 Customization

### Modify the App

Edit `main.py` to add your routes and application logic:

```python
@app.route('/api/users')
def users():
    return {'users': ['alice', 'bob']}
```

### Change Python Version

In `pyproject.toml`:
```toml
requires-python = ">=3.11"  # Change to your desired version
```

### Configure Deployment

Edit `railway.json` to customize deployment settings:
```json
{
  "deploy": {
    "numReplicas": 3,
    "healthcheckTimeout": 60
  }
}
```

## 📝 Railway Configuration

This template uses Railpack, Railway's modern build system that:
- Auto-detects Python projects
- Uses uv for fast dependency installation
- Provides optimal caching strategies
- Sets production-ready defaults

### Networking
- **Dual-stack support**: Gunicorn binds to `[::]` for both IPv4 (public) and IPv6 (private) traffic
- **Auto-provided PORT**: Railway automatically assigns and manages the PORT variable
- **Health checks**: Built-in `/health` endpoint for Railway monitoring

See `railway.json` for current configuration.

## 🚨 Troubleshooting

### Application won't start
- Check logs: `railway logs`
- Ensure the app binds to `0.0.0.0:$PORT` (Railway's provided PORT)
- Verify the app uses: `os.getenv('PORT', 8080)` for port configuration
- Verify Gunicorn is installed in dependencies

### Dependencies not installing
- Ensure `pyproject.toml` is valid
- Check Python version compatibility
- Clear build cache: `railway up --no-cache`

### Health check failing
- Verify `/health` endpoint returns 200 status
- Increase `healthcheckTimeout` if needed
- Check application startup time

## 📚 Resources

- [Bottle Documentation](https://bottlepy.org/docs/dev/)
- [Railway Documentation](https://docs.railway.com)
- [Railpack Documentation](https://railpack.com/)
- [Gunicorn Documentation](https://docs.gunicorn.org)
- [Python Packaging Guide](https://packaging.python.org)

## 📄 License

This template is open source and available under the [MIT License](LICENSE).

---

From 💎 [Shiny Pebble](https://shiny-pebble.com/) for the Railway community