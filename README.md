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


## 🚀 Quick Start

Click the deploy button above and your app is live in seconds! Zero configuration needed - Railway handles everything automatically.

## 💻 Local Development

```bash
# Clone and setup
git clone git@github.com:shinypebble/railway-python-bottle-quickstart.git
cd railway-python-bottle-quickstart

# Create virtual environment (with uv - recommended)
uv venv --python 3.13
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Run locally
python main.py  # Development server on http://localhost:8080
```

## 🌐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port (auto-provided by Railway) | `8080` |
| `LOG_LEVEL` | Gunicorn log level | `info` |

Railway automatically provides PORT - no configuration needed!

## 🔧 Customization

**Add Dependencies:**
```toml
# In pyproject.toml
dependencies = [
    "bottle>=0.12.25",
    "gunicorn>=21.2.0",
    "your-package>=1.0.0",
]
```

**Add Routes:**
```python
# In main.py
@app.route('/api/users')
def users():
    return {'users': ['alice', 'bob']}
```


## 🚨 Troubleshooting

**App won't start?** → Check logs with `railway logs`  
**Dependencies failing?** → Clear cache with `railway up --no-cache`  
**Health check failing?** → Verify `/health` endpoint returns 200

## 📚 Resources

- [Bottle Documentation](https://bottlepy.org/docs/dev/)
- [Railway Documentation](https://docs.railway.com)

---

Made with 💎 by [Shiny Pebble](https://shiny-pebble.com/) • [MIT License](LICENSE)