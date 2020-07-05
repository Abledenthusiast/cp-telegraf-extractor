FROM arm32v7/python:3 
WORKDIR /usr/src/app
COPY src/ ./
RUN pip install -r requirements.txt
ARG app_creds="./centralperk-b3017fb16515.json"
copy $app_creds ./GCP_CREDS 
ENV GOOGLE_APPLICATION_CREDENTIALS="./GCP_CREDS"
CMD [ "python", "./extractor.py" ]
