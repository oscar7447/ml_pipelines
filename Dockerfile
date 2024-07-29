FROM python:3.11
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /app/test.py

COPY . ./app 


