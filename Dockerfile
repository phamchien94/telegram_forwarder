FROM python:3.7.10-slim-stretch
COPY ./ /telegram_forwarder/
WORKDIR /telegram_forwarder/
RUN pip install -r requirement.txt
CMD ["python", "forwarder.py"]
