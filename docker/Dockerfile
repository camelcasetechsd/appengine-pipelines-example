FROM debian:jessie

RUN apt-get -y update && \
    apt-get -y install build-essential curl bzip2 unzip mercurial git python-pip python-dev && \
    curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-223.0.0-linux-x86_64.tar.gz -o /gcloud.tar.gz && \
    tar -xzf /gcloud.tar.gz && \
    /google-cloud-sdk/install.sh --quiet && \
    /google-cloud-sdk/bin/gcloud components install app-engine-python --quiet && \
    apt-get remove python-openssl -y && \
    easy_install --upgrade pip && \
    apt-get clean

RUN chmod +x /google-cloud-sdk/platform/google_appengine/dev_appserver.py
