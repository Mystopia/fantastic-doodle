virtualenv:
	virtualenv -p python3 venv3

docker_pip_compile:
	docker-compose run web pip-compile --output-file requirements.txt requirements.in

docker_migrate:
	docker-compose run web python manage.py migrate

docker_test:
	docker-compose run web python manage.py test --settings service.settings.test
