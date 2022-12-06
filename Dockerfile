FROM tiangolo/uvicorn-gunicorn:python3.9

WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
COPY ./streamlit_requirements.txt streamlit_requirements.txt
RUN pip install -r requirements.txt
RUN pip install -r streamlit_requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . .
CMD ["python","./app/main.py"]
ENTRYPOINT ["streamlit", "run", "./fraud_detection_app.py", "--server.port=8501", "--server.address=0.0.0.0"]