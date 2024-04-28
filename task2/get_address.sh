#!/bin/bash

minikube_ip=$(minikube ip)

node_port=$(minikube kubectl -- get service istio-ingressgateway -n istio-system -o jsonpath='{.spec.ports[?(@.port==80)].nodePort}')

echo "${minikube_ip}:${node_port}"