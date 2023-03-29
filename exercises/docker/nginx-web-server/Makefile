NAME=myweb

build:
	sudo docker build -t $(NAME) .

login:
	sudo docker login
	
run:
	sudo docker run -d -p 80:80 --name $(NAME) $(NAME)

browse:
	firefox 'http://localhost:80' &

show:
	sudo docker images; echo "\n-----------\n"; sudo docker ps

clean:
	sudo docker stop $(NAME);  sudo docker rm $(NAME); sudo docker rmi -f $(NAME)

purge:
	./purgeAll
