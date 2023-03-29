NAME=squirrel
SAY="Howdy!"

all: build run

build:
	sudo docker build -t $(NAME) .

run:
	sudo docker rm $(NAME); sudo docker run --name $(NAME) $(NAME) $(SAY)

rune:
	sudo docker rm $(NAME); sudo docker run --name $(NAME) --env-file env.txt $(NAME)

shell:
	sudo docker exec -it $(NAME) bash

showc:
	sudo docker container ls -a

showi:
	sudo docker images $(NAME)

inspect:
	sudo docker inspect $(NAME)

clean:
	sudo docker stop $(NAME); sudo docker rm $(NAME); sudo docker rmi $(NAME)

purge:
	./purgeAll
