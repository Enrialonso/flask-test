FROM python:3.8-alpine
RUN apk update
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "./app.py" ]