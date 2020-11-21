# REST API to store user rating

## Description

It is a simple REST API to create key-val stored that serves as user rating example.


### Prerequisites

Following package and library have to install into your machine to run this app
* Helm
* Docker
* docker-compose


### Usage

This repository containts two part:
1. The service source code (stored in `service`)
2. A Helm chart with the required services to help you deploy the application on Kubernetes Cluster (in `chart`)

### Service part:
This directory contains the Makefile that contains some important step to help with the dev and build of the service that follows (gazr)[https://gazr.io/] guidelines.

To start dev and watch you can use :
```
make watch
```
Note: In this part we leverage docker-compose to setup our dev environement and run the required services to startup our application.


To build :
```
make build
```

Push the latest image to the registry:
```
make push
```

To run test:
```
make test
```

### API Usage

After running the app you can use curl to test out the app.
The API has total 4 endpoints

1. GET /ratings/ (Get all the values of the store)
  * response: {user1: rating1, user2: rating2, user3: rating3...}

2. GET /ratings/user1/ (Get one the rating of te specific user)
  * response: {value: rating1}

3. POST /ratings/
  * request: {user1: rating1, user2: rating2, user3: rating3..}
  * response: Successfully store the values

4. PUT /values
  * request: {user1: rating1, user2: rating2, user3: rating3..}
  * response: Successfully updated the values

### Helm Chart
This service depends on Redis as datastore so it has a dependecy with Bitname Helm chart.

To deploy :
```
helm install --namespace=<custom-ns> rating chart
```
