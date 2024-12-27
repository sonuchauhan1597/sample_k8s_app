FROM python:3.13.1-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y curl

RUN pip install -r requirements.txt

COPY . .

# Expose the backend port
EXPOSE 5000

CMD ["python", "app.py"]
