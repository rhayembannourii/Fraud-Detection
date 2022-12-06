FROM tiangolo/uvicorn-gunicorn:python3.9

WORKDIR /app
RUN pip install --upgrade pip
COPY ./streamlit_requirements.txt /app/streamlit_requirements.txt
RUN pip install -r /app/streamlit_requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY . /app
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["fraud_detection_app.py"]

#CMD ["python","./main.py"]
#ENTRYPOINT ["streamlit", "run", "./fraud_detection_app.py", "--server.port=8501", "--server.address=0.0.0.0"]