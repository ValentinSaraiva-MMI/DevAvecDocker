FROM python:3.9
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN useradd -m appuser
RUN chown -R appuser:appuser /server
EXPOSE 8000     
USER appuser
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
