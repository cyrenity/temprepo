FROM python:3-alpine

WORKDIR /usr/app

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./ 
COPY tasks.py ./ 

#CMD [ "python", "./server.py" ]