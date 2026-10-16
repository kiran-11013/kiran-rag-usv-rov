
# 1. Use Python 3.12
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Install uv
RUN pip install --no-cache-dir uv

# 4. Copy dependency files
COPY pyproject.toml uv.lock ./

# 5. Install Python dependencies
RUN uv sync --frozen --no-dev --no-install-project

# 6. Copy application code
COPY api.py app.py ./
COPY src/ ./src/

# 7. Define the API port
EXPOSE 8000

# 8. Start FastAPI
CMD ["/app/.venv/bin/python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
