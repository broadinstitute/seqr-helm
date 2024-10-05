# seqr-platform

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

A Helm chart for deploying all components of Seqr, an open source software platform for rare disease genomics

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| seqr | <seqr@broadinstitute.org> |  |

## Source Code

* <https://github.com/broadinstitute/seqr-helm>
* <https://github.com/broadinstitute/seqr>
* <https://github.com/broadinstitute/seqr-loading-pipelines>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../hail-search | hail-search | 0.2.8-dev |
| file://../lib | lib | 0.1.3 |
| file://../pipeline-runner | pipeline-runner | 0.1.2-dev |
| file://../seqr | seqr | 1.1.7-dev |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.seqrPlatformDeploy | bool | `true` |  |
| hail-search.affinity | string | `"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""` |  |
| hail-search.deploymentAnnotations | object | `{}` |  |
| hail-search.environment.HAIL_SEARCH_DATA_DIR | string | `"/seqr/seqr-hail-search-data"` |  |
| hail-search.environment.REFERENCE_DATASETS_DIR | string | `"/seqr/seqr-reference-data"` |  |
| hail-search.image.pullPolicy | string | `"Always"` |  |
| hail-search.image.repository | string | `"gcr.io/seqr-project/seqr-hail-search"` |  |
| hail-search.imagePullSecrets | list | `[]` |  |
| hail-search.initContainers | object | `{}` |  |
| hail-search.nodeSelector | object | `{}` |  |
| hail-search.podAnnotations | object | `{}` |  |
| hail-search.replicaCount | int | `1` |  |
| hail-search.resources | object | `{}` |  |
| hail-search.service.port | int | `5000` |  |
| hail-search.service.type | string | `"ClusterIP"` |  |
| hail-search.serviceAccount.annotations | object | `{}` |  |
| hail-search.serviceAccount.create | bool | `true` |  |
| hail-search.tolerations | list | `[]` |  |
| hail-search.volumeMounts | string | `"- name: seqr-datasets\n  mountPath: /seqr\n  readOnly: true"` |  |
| hail-search.volumes | string | `"- name: seqr-datasets\n  persistentVolumeClaim:\n    readOnly: true\n    claimName: {{ include \"lib.pvc-name\" . }}"` |  |
| hail-search.lib.exports.global.lib.persistentVolume.accessMode | string | `"ReadWriteOnce"` |  |
| hail-search.lib.exports.global.lib.persistentVolume.csi | object | `{}` |  |
| hail-search.lib.exports.global.lib.persistentVolume.local.nodeSelector | string | `"kind-control-plane"` |  |
| hail-search.lib.exports.global.lib.persistentVolume.local.path | string | `"/seqr"` |  |
| hail-search.lib.exports.global.lib.persistentVolume.storageCapacity | string | `"750Gi"` |  |
| hail-search.lib.exports.global.seqrPlatformDeploy | bool | `false` |  |
| lib.exports.global.lib.persistentVolume.accessMode | string | `"ReadWriteOnce"` |  |
| lib.exports.global.lib.persistentVolume.csi | object | `{}` |  |
| lib.exports.global.lib.persistentVolume.local.nodeSelector | string | `"kind-control-plane"` |  |
| lib.exports.global.lib.persistentVolume.local.path | string | `"/seqr"` |  |
| lib.exports.global.lib.persistentVolume.storageCapacity | string | `"750Gi"` |  |
| lib.exports.global.seqrPlatformDeploy | bool | `false` |  |
| pipeline-runner.affinity | string | `"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""` |  |
| pipeline-runner.deploymentAnnotations | object | `{}` |  |
| pipeline-runner.environment.SHOULD_TRIGGER_HAIL_BACKEND_RELOAD | string | `"1"` |  |
| pipeline-runner.image.pullPolicy | string | `"Always"` |  |
| pipeline-runner.image.repository | string | `"gcr.io/seqr-project/seqr-pipeline-runner"` |  |
| pipeline-runner.imagePullSecrets | list | `[]` |  |
| pipeline-runner.nodeSelector | object | `{}` |  |
| pipeline-runner.podAnnotations | object | `{}` |  |
| pipeline-runner.pods[0].command[0] | string | `"python3"` |  |
| pipeline-runner.pods[0].command[1] | string | `"-m"` |  |
| pipeline-runner.pods[0].command[2] | string | `"v03_pipeline.api"` |  |
| pipeline-runner.pods[0].healthCheckRoute | string | `"/status"` |  |
| pipeline-runner.pods[0].initContainers | string | `"{{- range $r := list \"GRCh37\" \"GRCh38\" }}\n{{- range $s := list \"rsync_reference_data\" \"download_vep_data\"}}\n- name: {{ $s | replace \"_\" \"-\" }}-{{ $r | lower}}\n  image: \"{{ $.Values.image.repository }}:{{ $.Values.image.tag | default $.Chart.AppVersion }}\"\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: [\"/v03_pipeline/bin/{{ $s }}.bash\", \"{{ $r }}\"]\n  resources:\n    requests:\n      memory: \"16Gi\"\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}\n{{- end }}\n{{- end }}"` |  |
| pipeline-runner.pods[0].name | string | `"api"` |  |
| pipeline-runner.pods[0].resources | object | `{}` |  |
| pipeline-runner.pods[0].service.port | int | `6000` |  |
| pipeline-runner.pods[0].service.type | string | `"ClusterIP"` |  |
| pipeline-runner.pods[0].sidecar.command[0] | string | `"python3"` |  |
| pipeline-runner.pods[0].sidecar.command[1] | string | `"-m"` |  |
| pipeline-runner.pods[0].sidecar.command[2] | string | `"v03_pipeline.bin.pipeline_worker"` |  |
| pipeline-runner.pods[0].sidecar.privileged | bool | `true` |  |
| pipeline-runner.pods[0].sidecar.resources.requests.memory | string | `"16Gi"` |  |
| pipeline-runner.pods[1].command[0] | string | `"luigid"` |  |
| pipeline-runner.pods[1].healthCheckRoute | string | `"/"` |  |
| pipeline-runner.pods[1].initContainers | string | `"- name: mkdir-luigi-state\n  image: busybox:1.35\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: ['/bin/mkdir', '-p', '/seqr/luigi-state']\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}"` |  |
| pipeline-runner.pods[1].name | string | `"ui"` |  |
| pipeline-runner.pods[1].resources | object | `{}` |  |
| pipeline-runner.pods[1].service.nodePort | int | `30901` |  |
| pipeline-runner.pods[1].service.port | int | `8082` |  |
| pipeline-runner.pods[1].service.type | string | `"NodePort"` |  |
| pipeline-runner.pods[1].sidecar | object | `{}` |  |
| pipeline-runner.replicaCount | int | `1` |  |
| pipeline-runner.resources | object | `{}` |  |
| pipeline-runner.serviceAccount.annotations | object | `{}` |  |
| pipeline-runner.serviceAccount.create | bool | `true` |  |
| pipeline-runner.tolerations | list | `[]` |  |
| pipeline-runner.volumeMounts | string | `"- name: seqr-datasets\n  mountPath: /seqr\n  readOnly: false"` |  |
| pipeline-runner.volumes | string | `"- name: seqr-datasets\n  persistentVolumeClaim:\n    readOnly: false\n    claimName: {{ include \"lib.pvc-name\" . }}"` |  |
| pipeline-runner.lib.exports.global.lib.persistentVolume.accessMode | string | `"ReadWriteOnce"` |  |
| pipeline-runner.lib.exports.global.lib.persistentVolume.csi | object | `{}` |  |
| pipeline-runner.lib.exports.global.lib.persistentVolume.local.nodeSelector | string | `"kind-control-plane"` |  |
| pipeline-runner.lib.exports.global.lib.persistentVolume.local.path | string | `"/seqr"` |  |
| pipeline-runner.lib.exports.global.lib.persistentVolume.storageCapacity | string | `"750Gi"` |  |
| pipeline-runner.lib.exports.global.seqrPlatformDeploy | bool | `false` |  |
| seqr.additionalSecrets | object | `{}` | Additional Secrets (defined directly as yaml) |
| seqr.affinity | string | `"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""` |  |
| seqr.cronJobs[0].command | string | `"python manage.py check_for_new_samples_from_pipeline"` |  |
| seqr.cronJobs[0].name | string | `"check-new-samples-job"` |  |
| seqr.cronJobs[0].schedule | string | `"*/10 * * * *"` |  |
| seqr.deploymentAnnotations | object | `{}` |  |
| seqr.environment.GUNICORN_WORKER_THREADS | string | `"4"` | The number of threads to allocate to the gunicorn server |
| seqr.environment.HAIL_BACKEND_SERVICE_HOSTNAME | string | `"hail-search"` |  |
| seqr.environment.HAIL_BACKEND_SERVICE_PORT | string | `"5000"` |  |
| seqr.environment.HAIL_SEARCH_DATA_DIR | string | `"/seqr/seqr-hail-search-data"` |  |
| seqr.environment.LOADING_DATASETS_DIR | string | `"/seqr/seqr-loading-temp"` |  |
| seqr.environment.PIPELINE_RUNNER_HOSTNAME | string | `"pipeline-runner"` |  |
| seqr.environment.PIPELINE_RUNNER_PORT | string | `"5000"` |  |
| seqr.environment.POSTGRES_SERVICE_HOSTNAME | string | `"seqr-postgresql"` | The hostname to use for the postgres database connectsion |
| seqr.environment.POSTGRES_SERVICE_PORT | string | `"5432"` | The TCP port number to use for the postgres database connection |
| seqr.environment.POSTGRES_USERNAME | string | `"postgres"` | The username to use for the postgres database connection |
| seqr.environment.REDIS_SERVICE_HOSTNAME | string | `"seqr-redis-master"` | The hostname of the redis cache that seqr should use |
| seqr.environment.REDIS_SERVICE_PORT | string | `"6379"` | The port of the redis cache that seqr should use |
| seqr.environment.SEQR_SERVICE_PORT | string | `"8000"` | The port that the seqr server should listen on |
| seqr.environment.STATIC_MEDIA_DIR | string | `nil` | If storing static media files in a local filesystem, the path to that filesystem |
| seqr.image.pullPolicy | string | `"Always"` |  |
| seqr.image.repository | string | `"gcr.io/seqr-project/seqr"` |  |
| seqr.image.tag | string | `""` |  |
| seqr.imagePullSecrets | list | `[]` |  |
| seqr.ingress.enabled | bool | `false` |  |
| seqr.jobAfterHook | string | `""` |  |
| seqr.jobBeforeHook | string | `""` |  |
| seqr.nodeSelector | object | `{}` |  |
| seqr.podAnnotations | object | `{}` |  |
| seqr.postgresql.architecture | string | `"standalone"` |  |
| seqr.postgresql.auth.existingSecret | string | `"postgres-secrets"` |  |
| seqr.postgresql.auth.secretKeys.adminPasswordKey | string | `"password"` |  |
| seqr.postgresql.auth.username | string | `"postgres"` |  |
| seqr.postgresql.enabled | bool | `true` |  |
| seqr.postgresql.fullnameOverride | string | `"seqr-postgresql"` |  |
| seqr.postgresql.image.tag | string | `"12.19.0-debian-12-r9"` |  |
| seqr.postgresql.postgresqlDataDir | string | `"/seqr/postgresql-data"` |  |
| seqr.postgresql.primary.initContainers[0].command[0] | string | `"/bin/sh"` |  |
| seqr.postgresql.primary.initContainers[0].command[1] | string | `"-ec"` |  |
| seqr.postgresql.primary.initContainers[0].command[2] | string | `"mkdir -p {{ .Values.postgresqlDataDir }}\nchown -R `id -u`:`id -G | cut -d \" \" -f2` {{ .Values.postgresqlDataDir }}\n"` |  |
| seqr.postgresql.primary.initContainers[0].image | string | `"{{- include \"postgresql.v1.volumePermissions.image\" . }}"` |  |
| seqr.postgresql.primary.initContainers[0].imagePullPolicy | string | `"IfNotPresent"` |  |
| seqr.postgresql.primary.initContainers[0].name | string | `"seqr-postgresql-init-chmod-data"` |  |
| seqr.postgresql.primary.initContainers[0].securityContext.runAsGroup | int | `0` |  |
| seqr.postgresql.primary.initContainers[0].securityContext.runAsNonRoot | bool | `false` |  |
| seqr.postgresql.primary.initContainers[0].securityContext.seLinuxOptions | object | `{}` |  |
| seqr.postgresql.primary.initContainers[0].securityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| seqr.postgresql.primary.initContainers[0].volumeMounts[0].mountPath | string | `"/seqr"` |  |
| seqr.postgresql.primary.initContainers[0].volumeMounts[0].name | string | `"data"` |  |
| seqr.postgresql.primary.persistence.existingClaim | string | `"{{ include \"lib.pvc-name\" . }}"` |  |
| seqr.postgresql.primary.persistence.mountPath | string | `"/seqr"` |  |
| seqr.postgresql.primary.startupProbe.enabled | bool | `true` |  |
| seqr.redis.architecture | string | `"standalone"` |  |
| seqr.redis.auth.enabled | bool | `false` |  |
| seqr.redis.enabled | bool | `true` |  |
| seqr.redis.fullnameOverride | string | `"seqr-redis"` |  |
| seqr.replicaCount | int | `1` |  |
| seqr.requiredSecrets | object | `{"postgresSecretName":"postgres-secrets","seqrSecretName":"seqr-secrets"}` | Secrets which are required for seqr's functionality |
| seqr.requiredSecrets.postgresSecretName | string | `"postgres-secrets"` | The secret containing the postgres credentials. See the README for information on the format of this secret |
| seqr.requiredSecrets.seqrSecretName | string | `"seqr-secrets"` | The secret containing the seqr required secrets. See the README for information on the format of this secret |
| seqr.resources | object | `{}` |  |
| seqr.service.nodePort | int | `30950` |  |
| seqr.service.port | int | `8000` |  |
| seqr.service.type | string | `"NodePort"` |  |
| seqr.serviceAccount.annotations | object | `{}` |  |
| seqr.serviceAccount.create | bool | `true` |  |
| seqr.tolerations | list | `[]` |  |
| seqr.volumeMounts | object | `{}` |  |
| seqr.volumes | object | `{}` |  |
| seqr.lib.exports.global.lib.persistentVolume.accessMode | string | `"ReadWriteOnce"` |  |
| seqr.lib.exports.global.lib.persistentVolume.csi | object | `{}` |  |
| seqr.lib.exports.global.lib.persistentVolume.local.nodeSelector | string | `"kind-control-plane"` |  |
| seqr.lib.exports.global.lib.persistentVolume.local.path | string | `"/seqr"` |  |
| seqr.lib.exports.global.lib.persistentVolume.storageCapacity | string | `"750Gi"` |  |
| seqr.lib.exports.global.seqrPlatformDeploy | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)