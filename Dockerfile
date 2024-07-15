# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file (if you have one, otherwise this line can be omitted)
# COPY requirements.txt .

# Install any dependencies (if you have a requirements file)
# RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run the tests
CMD ["python", "-m", "unittest", "discover"]