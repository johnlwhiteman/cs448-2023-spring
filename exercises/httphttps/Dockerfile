FROM alpine:latest AS BUILD
ENV NAME=student
ENV PDIR=/home/${NAME}
ENV PYTHONUNBUFFERED=1
RUN adduser -D ${NAME}
WORKDIR ${PDIR}
COPY --chown=${NAME} /assets/* ./
RUN apk update --no-cache \
    && apk add bash openssl python3 vim \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && python3 -m ensurepip \
    && ln -sf /usr/bin/pip3 /usr/bin/pip \
    && pip3 install --no-cache --upgrade pip setuptools \
    && pip install -r requirements.txt \
    && rm -rf requirements.txt /var/cache/apk/* /tmp/* \
    && openssl req -new -newkey rsa:4096 -sha384 -days 365 -nodes -x509 \
       -subj "/C=US/ST=Oregon/L=Portland/O=Cybersecurity/CN=up.edu" \
       -keyout key.pem -out cert.pem
USER ${NAME}
COPY --chown=${NAME} app/ ${PDIR}/
USER root
CMD ["python", "http-server.py"]
