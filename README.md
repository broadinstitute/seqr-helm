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
