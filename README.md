# seqr-helm
Helm charts for the *seqr* platform

## Overview
This repo consists of helm charts defining the seqr platform.  [Helm](https://helm.sh) is a package manager for [Kubernetes](https://kubernetes.io), an open source system for automating deployment and management of containerized applications.  

1. The [*seqr*](charts/seqr) application chart consists of deployments for the [*seqr* application](https://github.com/broadinstitute/seqr), the [`redis` cache](https://github.com/redis/redis) and [`postgresql` relational database](https://github.com/postgres/postgres).  The `redis` and `postgresql` services may be disabled if `seqr` is running in a cloud environment with access to managed services.  Note that this deployment does not include support for `elasticsearch`.
1. The [hail-search](charts/hail-search) application chart contains a deployment of the service powering variant search within *seqr*.
1. The [pipeline-runner](charts/pipeline-runner) application chart contains the multiple services that make up the [*seqr* loading pipeline](https://github.com/broadinstitute/seqr-loading-pipelines).  This chart also runs the [luigi scheduler user interface](https://luigi.readthedocs.io/en/stable/central_scheduler.html) to view running pipeline tasks.
1. A [lib](charts/lib) library chart for resources shared
between the other charts.
1. The [*seqr-platform*](charts/seqr-platform) umbrella chart that bundles the composing charts into a single installable.

## Instructions for Initial Deployment

The Kubernetes ecosystem contains many standardized and custom solutions across a [wide range of cloud and on-premises environments](https://kubernetes.io/docs/setup/production-environment/turnkey-solutions/).  To avoid the complexity of a full-fledged [production environment](https://kubernetes.io/docs/setup/production-environment/) and to achieve parity with the [existing docker-compose](https://github.com/broadinstitute/seqr/blob/master/docker-compose.yml), we recommend setting up a simple local Kubernetes cluster on an on-premises server or a cloud Virtual Machine with at least `32GB` of memory and `750GB` of disk space.

Install the four required kubernetes infrastructure components:
1. The [`docker`](https://docs.docker.com/engine/install/) container engine.
    - If running `Docker Desktop` on a laptop, make sure to set your CPU and Memory limits under Settings > Resources > Advanced.
1. The [`kubectl`](https://kubernetes.io/docs/tasks/tools/) command line client.
1. The [`kind`](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) local cluster manager.
1. The [`helm`](https://helm.sh/docs/intro/install/) package manager.

Then:
1. Create a local `/var/seqr` directory to be mounted into the Kubernetes cluster.  This will host all seqr application data:
```
mkdir -p /var/seqr
```
2. Start a `kind` cluster:
```
curl https://raw.githubusercontent.com/broadinstitute/seqr-helm/refs/heads/main/kind.yaml > kind.yaml
kind create cluster --config kind.yaml
```
3. Create a `~/.kube/config` file:
```
mkdir -p ~/.kube; kubectl config view --raw > ~/.kube/config; chmod go-r ~/.kube/config
```
4. Create the [Required Secrets](#required-secrets) in your cluster using `kubectl`.
5. [Migrate](#migrating-application-data) any existing application data.
6. Install the `seqr-platform` chart with any [override values](#valuesenvironment-overrides):
```
helm repo add seqr-helm https://broadinstitute.github.io/seqr-helm
helm install YOUR_INSTITUTION_NAME-seqr seqr-helm/seqr-platform
```

After install you should expect to something like:

```
helm install broad-seqr seqr-helm/seqr-platform 
NAME: YOUR_INSTITUTION_NAME-seqr
LAST DEPLOYED: Wed Oct 16 14:50:22 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

The first deployment will include a download of all of the genomic reference data (400GB+).  It is likely to be slow, but can be monitored by checking the contents of `/var/seqr/seqr-reference-data`.  Once the download completes, you may check the status of the services with:

```
kubectl get pods
NAME                                        READY   STATUS      RESTARTS      AGE
hail-search-7678986f7-n8655                 1/1     Running     0             22m
pipeline-runner-api-5557bbc7-vrtcj          2/2     Running     0             22m
pipeline-runner-ui-749c94468f-62rtv         1/1     Running     0             22m
seqr-68d7b855fb-bjppn                       1/1     Running     0             22m
seqr-check-new-samples-job-28818190-vlhxj   0/1     Completed   0             22m
seqr-postgresql-0                           1/1     Running     0             22m
seqr-redis-master-0                         1/1     Running     0             22m
```

Once services are healthy, you may create a seqr Admin user using the pod name from the above output:

```
kubectl exec seqr-68d7b855fb-bjppn -c seqr -it -- bash
python3 /seqr/manage.py createsuperuser
```

## Required Secrets

The *seqr* application expects a few secrets to be defined for the services to start.  The default expected secrets are declared in the [default `values.yaml`](charts/seqr/values.yaml#L68) file of the *seqr* application chart.  You should create these secrets in your kubernetes cluster prior to attempting to install the chart.

1. A secret containing a `password` field for the postgres database password.  By default this secret is named `postgres-secrets`.
1. A secret containing a `django_key` field for the django security key.  By default this secret is named `seqr-secrets`.

Here's how you might create the secrets:

```bash
kubectl create secret generic postgres-secrets \
  --from-literal=password='super-secure-password'

kubectl create secret generic seqr-secrets \
  --from-literal=django_key='securely-generated-key'
```

Alternatively, you can use your preferred method for defining secrets in kubernetes. For example, you might use [External Secrets](https://external-secrets.io/) to synchronize secrets from your cloud provider into your kubernetes cluster.

## Migrating Application Data

- If you wish to preserve your existing application state in `postgresql`, you may move your existing [`./data/postgres`](https://github.com/broadinstitute/seqr/blob/master/docker-compose.yml#L11) to `/var/seqr/postgresql-data`.  You should see:

```
cat /var/seqr/postgresql-data/PG_VERSION
12
```

- To migrate static files, you may move your existing [`./data/seqr_static_files`](https://github.com/broadinstitute/seqr/blob/master/docker-compose.yml#L63)  to [`/var/seqr/seqr-static-media`](charts/seqr/values.yaml#L58).

- To migrate `readviz`, you may move your existing [`./data/readviz`](https://github.com/broadinstitute/seqr/blob/master/docker-compose.yml#L62) directory to [`/var/seqr/seqr-static-media`](charts/seqr/values.yaml#L58) and additionally run the `update_igv_location.py` `manage.py` command:

```
python /seqr/manage.py update_igv_location old_prefix new_prefix
```

Note that you do not need to migrate any elasticsearch data.

## Values/Environment Overrides

All default values in the `seqr-platform` chart may be overriden with [helm's Values file functionality](https://helm.sh/docs/chart_template_guide/values_files/).  For example, to disable the `postgresql` deployment, you might create a file `my-values.yaml` with the contents:
```
seqr:
  postgresql:
    enabled: false
```

This is also the recommended pattern for overriding any `seqr` environment variables:

```
seqr:
  environment:
    GUNICORN_WORKER_THREADS: "8"
```

A more comprehensive example of what this may look like, and how the different values are formated in practice, is found in the [*seqr* unit tests](unit_test/seqr/values.yaml).

## Updating your code
To fetch the latest versions of the `helm` infrastructure and `seqr` application code, you may run:
```
helm upgrade broad-seqr seqr-helm/seqr-platform
```

## Debugging FAQ
- How do I uninstall `seqr` and remove all application data?
```
helm uninstall YOUR_INSTITUTION_NAME-seqr
kind delete cluster
rm -rf /var/seqr
```
- How do I view `seqr`'s disk utilization?
You may access the size of each of the on-disk components with:
```
du -sh /var/seqr/*
```
- How do I tail logs?
To tail the logs of the pipeline worker after you have started a pipeline run, for example:
```
kubectl get pods -o name | grep pipeline-runner-api
pipeline-runner-api-5557bbc7-vrtcj
kubectl logs pipeline-runner-api-5557bbc7-vrtcj -c pipeline-runner-api-sidecar
2024-10-16 18:24:27 - pipeline_worker - INFO - Waiting for work
2024-10-16 18:24:28 - pipeline_worker - INFO - Waiting for work
2024-10-16 18:24:29 - pipeline_worker - INFO - Waiting for work
....
base_hail_table - INFO - UpdatedCachedReferenceDatasetQuery(reference_genome=GRCh37, dataset_type=SNV_INDEL, crdq=CLINVAR_PATH_VARIANTS) start
[Stage 42:========>
```
