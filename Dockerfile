FROM python:3

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip &&\
    pip install --upgrade setuptools &&\
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 9898

CMD ["python", "main.py"]
