# Setup

## Pre-Requisites
- Docker Engine
- Access to a public repo where you can host `chaos-demo` app (say, hub.docker.com)
- Kubernetes (`minikube` or `kind` with `kubectl` installed)
- Python 3.7+ with `pip`
- JDK 8, Maven 3.3+ (to build and locally deploy **chaos-demo**)

## Running [chaos-demo](chaos-demo/README.md) as a K8S service
- Refer [chaos-demo/README.md](chaos-demo/README.md) for details on how to build, run and deploy the app as a K8S service.

## Installing Chaos Toolkit and extensions

1. Ensure that you have the latest Python 3.7+ installed. On most computers, `python` refers to Python 2.x, so look for `python3` in your `$PATH`.
    ```shell
    python3 -V
    ```

2. Create a virtual environment where you can install and run chaos toolkit experiments.
    ```shell
    mkdir ~/.venvs && python3 -m venv ~/.venvs/chaostoolkit
    ```

3. Activate the virtual environment for chaos toolkit
    ```shell
    source ~/.venvs/chaostoolkit/bin/activate
    ```

4. Make sure you have the latest version of the `pip` package manager
    ```shell
    pip install -U pip
    ```

5. Install `chaostoolkit` in the virtual environment
    ```shell
    pip install -U chaostoolkit
    ```

6. Install chaostoolkit extensions as required
    ```shell
    pip install -U chaostoolkit-kubernetes
    ```

## You're all set!
Check **README.md** in each experiment for details on how to run experiments, analyze results and generate reports etc.


- - -


## APPENDIX 1: Useful `kubectl` commands
#### List all pods, deployments, services, replicasets etc. in the cluster
```
kubectl get all
```

#### List all pods
```
kubectl get pods --output=wide
```

#### Delete all pods, deployments, services, replicasets etc. across all namespaces in the cluster
```
kubectl delete all --all --all-namespaces
```

#### Create a deployment based on a spec
```
kubectl create -f deployment.yaml
```

#### Create a service based on a spec
```
kubectl create -f service.yaml
```

#### Scale up / down PODs in a deployment
```
kubectl scale --replicas=4 deployment.apps/<deployment name>
```

#### Expose a port from a service / replicaset via port-forwarding _(poor man's alternative to actually setting-up a load balancer)
```
kubectl port-forward replicaset.apps/<replicaset name> <SRC_PORT>:<DST_PORT>
```