# Chaos Engineering Playground
Exploring [chaos engineering](https://principlesofchaos.org/) principles using [Chaos Toolkit](https://chaostoolkit.org/)

## Overview
This repository contains 2 things:
- [**chaos-demo**](chaos-demo/README.md) - A simple containerized demo application which can be deployed as a service on a K8S cluster
- [**experiments**](experiments) - A set of chaos experiments that assault the _chaos-demo_ service and validate availability during / after these experiments

## Setup
Follow steps in [SETUP.md](SETUP.md) to setup the tools and environment required

## Experiments

|Experiment|Description|
|----------|-----------|
|[experiment-01](experiments/experiment01/README.md)|_**K8S POD crashes must not cause downtime of chaos-demo service**_<br>Simple ChaosToolkit experiment that uses the [`chaostoolkit-kubernetes`](https://github.com/chaostoolkit/chaostoolkit-kubernetes) extension to terminate PODs and validate service availability.|

## References
- [Chaos Engineering Principles](https://principlesofchaos.org/)
- [Chaos Toolkit](https://chaostoolkit.org/)
- [chaostoolkit-kubernetes](https://github.com/chaostoolkit/chaostoolkit-kubernetes)
- [My notes about Chaos Toolkit](./NOTES.md)