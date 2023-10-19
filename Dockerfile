FROM python:3
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 8012
ENV FLASK_APP=main.py 
CMD ["python", "main.py"]