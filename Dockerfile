FROM python:3

COPY . /image_classification_app

WORKDIR /image_classification_app

RUN make install

CMD ["python", "main.py"]
