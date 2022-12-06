FROM tiangolo/uvicorn-gunicorn:python3.9

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .
ENTRYPOINT ["streamlit", "run", "./fraud_detection_app.py", "--server.port=8501", "--server.address=0.0.0.0"]