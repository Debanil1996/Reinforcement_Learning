```caffeinate -i docker run --name star-ways-container -it my-app /bin/bash```

### When in Docker you want to build the image
```docker build  -t starways:latest .```

### When you want to generate a container to build the image
```caffeinate -i docker run --name starwayscontainer -it my-app /bin/bash```
