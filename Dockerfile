FROM python:3.9.1

EXPOSE 8888
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt-get update
RUN pip install jupyter jupyterlab
RUN bash start.sh

CMD [ "jupyter-lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root" ]
