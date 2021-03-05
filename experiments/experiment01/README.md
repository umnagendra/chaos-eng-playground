# Experiment 01
## K8S POD crashes must not cause downtime of [chaos-demo](../../chaos-demo/README.md) service

## Overview
Simple ChaosToolkit experiment that uses the [`chaostoolkit-kubernetes`](https://github.com/chaostoolkit/chaostoolkit-kubernetes) extension to terminate PODs and validate service availability.

This experiment does the following:

- **STEP 1:** Inject a constant-rate HTTP API request traffic into [chaos-demo](../../chaos-demo/README.md) service throughout the duration of the experiment

- **STEP 2:** Establish the following [steady-state-hypothesis](https://docs.chaostoolkit.org/reference/concepts/#steady-state-hypothesis):
  - service is UP and RUNNING, and reports a 'healthy' status
  - all traffic is being served successfully -- there are no errors

- **STEP 3:** Then, using the [`chaostoolkit-kubernetes`](https://github.com/chaostoolkit/chaostoolkit-kubernetes) extension, a single random POD is terminated abruptly. (This should make K8S spin up another POD to keep the replica set intact as per spec.)

- **STEP 4:** The experiment waits for some time, lets the constant-rate HTTP API request traffic continue to hit the service.

- **STEP 5:** The traffic metrics are gathered and transformed to be analyzed.

- **STEP 6:** Finally, the steady-state-hypothesis (described above) is validated again. **It must pass**. Else, the experiment is considered a failure because it has affected service availability.

## Pre-Requisites
[Vegeta](https://github.com/tsenart/vegeta) is a CLI based HTTP performance testing tool, (much like [_apacheBench `(ab)`_](https://httpd.apache.org/docs/2.4/programs/ab.html) but better). This is used to inject constant rate load for a specific duration through the experiment.

## Run
1. Navigate to `experiments/experiment01` directory
    ```shell
    pushd ${repo}/experiments/experiment01
    ```

2. Activate the python virtual environment created for chaos toolkit
    ```shell
    source ~/.venvs/chaostoolkit/bin/activate
    ```

3. For custom python extension code to be picked-up, we need to add this directory (where we have [custom-probes.py](custom_probes.py) to `$PYTHONPATH`
    ```shell
    export PYTHONPATH=`pwd`
    ```

4. Run the chaos experiment!
    ```shell
    chaos run experiment01.json
    ```
   This will run the chaos experiment as defined in [experiment01.json](experiment01.json). Chaos toolkit logs will be written to `chaostoolkit.log`, and also `journal.json` which contains details about the experiment execution.

## Analyze
Irrespective of whether the experiment succeeds or not, we can generate a detailed report in HTML, or PDF formats.

```shell
chaos report --export-format=html journal.json report.html
```