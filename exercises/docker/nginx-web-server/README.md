# Exercise: Docker - Nginx Web Server

## Login to Docker
```bash
sudo docker login -u <username>
# Enter you password
```

## Check if Docker is installed and running
```bash
docker info
sudo systemctl status docker
```

## Build the image
```bash
docker build -t mywebserver .
```

## Check the image
```bash
docker images
```

## Remove the image
```bash
docker rmi mywebserver
