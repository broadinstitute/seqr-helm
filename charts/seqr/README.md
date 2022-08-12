# seqr

![Version: 0.0.2](https://img.shields.io/badge/Version-0.0.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v1.0-dea935a](https://img.shields.io/badge/AppVersion-v1.0--dea935a-informational?style=flat-square)

A Helm chart for deploying Seqr, an open source software platform for rare disease genomics

**Homepage:** <https://seqr.broadinstitute.org>

## Source Code

* <https://github.com/broadinstitute/seqr>
* <https://github.com/broadinstitute/seqr-helm>

## Pre-requisites

### Required Services

Seqr needs the following services to function correctly, and they are expected to be available before installing seqr:

* Redis
* Elasticsearch
* Kibana
* Postgres

### Secret Definition

For minimal functiontionality, seqr requires a few secrets to be defined. You should create these secrets in your kubernetes cluster, and then, using the `required_secrets` variable in your Helm values, inform the chart what the names of the kubernetes secrets are which contain these required settings.

1. A secret containing a `password` field for the postgres database password.
1. A secret containing a:
   1. `django_key` field for the django security key
   1. `seqr_es_password` field which contains the credential that seqr will use to connect to elasticsearch
1. A secret containing a `elasticsearch.password` field, that the kibana container will use to connect to elasticsearch

Here's how you might create some of the multi-field secrets described above:

```bash
# provide the postgres password. After creating, the required_secrets.postgresSecretName variable in
# values.yml should be set to 'postgres-secrets'
kubectl create secret generic postgres-secrets \
  --from-literal=password='super-secure-password'

# provide the seqr secrets. After creating, the required_secrets.seqrSecretName variable in
# values.yml should be set to 'seqr-secrets'
kubectl create secret generic seqr-secrets \
  --from-literal=django_key='securely-generated-key' \
  --from-literal=seqr_es_password='super-secure-password1' \
```

Alternatively, you can use your preferred method for defining secrets in kubernetes. For example, you might use [External Secrets](https://external-secrets.io/) to synchronize secrets from your cloud provider into your kubernetes cluster.

## Installation

After ensuring that the prerequisites are taken care of:

helm repo add https://seqr.github.io/charts
helm install seqr-institution-name tgg-helm/seqr -f my-values.yaml

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | redis | 16.8.5 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| additional_secrets | object | `{}` | If you have additional secrets to provide to the seqr Deployment, provide them in this dictionary. Examples can be found in the default values.yaml file. |
| affinity | string | `"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchLabels:\n            {{- include \"seqr.selectorLabels\" . | nindent 12 }}\n        topologyKey: \"kubernetes.io/hostname\""` | Affinity configuration for the seqr Deployment |
| enable_elasticsearch_auth | bool | `false` | If seqr needs a password to connect to elasticsearch and kibana |
| environment.ELASTICSEARCH_PROTOCOL | string | `"http"` | The URL protocol that seqr should use to connect to elasticsearch |
| environment.ELASTICSEARCH_SERVICE_HOSTNAME | string | `"elasticsearch-es-http"` | The hostname that seqr should use to connect to elasticsearch |
| environment.ELASTICSEARCH_SERVICE_PORT | string | `"9200"` | The port number that seqr should use to connect to elasticsearch |
| environment.GUNICORN_WORKER_THREADS | string | `"4"` | The number of threads to allocate to the gunicorn server |
| environment.POSTGRES_SERVICE_HOSTNAME | string | `"postgres"` | The hostname to use for the postgres database connectsion |
| environment.POSTGRES_SERVICE_PORT | string | `"5432"` | The TCP port number to use for the postgres database connection |
| environment.POSTGRES_USERNAME | string | `"postgres"` | The username to use for the postgres database connection |
| environment.REDIS_SERVICE_HOSTNAME | string | `"seqr-redis-master"` | The hostname of the redis cache that seqr should use |
| environment.SEQR_SERVICE_PORT | string | `"8000"` | The port that the seqr server should listen on |
| environment.STATIC_MEDIA_DIR | string | `nil` | If storing static media files in a local filesystem, the path to that filesystem |
| fullnameOverride | string | `""` | Overrides the fully qualified name of the app, for use in templates |
| image.pullPolicy | string | `"Always"` | The policy for pulling images |
| image.repository | string | `"gcr.io/seqr-project/seqr"` | The docker image repository to pull images from |
| image.tag | string | `"gcloud-dev"` | The docker image tag to pull from the repository |
| imagePullSecrets | list | `[]` | If needed, you can provide secrets required to retrieve images |
| ingress.enabled | bool | `false` | Enables or Disables the seqr Ingress object |
| nameOverride | string | `""` | Overrides the name of the helm chart, for use in templates |
| podAnnotations | object | `{}` | A dictionary of annotations to add to the seqr Deployment |
| redis.enabled | bool | `false` | enables or disables redis deployment using this chart |
| replicaCount | int | `1` | The number of replicas of the seqr web service pod to run. Currenly only 1 is supported. |
| required_secrets | object | `{"postgresSecretName":"postgres-secrets"}` | The name of the secret containing seqr's kibana password kibanaSecretName: kibana-secrets Seqr requires a few secrets to be defined. Here you can specify the names of the kubernetes secrets if you have named them differently than the defaults. See the README for information on the format of these secrets. |
| required_secrets.postgresSecretName | string | `"postgres-secrets"` | The secret containing the postgres credentials. See the README for information on the format of this secret |
| resources | object | `{}` | Sets the resource requests and limits for the seqr Deployment |
| run_seqr_database_migration | bool | `false` | Enables or disables seqr database migration Jobs |
| service.port | int | `8000` | The port for the seqr Service |
| service.type | string | `"NodePort"` | The type for the seqr Service |
| tolerations | list | `[]` | Pod tolerations for the seqr Deployment |
| volumeMounts | object | `{}` | Mountpoint information for additional data volumes on the seqr Deployment |
| volumes | object | `{}` | Additional data volumes to use in the seqr Deployment |
