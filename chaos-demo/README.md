# chaos-demo
Simple Spring Boot demo application to perform [chaos engineering](https://principlesofchaos.org/) experiments on.

## Overview
- Exposes basic health/uptime interfaces via [Spring Actuator]() `/health` and `/info` endpoints
- Implements non-authenticated custom REST endpoint (**GET** `/factorial/{number}`) that performs a reasonably CPU-intensive task to compute the factorial of a number

## Build
```shell
mvn clean install               # executable JAR
mvn spring-boot:build-image     # Docker image
```

## Run
#### As a native process
```shell
java -jar target/chaos-demo-0.0.1-SNAPSHOT.jar

## (or)

mvn spring-boot:run
```

#### As a docker container
```shell
docker run -p 8080:8080 --name chaos-demo chaos-demo:0.0.1-SNAPSHOT
```

#### Deploy in K8S
```shell
# 1. Create a deployment
kubectl create -f deployment.yaml

# 2. Create a service
kubectl create -f service.yaml

# 3. Expose container port (8080) via LoadBalancer, or use SSH port forwarding
kubectl port-forward svc/chaos-demo 8080:8080
```