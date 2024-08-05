```caffeinate -i docker run --name star-ways-container -it my-app /bin/bash```

### When in Docker you want to build the image
```docker build  -t starways:latest .```

### When you want to generate a container to build the image
```caffeinate -i docker run --name starwayscontainer -it my-app /bin/bash```

### When you want to run only the container
``` caffeinate -i docker exec -it starwayscontainer /bin/bash ```

--- Folder Structure ---
.DS_Store
Dockerfile
README.md
alien-icon-damage.png
alien-icon.avif
alien-icon.png
bg-space.jpg
blackhole.jpg
constants.py
[docs]
    └── .project_structure_ignore
main.py
[npyfiles]
    ├── 5013658704q_table.npy
    ├── 5014805584q_table.npy
    ├── 5019704496q_table.npy
    ├── 5041905104q_table.npy
    ├── 5047082448q_table.npy
    ├── 5048786000q_table.npy
    ├── 5054995920q_table.npy
    ├── 5073099856q_table.npy
    ├── 5074574416q_table.npy
    └── q_table.npy
q_learning.py
q_table.npy
requirements.txt
starways_env.py
ufo.webp


--- File: Dockerfile ---
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

## Video Demonstration
[![Watch the video](https://img.youtube.com/vi/sg5AlEG2gwc/maxresdefault.jpg)](https://youtu.be/sg5AlEG2gwc))
