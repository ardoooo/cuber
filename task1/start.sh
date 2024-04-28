#!/bin/bash
minikube start

minikube addons enable ingress
eval $(minikube docker-env)

docker build -t time-app-image ./app
docker build -t time-app-script-image ./script

minikube kubectl -- apply -f ./k8s/deployment
minikube kubectl -- apply -f ./k8s/service

sleep 10

minikube kubectl -- apply -f ./k8s/ingress
