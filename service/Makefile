
IMAGE_NAME=quay.io/mrmm/dm-rest-api
IMAGE_TAG=$(git rev-parse --short HEAD || latest)

CMD=docker run --rm -it --entrypoint=bash $(IMAGE_NAME):$(IMAGE_TAG)
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .


style:
	$(CMD) "/app/scripts/lint.sh"

watch:
	docker-compose up
