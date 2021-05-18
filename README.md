# Service Dev setup

After cloning the repository, follow the next steps to have the project's BE up and running:

## Guide

- [Service Dev setup](#service-dev-setup)
  - [Guide](#guide)
  - [Description](#description)
  - [System dependencies](#system-dependencies)
  - [Execute code](#execute-code)
        - [After executing this command actions take place](#after-executing-this-command-actions-take-place)
  - [Execute Tests](#execute-tests)
  - [Sentry](#sentry)
  - [Curl Request](#curl-request)

## Description

    Its Flask project implement Algorithms like Ackermann Fibonacci Factorial

    Most of the Algorithms implemented Dynamic programming Iterative and recursive 

    Include unit testing 

    Include Sentry for montering   

## System dependencies

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Execute code
This might take long time to install sentry onpremise
</br>
<mark>Skip creating user during running sentry container for the first time</mark>

    sudo bash install.sh

##### After executing this command actions take place

- sentry containers will be up
- backend container will be up
- move sentry-postgres dump to the docker volumes
- export machine wlp1s0 to environment variable  MACHINE_IP

## Execute Tests

    docker exec -it backend  python manage.py test

## Sentry 

- URL: [localhost:9000](http://localhost:9000/auth/login/sentry/) 
- User credentials
    ```
    Account: root@localhost
    password: 123456
    ```

## Curl Request

- Factorial:
    ```
     curl -X GET -H "Content-type: application/json" -H "Accept:application/json" -d '{"number":1000}' "http://localhost:5000/factorial"
    ```
- Fibonacci:
    ```
     curl -X GET -H "Content-type: application/json" -H "Accept:application/json" -d '{"number":1000}' "http://localhost:5000/fibonacci"
    ```
- Ackermann:
    ```
     curl -X GET -H "Content-type: application/json" -H "Accept:application/json" -d '{"row":8,"column":8}' "http://localhost:5000/ackermann"
    ```