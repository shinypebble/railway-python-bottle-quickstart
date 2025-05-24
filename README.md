# Bottle on Railway

A minimal Python Bottle web application template, ready for instant deployment on Railway.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/bottle)

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
   git clone <your-repo-url>
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
   ```bash
   python main.py
   ```

5. **Visit** http://localhost:8080

## 🌐 Environment Variables

Configure your application using these environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Port number for the server | `8080` |
| `HOST` | Host address to bind to | `0.0.0.0` |
| `DEBUG` | Enable debug logging (verbose Gunicorn logs) | `False` |

### Setting Environment Variables

**Local Development:**
```bash
export PORT=3000
export DEBUG=True
python main.py
```

**On Railway:**
Environment variables can be configured in the Railway dashboard or using the CLI:
```bash
railway variables set PORT=3000
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

See `railway.json` for current configuration.

## 🚨 Troubleshooting

### Application won't start
- Check logs: `railway logs`
- Ensure `PORT` environment variable is used: `os.getenv('PORT', 8080)`
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