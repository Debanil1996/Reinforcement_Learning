# Use the official NVIDIA CUDA runtime image with Python support
FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run your Python script
CMD ["python3", "main.py"]
