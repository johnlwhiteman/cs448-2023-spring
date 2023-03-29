# Exercise: Multi-Stage

```bash
cd exercises/docker/multi-stage
```

## Build the Docker image
```bash
# make build
sudo docker build -t squirrel .
```

## Run a container based on the Docker image
```bash
# make run
sudo docker run --name squirrel squirrel "say whatever you like here"
```

## Take a look at the image size for squirrel
```bash
# make showi
sudo docker images squirrel

REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
squirrel     latest    5e86c8a78fcc   2 minutes ago   254MB
```

## Inspect Docker container
```bash
# make inspect
sudo docker inspect squirrel
```

## Clean up
```bash
# make clean
sudo docker stop squirrel
sudo docker rm squirrel
sudo docker rmi squirrel
```

* Edit the Dockerfile by removing comments for STAGE2
* Rerun everything above ... check to see the file size differences with the container image
