NAME=webapp
PORT=12345
IP=127.0.0.1
CERT=cert.pem

all: build http

build:
	echo "Your docker build command goes here"

run:
	echo "Your docker run command goes here"

http:
	cd webapp; python ./server.py -i $(IP) -p $(PORT)

https:
	cd webapp; python ./server.py -i $(IP) -p $(PORT) -c $(CERT)

clean:
	sudo kill -9 $(lsof -ti :${PORT}); sudo docker stop -f $(NAME); sudo docker -f rm $(NAME); ./killy;

purge:
	./purgeAll
