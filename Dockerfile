FROM python
RUN apt-get update && apt-get install libenchant-dev -y
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
ADD . /app
RUN pip3 install ipython
RUN pip3 install cmd2
RUN patch /usr/local/lib/python3.8/site-packages/usb/util.py pyusb_patches/pyusb_langid.patch
