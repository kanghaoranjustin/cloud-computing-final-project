#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=tictactoeserver .


dockerpath="hy687098/image_classifier_v3"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag image_classifier_v3 $dockerpath

# Push Image
docker image push $dockerpath