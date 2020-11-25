#!/bin/bash

# Make sure the docker containers are running so we can access the database
# docker-compose up -d

# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate

read_var() {
  local ENV_FILE="${2:-./.env}"
  local VAR=$(grep $1 "$ENV_FILE" | xargs)

  IFS="=" read -ra VAR <<< "$VAR"
  echo ${VAR[1]} | tr -d '\r'
}

pip-3.8 install -r requirements.txt

export DB_USERNAME=$(read_var DB_USER)
export DB_PASSWORD=$(read_var DB_PASS)
export DB_DATABASE=$(read_var DB_NAME)
export DB_HOST=0.0.0.0
export MODE=$(read_var MODE)

# Run on a separate port instead
python3.8 /usr/local/bin/uvicorn --host=0.0.0.0 --port=5001 app.main:app