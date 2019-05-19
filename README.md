# django-celery-dockerize

This repository provides skeleton project of Django / Celery / Maria DB / Redis Cache configurations with Docker

Please refer to the following posts:  
https://blog.khtinsoft.xyz/posts/django-celery-mariadb-redis-docker/  
https://blog.khtinsoft.xyz/posts/django-celery-auto-restart/


## Commands

You can manage this project by following commands

```bash
$ docker-compose up       # Start all containers
$ docker-compose up -d    # Start all containers (daemon mode)
$ docker-compose down     # Stop all containers
$ docker-compose down -v  # Stop all containers and remove docker volumes