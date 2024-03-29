FROM python:latest
WORKDIR /
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
EXPOSE 5000