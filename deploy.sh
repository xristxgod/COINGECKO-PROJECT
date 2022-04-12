#!/bin/bash

set -e

cd /var/www/html/exchange

git reset --hard HEAD
git pull

docker-compose -f ./$COMPOSE_FILE build
docker-compose -f ./$COMPOSE_FILE up --no-deps -d

echo "Finished"