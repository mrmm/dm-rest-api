
IMAGE_NAME=quay.io/mrmm/dm-rest-api
IMAGE_TAG=$(shell git rev-parse --short HEAD || echo "latest" )

CMD=docker run --rm --user=root -it --entrypoint=bash $(IMAGE_NAME):$(IMAGE_TAG)
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

push: build
	docker push $(IMAGE_NAME):$(IMAGE_TAG)

style:
	$(CMD) "/app/scripts/lint.sh" > lint_report.txt

watch:
	docker-compose up

test:
	docker-compose up -d
	docker exec -it api python manage.py test
	docker-compose down
