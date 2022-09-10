release: chmod u+x release.sh && ./release.sh
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app