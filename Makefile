check:
	docker-compose -f compose-testing.yaml up -d
	sleep .5
	coverage run --source depositos setup.py test --verbose
	docker-compose -f compose-testing.yaml stop
	sleep .5
	coverage report -m