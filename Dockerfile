FROM python:3
MAINTAINER Divyarams
WORKDIR app/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["app.py"]
ENTRYPOINT ["python3"]