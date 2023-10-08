FROM python:3.11-slim

WORKDIR /app/

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip && \
    python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
