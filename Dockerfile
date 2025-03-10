FROM python:3.9-slim

WORKDIR /CyberpsychBot

RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

# CMD ["gunicorn","-b","0.0.0.0:8000","CyberpsychBot.server:bot"] for prod (optional)
CMD ["python","CyberpsychBot/server.py"]