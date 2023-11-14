# Use the official Python image
FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install pip requirements
RUN python -m pip install --no-cache-dir -r requirements.txt

# Download and set up chromedriver (Windows)
RUN Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/VERSION_NUMBER/chromedriver_win32.zip" -OutFile chromedriver.zip
RUN Expand-Archive -Path chromedriver.zip -DestinationPath C:\chromedriver
RUN Remove-Item chromedriver.zip
ENV PATH $env:PATH;C:\chromedriver

# Copy the current directory contents into the container at /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
