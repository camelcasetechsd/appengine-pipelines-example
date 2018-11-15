#!/bin/bash

source /google-cloud-sdk/path.bash.inc

echo "Google auth..."
GCLOUD_USER=`gcloud auth list --filter=status:ACTIVE --format="value(account)"`
printf "GCLOUD_USER: %s\n" $GCLOUD_USER
if [ -z "$GCLOUD_USER" ]
then
    gcloud auth login
fi

echo "Starting AppEngine deploy..."
printf "APPENGINE_PROJECT_ID: %s\n" $APPENGINE_PROJECT_ID
if [ -z "$APPENGINE_PROJECT_ID" ]
then
    echo "You must obtain an AppEngine PROJECT_ID [https://console.cloud.google.com/appengine] and place it in .env before running this!"
else
    gcloud app deploy app-deploy.yaml --project $APPENGINE_PROJECT_ID --version 1 --promote
fi
