# seqr-helm
Helm charts for the *seqr* platform

## Overview
This repo consists of helm charts defining the seqr platform.  [Helm](https://helm.sh) is a package manager for [Kubernetes](https://kubernetes.io), an open source system for automating deployment and management of containerized applications.  

1. The [*seqr*](charts/seqr) application chart consists of deployments for the [*seqr* application](https://github.com/broadinstitute/seqr) and the optionally enabled [redis cache](https://github.com/redis/redis) and [postgresql relational database](https://github.com/postgres/postgres).  
1. The [hail-search](charts/hail-search) application chart contains a deployment of the service powering variant search within *seqr*.
1. The [pipeline-runner](charts/pipeline-runner) application chart contains the multiple services that make up the [*seqr* loading pipeline](https://github.com/broadinstitute/seqr-loading-pipelines).  This chart also exposes the [luigi scheduler user interface](https://luigi.readthedocs.io/en/stable/central_scheduler.html) to view running pipeline tasks.
1. A [lib](charts/lib) library chart for resources shared
amongst the other charts.
1. The [seqr-platform](charts/seqr-platform) umbrella chart that bundles the composing charts into a single installable.

## Instructions for initial deployment.

The Kubernetes ecosystem contains many standardized and custom solutions across a [wide range of cloud and bare metal environments](https://kubernetes.io/docs/setup/production-environment/turnkey-solutions/).  To avoid the complexity of a full-fledged [production environment](https://kubernetes.io/docs/setup/production-environment/) and to achieve parity with the [existing docker-compose](https://github.com/broadinstitute/seqr/blob/master/docker-compose.yml), we recommend setting up a simple local Kubernetes cluster on an on-premises server or a cloud Virtual Machine with at least 32GB of memory and 750GB of disk space.  

Follow the instructions [here](https://kubernetes.io/docs/tasks/tools/) to install the four required infrastructure components:
1. [Docker](https://www.docker.com).
1. [the `kubectl` client](https://kubernetes.io/docs/tasks/tools/#kubectl)
1. [the `kind` local cluster manager](https://kubernetes.io/docs/tasks/tools/#kind).
1. [helm](https://helm.sh/docs/intro/install/)


Then:
1. Create a local `/var/seqr` directory to be mounted into the Kubernetes cluster:
```
mkdir -p /var/seqr
```
1. Start a `kind` cluster:
```
kind create cluster --config kind.yaml
```
1. [Create the Required Secrets](#Required Secrets) in your cluster using `kubectl`.
1.  Install the `seqr-platform` chart with any override values:
```
helm repo add seqr https://broadinstitute.github.io/seqr-helm
helm install institution-name charts/seqr-platform -f my-values.yaml
```

## Required Secrets

The *seqr* application expects a few secrets to be defined for the services to start.  The default expected secrets are declared in the [default `values.yaml`](charts/seqr/values.yaml) file of the *seqr* application chart.  You should create these secrets in your kubernetes cluster prior to attempting to install the chart.

1. A secret containing a `password` field for the postgres database password.  By default this secret is named `postgres-secrets`.
1. A secret containing a `django_key` field for the django security key.  By default this secret is named `seqr-secrets`.

Here's how you might create the secrets:

```bash
kubectl create secret generic postgres-secrets \
  --from-literal=password='super-secure-password'

kubectl create secret generic seqr-secrets \
  --from-literal=django_key='securely-generated-key' \
```

Alternatively, you can use your preferred method for defining secrets in kubernetes. For example, you might use [External Secrets](https://external-secrets.io/) to synchronize secrets from your cloud provider into your kubernetes cluster.
