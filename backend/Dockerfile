FROM tiangolo/uvicorn-gunicorn:python3.9

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY . /app
EXPOSE 8000
#CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000" , "--reload"]
CMD ["python","main.py"]