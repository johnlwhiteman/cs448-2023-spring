NAME=webapp
IP=127.0.0.1
CERT=cert.pem

all: build http

build:
	echo "Your docker build command goes here"

run:
	echo "Your docker run command goes here"

http:
	cd webapp; python ./server.py -i $(IP) -p 80

https:
	cd webapp; python ./server.py -i $(IP) -p 443 -c $(CERT)

clean:
	sudo docker stop -f $(NAME); sudo docker -f rm $(NAME)

purge:
	./purgeAll
