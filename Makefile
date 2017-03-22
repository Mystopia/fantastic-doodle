virtualenv:
	virtualenv -p python3 venv3

docker_pip_compile:
	docker-compose run web pip-compile --output-file requirements.txt requirements.in

docker_pip_upgrade:
	echo "" > requirements.txt
	docker-compose run web pip-compile --output-file requirements.txt requirements.in

docker_migrate:
	docker-compose run web python manage.py migrate

docker_test:
	docker-compose run web python -Wd manage.py test --settings service.settings.test

docker_cleanup_aggressive:
	docker ps -aq
	docker ps -aq | xargs docker rm -f
	docker images -aq
	docker images -aq | xargs docker rmi -f
