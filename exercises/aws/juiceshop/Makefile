
NAME=juice-shop
PORT=3000

all: build run

build:
	docker pull bkimminich/juice-shop

run:
	docker run --rm -d -p $(PORT):$(PORT) --name $(NAME) bkimminich/juice-shop

clean:
	sudo docker stop $(NAME);  sudo docker rm $(NAME); sudo docker rmi -f $(NAME)

purge:
	purgeAll
