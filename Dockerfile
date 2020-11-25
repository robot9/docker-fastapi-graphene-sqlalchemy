# Use an official Python runtime as an image
FROM python:3.8.1

# Copy all essentials file
COPY ./requirements.txt /var/www/requirements.txt

# Work Directory
WORKDIR /var/www

# Install requirements
RUN pip install -r requirements.txt

# Copy the rest
COPY . /var/www/

# Expose Port
EXPOSE 5000

# Start application
CMD uvicorn --host=0.0.0.0 --port=5000 app.main:app