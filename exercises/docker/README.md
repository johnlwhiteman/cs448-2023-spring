# A Simple Docker Exercise

```bash
docker build -t myapp ./app
docker run -dp 3000:3000 myapp
firefox http://localhost:3000
```

## References

* https://docs.docker.com/get-started/02_our_app/
