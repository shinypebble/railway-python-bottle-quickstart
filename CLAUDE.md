# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a Railway template repository for a minimal Python Bottle web application. It's designed to be forked by Railway users for quick deployment of Python web services.

## Common Commands

### Local Development
```bash
# Setup virtual environment with uv (recommended)
uv venv --python 3.13
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Run the application locally
python main.py

# Run with custom environment variables
PORT=3000 DEBUG=True python main.py

# Test debug mode (enables verbose Gunicorn logging)
DEBUG=true PORT=3000 python main.py
```

### Deployment
```bash
# Deploy to Railway
railway up

# Set environment variables on Railway
railway variables set PORT=3000
railway variables set DEBUG=False
```

## Architecture

### Core Components
- **main.py**: Single-file Bottle application with two routes:
  - `/` - Main index route returning HTML
  - `/health` - JSON health check endpoint for Railway monitoring
  
### Configuration
- **pyproject.toml**: Modern Python packaging using setuptools, requires Python 3.13+
- **railway.json**: Railway deployment configuration using Railpack builder with Gunicorn as WSGI server
- Environment variables handled via `os.getenv()` with sensible defaults

### Key Design Decisions
1. Uses Railpack (not Nixpacks) for faster builds with uv package manager
2. Gunicorn configured to bind to `0.0.0.0:$PORT` for Railway compatibility
3. Health check endpoint returns JSON for Railway's health monitoring
4. Debug mode controlled via environment variable, defaulting to False for production safety

## Testing Changes

Since this is a template repository, ensure any modifications maintain:
1. Zero-configuration deployment capability on Railway
2. Compatibility with Railway's PORT environment variable
3. The health check endpoint at `/health` returning 200 status