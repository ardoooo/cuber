FROM python:3.9

WORKDIR /script

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .

CMD ["python", "script.py"]
