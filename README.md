# fantastic-doodle

## Getting Started

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
