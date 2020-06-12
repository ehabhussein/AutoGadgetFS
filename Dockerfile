FROM python
RUN apt-get update && apt-get install libenchant-dev -y
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
ADD . /app
RUN pip3 install ipython
RUN pip3 install cmd2

