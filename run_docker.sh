#!/usr/bin/env bash

#build image
docker build --tag=image_classifier_v4 .

#list docker images
docker image ls

#run flask app
docker run -p 9898:9898 image_classifier_v4