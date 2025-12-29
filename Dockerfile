FROM python:3.11-slim

WORKDIR /app

# Copy only what we need
COPY APP ./APP
COPY RUNTIME ./RUNTIME
COPY PHASE6 ./PHASE6
COPY ENRICHMENT ./ENRICHMENT
COPY OUTPUT ./OUTPUT
COPY OUTPUTS ./OUTPUTS

RUN pip install --no-cache-dir -r APP/requirements.txt

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "APP.app:app", "--host", "0.0.0.0", "--port", "8000"]
