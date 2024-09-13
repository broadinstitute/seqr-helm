# seqr

![Version: 0.0.21](https://img.shields.io/badge/Version-0.0.21-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 10a03ca1b98c149d798fe8c6b90f2b2473dfb4f4](https://img.shields.io/badge/AppVersion-10a03ca1b98c149d798fe8c6b90f2b2473dfb4f4-informational?style=flat-square)

A Helm chart for deploying Seqr, an open source software platform for rare disease genomics

**Homepage:** <https://seqr.broadinstitute.org>

## Source Code

* <https://github.com/broadinstitute/seqr>
* <https://github.com/broadinstitute/seqr-helm>

## Pre-requisites

### Required Services

Seqr needs the following services to function correctly, and they are expected to be available before installing seqr:

* Redis (optionally, redis can be deployed as a dependency of this chart, see [Redis](#redis) below.)
* Elasticsearch
* Kibana
* Postgres

### Secret Definition

For minimal functiontionality, seqr requires a few secrets to be defined. You should create these secrets in your kubernetes cluster, and then, using the `requiredSecrets` variable in your Helm values, inform the chart what the names of the kubernetes secrets are which contain these required settings.

1. A secret containing a `password` field for the postgres database password.
1. A secret containing a:
   1. `django_key` field for the django security key
   1. `seqr_es_password` field which contains the credential that seqr will use to connect to elasticsearch
1. A secret containing a `elasticsearch.password` field, that the kibana container will use to connect to elasticsearch

Here's how you might create some of the multi-field secrets described above:

```bash
# provide the postgres password. After creating, the requiredSecrets.postgresSecretName variable in
# values.yml should be set to 'postgres-secrets'
kubectl create secret generic postgres-secrets \
  --from-literal=password='super-secure-password'

# provide the seqr secrets. After creating, the requiredSecrets.seqrSecretName variable in
# values.yml should be set to 'seqr-secrets'
kubectl create secret generic seqr-secrets \
  --from-literal=django_key='securely-generated-key' \
  --from-literal=seqr_es_password='super-secure-password1' \
```

Alternatively, you can use your preferred method for defining secrets in kubernetes. For example, you might use [External Secrets](https://external-secrets.io/) to synchronize secrets from your cloud provider into your kubernetes cluster.

## Installation

After ensuring that the prerequisites are taken care of:

```bash
helm repo add seqr https://broadinstitute.github.io/seqr-helm
helm install institution-name charts/seqr -f my-values.yaml
```

## Redis

If you choose to deploy redis using this chart, you can do so by setting the `redis.enabled` flag to `true` in your values.yaml file. The [Bitnami Redis](https://github.com/bitnami/charts/tree/main/bitnami/redis/) chart will be used, and its configuration options can be found in its README. Any values that you pass to this chart in the `redis` namespace of your values.yaml will be passed directly to the Bitnami chart.

The hostname of your redis deployment will need to be defined in the seqr `REDIS_SERVICE_HOSTNAME` environment variable in your values.yaml file. This hostname depends on the configuration you pass to the Bitnami chart. An example hostname when provisioning a `standalone` mode cluster with this chart is "seqr-redis-master".

### Updating the Redis dependency

If you need to upgrade the redis version made available by this chart, you can do so by updating the version number of the dependency in Chart.yaml, and then running `helm dep update` to update the Chart.lock file.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | redis | 17.9.3 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| additionalSecrets | object | `{}` | If you have additional secrets to provide to the seqr Deployment, provide them in this dictionary. Examples can be found in the default values.yaml file. |
| affinity | string | The chart adds some antiAffinity rules to prevent multiple seqr pods on the same host, but these can be overridden. | Adds affinity rules to the seqr Deployment |
| environment.GUNICORN_WORKER_THREADS | string | `"4"` | The number of threads to allocate to the gunicorn server |
| environment.POSTGRES_SERVICE_HOSTNAME | string | `"postgres"` | The hostname to use for the postgres database connectsion |
| environment.POSTGRES_SERVICE_PORT | string | `"5432"` | The TCP port number to use for the postgres database connection |
| environment.POSTGRES_USERNAME | string | `"postgres"` | The username to use for the postgres database connection |
| environment.REDIS_SERVICE_HOSTNAME | string | `"seqr-redis-master"` | The hostname of the redis cache that seqr should use |
| environment.SEQR_SERVICE_PORT | string | `"8000"` | The port that the seqr server should listen on |
| environment.STATIC_MEDIA_DIR | string | `nil` | If storing static media files in a local filesystem, the path to that filesystem |
| image.pullPolicy | string | `"Always"` | The policy for pulling images |
| image.repository | string | `"gcr.io/seqr-project/seqr"` | The docker image repository to pull images from |
| imagePullSecrets | list | `[]` | If needed, you can provide secrets required to retrieve images |
| ingress.enabled | bool | `false` | Enables or Disables the seqr Ingress object |
| nodeSelector | object | `{}` | A dictionary of node selection annotations.  Used to assign the seqr application pods to specific node types.
| podAnnotations | object | `{}` | A dictionary of annotations to add to the seqr Pod |
| deploymentAnnotations | object | `{}` | A dictionary of annotations to add to the seqr Deployment |
| redis.enabled | bool | `false` | enables or disables redis deployment using this chart |
| replicaCount | int | `1` | The number of replicas of the seqr web service pod to run. Currenly only 1 is supported. |
| requiredSecrets | object | `{"postgresSecretName":"postgres-secrets","seqrSecretName":"seqr-secrets"}` | Secrets which are required for seqr's functionality |
| requiredSecrets.postgresSecretName | string | `"postgres-secrets"` | The secret containing the postgres credentials. See the README for information on the format of this secret |
| requiredSecrets.seqrSecretName | string | `"seqr-secrets"` | The secret containing the seqr required secrets. See the README for information on the format of this secret |
| resources | object | `{}` | Sets the resource requests and limits for the seqr Deployment |
| run_seqr_database_migration | bool | `false` | Enables or disables seqr database migration Jobs |
| service.port | int | `8000` | The port for the seqr Service |
| service.type | string | `"NodePort"` | The type for the seqr Service |
| volumeMounts | object | `{}` | Mountpoint information for additional data volumes on the seqr Deployment |
| volumes | object | `{}` | Additional data volumes to use in the seqr Deployment |
