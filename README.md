# fantastic-doodle

## Getting Started

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Example usage:

```
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py shell_plus
```

### Deploy to Docker

Once everything is up, head over to [localhost:8080](http://localhost:8080/admin/).

```shell
cp sample.env .env
docker-compose up
```

Example usage:

```
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose run web python manage.py test --settings service.settings.test
docker-compose run --rm web python manage.py shell_plus
```
