# seqr

![Version: 1.1.7-dev](https://img.shields.io/badge/Version-1.1.7--dev-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2a0d731ad31d30234283a86dd8f2dd183b2d489c](https://img.shields.io/badge/AppVersion-2a0d731ad31d30234283a86dd8f2dd183b2d489c-informational?style=flat-square)

A Helm chart for deploying the Seqr app, an open source software platform for rare disease genomics

**Homepage:** <https://seqr.broadinstitute.org>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| seqr | <seqr@broadinstitute.org> |  |

## Source Code

* <https://github.com/broadinstitute/seqr>
* <https://github.com/broadinstitute/seqr-helm>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../lib | lib | 0.1.3 |
| https://charts.bitnami.com/bitnami | postgresql | 15.5.31 |
| https://charts.bitnami.com/bitnami | redis | 19.0.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.seqrPlatformDeploy | bool | `false` |  |
| additionalSecrets | object | `{}` | Additional Secrets (defined directly as yaml) |
| affinity | string | `"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""` |  |
| cronJobs[0].command | string | `"python manage.py check_for_new_samples_from_pipeline"` |  |
| cronJobs[0].name | string | `"check-new-samples-job"` |  |
| cronJobs[0].schedule | string | `"*/10 * * * *"` |  |
| deploymentAnnotations | object | `{}` |  |
| environment.GUNICORN_WORKER_THREADS | string | `"4"` | The number of threads to allocate to the gunicorn server |
| environment.HAIL_BACKEND_SERVICE_HOSTNAME | string | `"hail-search"` |  |
| environment.HAIL_BACKEND_SERVICE_PORT | string | `"5000"` |  |
| environment.HAIL_SEARCH_DATA_DIR | string | `"/seqr/seqr-hail-search-data"` |  |
| environment.LOADING_DATASETS_DIR | string | `"/seqr/seqr-loading-temp"` |  |
| environment.PIPELINE_RUNNER_HOSTNAME | string | `"pipeline-runner"` |  |
| environment.PIPELINE_RUNNER_PORT | string | `"5000"` |  |
| environment.POSTGRES_SERVICE_HOSTNAME | string | `"seqr-postgresql"` | The hostname to use for the postgres database connectsion |
| environment.POSTGRES_SERVICE_PORT | string | `"5432"` | The TCP port number to use for the postgres database connection |
| environment.POSTGRES_USERNAME | string | `"postgres"` | The username to use for the postgres database connection |
| environment.REDIS_SERVICE_HOSTNAME | string | `"seqr-redis-master"` | The hostname of the redis cache that seqr should use |
| environment.REDIS_SERVICE_PORT | string | `"6379"` | The port of the redis cache that seqr should use |
| environment.SEQR_SERVICE_PORT | string | `"8000"` | The port that the seqr server should listen on |
| environment.STATIC_MEDIA_DIR | string | `nil` | If storing static media files in a local filesystem, the path to that filesystem |
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"gcr.io/seqr-project/seqr"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.enabled | bool | `false` |  |
| jobAfterHook | string | `""` |  |
| jobBeforeHook | string | `""` |  |
| nodeSelector | object | `{}` |  |
| podAnnotations | object | `{}` |  |
| postgresql.architecture | string | `"standalone"` |  |
| postgresql.auth.existingSecret | string | `"postgres-secrets"` |  |
| postgresql.auth.secretKeys.adminPasswordKey | string | `"password"` |  |
| postgresql.auth.username | string | `"postgres"` |  |
| postgresql.enabled | bool | `true` |  |
| postgresql.fullnameOverride | string | `"seqr-postgresql"` |  |
| postgresql.image.tag | string | `"12.19.0-debian-12-r9"` |  |
| postgresql.postgresqlDataDir | string | `"/seqr/postgresql-data"` |  |
| postgresql.primary.initContainers[0].command[0] | string | `"/bin/sh"` |  |
| postgresql.primary.initContainers[0].command[1] | string | `"-ec"` |  |
| postgresql.primary.initContainers[0].command[2] | string | `"mkdir -p {{ .Values.postgresqlDataDir }}\nchown -R `id -u`:`id -G | cut -d \" \" -f2` {{ .Values.postgresqlDataDir }}\n"` |  |
| postgresql.primary.initContainers[0].image | string | `"{{- include \"postgresql.v1.volumePermissions.image\" . }}"` |  |
| postgresql.primary.initContainers[0].imagePullPolicy | string | `"IfNotPresent"` |  |
| postgresql.primary.initContainers[0].name | string | `"seqr-postgresql-init-chmod-data"` |  |
| postgresql.primary.initContainers[0].securityContext.runAsGroup | int | `0` |  |
| postgresql.primary.initContainers[0].securityContext.runAsNonRoot | bool | `false` |  |
| postgresql.primary.initContainers[0].securityContext.seLinuxOptions | object | `{}` |  |
| postgresql.primary.initContainers[0].securityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| postgresql.primary.initContainers[0].volumeMounts[0].mountPath | string | `"/seqr"` |  |
| postgresql.primary.initContainers[0].volumeMounts[0].name | string | `"data"` |  |
| postgresql.primary.persistence.existingClaim | string | `"{{ include \"lib.pvc-name\" . }}"` |  |
| postgresql.primary.persistence.mountPath | string | `"/seqr"` |  |
| postgresql.primary.startupProbe.enabled | bool | `true` |  |
| redis.architecture | string | `"standalone"` |  |
| redis.auth.enabled | bool | `false` |  |
| redis.enabled | bool | `true` |  |
| redis.fullnameOverride | string | `"seqr-redis"` |  |
| replicaCount | int | `1` |  |
| requiredSecrets | object | `{"postgresSecretName":"postgres-secrets","seqrSecretName":"seqr-secrets"}` | Secrets which are required for seqr's functionality |
| requiredSecrets.postgresSecretName | string | `"postgres-secrets"` | The secret containing the postgres credentials. See the README for information on the format of this secret |
| requiredSecrets.seqrSecretName | string | `"seqr-secrets"` | The secret containing the seqr required secrets. See the README for information on the format of this secret |
| resources | object | `{}` |  |
| service.nodePort | int | `30950` |  |
| service.port | int | `8000` |  |
| service.type | string | `"NodePort"` |  |
| serviceAccount.annotations | object | `{}` |  |
| serviceAccount.create | bool | `true` |  |
| tolerations | list | `[]` |  |
| volumeMounts | object | `{}` |  |
| volumes | object | `{}` |  |
| lib.exports.global.lib.persistentVolume.accessMode | string | `"ReadWriteOnce"` |  |
| lib.exports.global.lib.persistentVolume.csi | object | `{}` |  |
| lib.exports.global.lib.persistentVolume.local.nodeSelector | string | `"kind-control-plane"` |  |
| lib.exports.global.lib.persistentVolume.local.path | string | `"/seqr"` |  |
| lib.exports.global.lib.persistentVolume.storageCapacity | string | `"750Gi"` |  |
| lib.exports.global.seqrPlatformDeploy | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
