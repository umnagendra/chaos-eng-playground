# Experiment 01
## K8S POD crashes must not cause downtime of [chaos-demo](../../chaos-demo/README.md) service

## Overview
Simple ChaosToolkit experiment that uses the [`chaostoolkit-kubernetes`](https://github.com/chaostoolkit/chaostoolkit-kubernetes) extension to terminate PODs and validate service availability.

## Pre-Requisites
[Vegeta](https://github.com/tsenart/vegeta) is a CLI based HTTP performance testing tool, (much like [_apacheBench `(ab)`_](https://httpd.apache.org/docs/2.4/programs/ab.html) but better). This is used to inject constant rate load for a specific duration through the experiment.

## Run
1. Navigate to `experiments/experiment-01` directory
    ```shell
    pushd ${repo}/experiments/experiment-01
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
    chaos run experiment-01.json
    ```
   This will run the chaos experiment as defined in [experiment-01.json](experiment01.json). Chaos toolkit logs will be written to `chaostoolkit.log`, and also `journal.json` which contains details about the experiment execution.

## Analyze
Irrespective of whether the experiment succeeds or not, we can generate a detailed report in HTML, or PDF formats.

```shell
chaos report --export-format=pdf journal.json report.pdf
```