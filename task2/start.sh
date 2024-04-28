#!/bin/bash

minikube start

eval $(minikube docker-env)

docker build -t time-app-image-v2 ./app
docker build -t time-app-script-image ./script

istioctl install -y --set profile=default --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
minikube kubectl -- patch service istio-ingressgateway -n istio-system -p '{"spec":{"type":"NodePort"}}'
minikube kubectl -- label namespace default istio-injection=enabled

minikube kubectl -- apply -f ./k8s/deployment
minikube kubectl -- apply -f ./k8s/service

minikube kubectl -- apply -f ./k8s/lstio/gateway.yaml
minikube kubectl -- apply -f ./k8s/lstio/virtual-service.yaml
minikube kubectl -- apply -f ./k8s/lstio/worldtimeapi-service-entry.yaml
