# fantastic-doodle

## Getting Started

```shell
cp sample.env .env
docker-compose up
```

Example usage:

```
docker-compose run web python manage.py migrate
docker-compose run web python manage.py test --settings service.settings.test
```
