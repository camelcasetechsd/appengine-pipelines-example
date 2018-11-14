#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Set root directory
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Check GAE_DIR is set
if [ -z "${GAE_DIR}" ]; then
  echo "GAE_DIR must be set to a directory containing Google App Engine binaries (including dev_appserver.py, etc)"
  exit 1
fi

# Install project dependencies
echo "Installing project dependencies with pip..."
rm -fr libs/*
pip install -r requirements.txt -t ./libs

# Run dev server
echo "Running dev server"
"${GAE_DIR}/dev_appserver.py" ${DIR}/app.yaml --skip_sdk_update_check --log_level=info --dev_appserver_log_level=error --datastore_path ${DATASTORE_PATH} --host 0.0.0.0 --admin_host 0.0.0.0 --port 9080 --admin_port 9000
