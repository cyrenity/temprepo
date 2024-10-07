FROM python:3

WORKDIR /usr/app

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./ 

CMD [ "python", "./server.py" ]