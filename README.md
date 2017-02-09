Django + Celery
===============

Install Ubuntu packages
-----------------------

```bash
source requirements.apt
```

Install Python packages
-----------------------

```bash
virtualenv -p python3 .venv
pip install -r requirements.txt
```

Install RabbitMQ server
-----------------------

```bash
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management
sudo service rabbitmq-server restart
```

Install RabbitMQ server to docker container
-------------------------------------------
https://hub.docker.com/_/rabbitmq/
```bash
docker pull rabbitmq
docker run -d --name rabbit-mq rabbitmq:3
docker network inspect bridge
docker exec -it rabbit-mq bash
```

Manage RabbitMQ via http
------------------------
    http://[your_host]:15672/
    guest/guest by default

RabbitMQ cli management
-----------------------
    $ rabbitmqctl list_queues
    $ rabbitmqctl list_exchanges

Run celery workers
------------------
    $ celery -A tpi worker -l info -n worker.email -Q email_queue
    $ celery -A tpi worker -l info --beat -n worker.beat -Q beat_queue --concurrency=1

List active celery nodes
---------------------------------------
    $ celery -A tpi status

Inspect celery task
-------------------
     $ celery -A tpi inspect active
     $ celery -A tpi inspect scheduled
