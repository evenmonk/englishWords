# REST API и админка для мобильного приложения по изучению английских слов

> Необходим интерпретатор Python версии не ниже, чем 3.6;

> docker-compose 1.26.2

### Installation

Install the dependencies and start the server.

```sh
$ sudo apt install docker-compose
```

build containers
```sh
$ sudo docker-compose build --d
```
run migrations
```sh 
$ sudo docker-compose run web python3 manage.py makemigrations
$ sudo docker-compose run web python3 manage.py migrate
```
collect static files
```sh
$ sudo docker-compose run web python3 manage.py collectstatic
```
create a user for admin
```sh
$ sudo docker-compose run web python3 manage.py createsuperuser
```
clear 8000 port
```sh
$ sudo ufw allow 8000
```
run containers
```sh
$ sudo docker-compose up
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
localhost:8000
```
запуск приложения: `docker-compose up --build -d` | `./start.sh `
остановка: `docker-compose down -v` | `./stop.sh` 
посмотреть логи: `./view_web_logs.sh`

Демка: https://englishwordsapi.herokuapp.com/admin

Данные для входа в админку:

```sh
user: root
password: djangorestfullapi
```
