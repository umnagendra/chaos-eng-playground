# Notes
## Chaos Toolkit
[Chaos Toolkit](https://chaostoolkit.org/) is a complete chaos engineering orchestrator framework. It supports the full lifecycle of chaos experiments.

![chaos engineering lifecycle](https://lh5.googleusercontent.com/XRgACxJNR1GKlF_mEGdrEgWPZeQMfosRiqw3KiF0ALUqjvE2gfgiozghYI0cDUO0b2TZRanW7EvLpvTSPCq2El_Vt_BfbEaTbKZJX9-wtmpfKoaxVyS7NkIsMwzH-oPYRVFOBa2E)

It focuses a lot on extensibility.

### Concepts
- **Probes** are checks that validate the state of the service against an expectation

- **Actions** are processes that will _attack_ the service to cause instability

- **Steady-state-hypothesis** is a set of probes that establishes the "ideal" state of the service -- once at the beginning, and once again after the experiment actions are completed

### Key Points
- FOSS project, founded by folks from [ChaosIQ](https://chaosiq.io/) who use it as the core of their commercial SaaS based reliability toolkit. Claims to be _"the most widely used Open Source Chaos Engineering tool"_

- Project [on Github](https://github.com/chaostoolkit) with 1.2k stars, occasional development and bug fix activity

- Good set of [driver extensions](https://chaostoolkit.org/extensions) - for K8S, Istio, AWS, Spring, prometheus etc.

- There is an ongoing [Open Chaos Initiative](https://github.com/open-chaos/openchaos) that aims to standardise chaos experiments through the use of the Chaos Toolkit Open API specifications.

- Ability to easily define custom extensions, probes, actions etc. Super easy!

- No built-in scheduling capability, but it is very straightforward to wrap a jenkins job around this and run chaos experiments

### Installation, Running and Management
- Very easy to install and run as a python-based tool

- Also supports Kubernetes native - installation and running as a kubernetes operator with Custom Resource Definitions (CRDs) that can be used to create Experiment resources in the cluster, making it possible to use `kubectl` to apply YAML manifest files.

![chaostoolkit deployment](https://lh4.googleusercontent.com/ISZZukgj0bc0ND4hjxXnlX_HjygjikhAXAiQf1nJm5iqpHWc6HBy3XrJt5PdwXFXiScK8uz2u_tO_7L-gfvVumWdE5R6i1Q6Jt-W6lqHgQXo25WZQI21sh7zx6rnQ29lJkiqqWWS)

- CLI-based only - **No UI** (which could be a good thing after all)

- Very straightforward to wrap a jenkins job around this to setup and run chaos experiments

- Very detailed reports can be generated via CLI tool in HTML, PDF, JSON formats

### Possible Experiments and Integrations
#### Kubernetes
- Supports credential management via K8S API key, username/password, TLS certs etc.
- Supports auth with managed kubernetes too
- Good amount of actions and probes. Ref https://docs.chaostoolkit.org/drivers/kubernetes/

#### Istio
- Supports complete set of faults as supported by Istio fault injection
- Also supports adding network delays etc.

#### Prometheus
- Supports probes to query anything from prometheus

### Pros and Cons
#### Pros
- Beautifully extensible and customizable experiments!
- Very lightweight to run, integrate and customize
- Good set of ready extensions and drivers
- Can also integrate and execute other chaos engineering tools (chaosmonkey, chaos-mesh etc.) as part of an experiment defined in chaos toolkit

#### Cons
- Not a complete end-to-end out-of-the-box chaos tool. More of a chaos framework.
- The burden of thorough reporting and observation falls on the users to adjust it to their own needs and infrastructure.

### References
- [Chaos Toolkit](https://chaostoolkit.org/)
- [ChaosIQ](https://chaosiq.io/)
- [Chaos Toolkit on Github](https://github.com/chaostoolkit)
- [Chaos Toolkit Driver Extensions](https://chaostoolkit.org/extensions)
- [Open Chaos Initiative](https://github.com/open-chaos/openchaos)
- https://blog.container-solutions.com/comparing-chaos-engineering-tools
- https://www.gremlin.com/community/tutorials/chaos-engineering-tools-comparison