# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy the Python script and text files into the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# Create output directory
RUN mkdir -p /home/data/output

# Install Python dependencies (if needed). In this case, none are required.
# RUN pip install <any-required-dependencies>

# Set the command to run the Python script when the container starts
CMD ["python", "script.py"]
