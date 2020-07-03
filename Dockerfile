FROM python:3
WORKDIR /usr/src/app
COPY src/ ./
RUN pip install -r requirements.txt
ENV GOOGLE_APPLICATION_CREDENTIALS="/home/pi/centralperk-b3017fb16515.json"
CMD [ "python", "./extractor.py" ]