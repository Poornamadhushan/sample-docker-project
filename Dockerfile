FROM python:3.10-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install packages from requirements.txt with increased timeout
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt

# Copy application files
COPY ./app .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]