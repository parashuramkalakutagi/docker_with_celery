
FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /django_rest
COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /django_rest/
