FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*.py ./

CMD [ "python", "./TestClickCountAPI.py", "--webappAddr", "http://34.245.196.183" ]
