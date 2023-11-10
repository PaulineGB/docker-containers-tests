#! /bin/bash

for test in "authentication_test" "authorization_test" "content_test"
    do
        docker image build --build-arg TEST=$test -t $test .
    done

docker-compose up
