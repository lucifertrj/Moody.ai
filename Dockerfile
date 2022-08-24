FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -c "import tensorflow"

COPY . .

EXPOSE 5000

CMD [ "flask","run","--host=0.0.0.0","--port=5000" ]