from alpine:latest AS STAGE1

ENV USER Jane
ENV PASSWORD password12345$
RUN apk update && \
    apk --no-cache --update add build-base
WORKDIR /app
COPY /app .
RUN echo $PASSWORD
RUN make 
ENTRYPOINT ["/app/squirrel"];

#from alpine:latest AS STAGE2
#RUN apk update
#WORKDIR /app
#COPY --from=STAGE1 /app/squirrel ./squirrel
#ENTRYPOINT ["/app/squirrel"];
