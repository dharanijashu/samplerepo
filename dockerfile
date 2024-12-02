FROM python:3.8-slim
WORKDIR /dockdir
COPY . .
RUN pip install pandas
CMD ["python", "app.py"]
