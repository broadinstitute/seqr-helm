# seqr

![Version: 1.4.0](https://img.shields.io/badge/Version-1.4.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 77e84647fa237fbb1fa02086598a1e11ae061ed3](https://img.shields.io/badge/AppVersion-77e84647fa237fbb1fa02086598a1e11ae061ed3-informational?style=flat-square)

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
| file://../lib | lib | 0.1.4 |
| https://charts.bitnami.com/bitnami | postgresql | 15.5.31 |
| https://charts.bitnami.com/bitnami | redis | 19.0.2 |

## Values

<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>global.seqrPlatformDeploy</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>additionalSecrets</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>affinity</td>
			<td>string</td>
			<td><pre lang="json">
"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>cronJobs[0].command</td>
			<td>string</td>
			<td><pre lang="json">
"python manage.py check_for_new_samples_from_pipeline"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>cronJobs[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"check-new-samples-job"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>cronJobs[0].schedule</td>
			<td>string</td>
			<td><pre lang="json">
"*/10 * * * *"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>deploymentAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.GUNICORN_WORKER_THREADS</td>
			<td>string</td>
			<td><pre lang="json">
"4"
</pre>
</td>
			<td>The number of threads to allocate to the gunicorn server</td>
		</tr>
		<tr>
			<td>environment.HAIL_BACKEND_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"hail-search"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.HAIL_BACKEND_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"5000"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.HAIL_SEARCH_DATA_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/seqr-hail-search-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.LOADING_DATASETS_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/seqr-loading-temp"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.LUIGI_UI_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"pipeline-runner-ui"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.LUIGI_UI_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"8082"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.PIPELINE_RUNNER_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"pipeline-runner-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.PIPELINE_RUNNER_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"6000"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.POSTGRES_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-postgresql"
</pre>
</td>
			<td>The hostname to use for the postgres database connectsion</td>
		</tr>
		<tr>
			<td>environment.POSTGRES_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"5432"
</pre>
</td>
			<td>The TCP port number to use for the postgres database connection</td>
		</tr>
		<tr>
			<td>environment.POSTGRES_USERNAME</td>
			<td>string</td>
			<td><pre lang="json">
"postgres"
</pre>
</td>
			<td>The username to use for the postgres database connection</td>
		</tr>
		<tr>
			<td>environment.REDIS_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-redis-master"
</pre>
</td>
			<td>The hostname of the redis cache that seqr should use</td>
		</tr>
		<tr>
			<td>environment.REDIS_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"6379"
</pre>
</td>
			<td>The port of the redis cache that seqr should use</td>
		</tr>
		<tr>
			<td>environment.SEQR_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"8000"
</pre>
</td>
			<td>The port that the seqr server should listen on</td>
		</tr>
		<tr>
			<td>environment.STATIC_MEDIA_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/seqr-static-media"
</pre>
</td>
			<td>If storing static media files in a local filesystem, the path to that filesystem</td>
		</tr>
		<tr>
			<td>image.pullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"Always"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"gcr.io/seqr-project/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>imagePullSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>initContainers</td>
			<td>string</td>
			<td><pre lang="json">
"- name: mkdir-loading-datasets\n  image: busybox:1.35\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: ['/bin/mkdir', '-p', {{ $.Values.environment.LOADING_DATASETS_DIR }}]\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jobAfterHook</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jobBeforeHook</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nodeSelector</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>podAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.architecture</td>
			<td>string</td>
			<td><pre lang="json">
"standalone"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.existingSecret</td>
			<td>string</td>
			<td><pre lang="json">
"postgres-secrets"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.secretKeys.adminPasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"postgres"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Set to "false" to disable the postgresql deployent (if you're using a managed cloud database).</td>
		</tr>
		<tr>
			<td>postgresql.fullnameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-postgresql"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.image.tag</td>
			<td>string</td>
			<td><pre lang="json">
"12.19.0-debian-12-r9"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.postgresqlDataDir</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/postgresql-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"/bin/sh"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].command[1]</td>
			<td>string</td>
			<td><pre lang="json">
"-ec"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].command[2]</td>
			<td>string</td>
			<td><pre lang="json">
"mkdir -p {{ .Values.postgresqlDataDir }}\nchown -R `id -u`:`id -G | cut -d \" \" -f2` {{ .Values.postgresqlDataDir }}\n"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].image</td>
			<td>string</td>
			<td><pre lang="json">
"{{- include \"postgresql.v1.volumePermissions.image\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].imagePullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"IfNotPresent"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-postgresql-init-chmod-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].securityContext.runAsGroup</td>
			<td>int</td>
			<td><pre lang="json">
1001
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].securityContext.runAsNonRoot</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].securityContext.seLinuxOptions</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].securityContext.seccompProfile.type</td>
			<td>string</td>
			<td><pre lang="json">
"RuntimeDefault"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].volumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.initContainers[0].volumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.persistence.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"lib.pvc-name\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.persistence.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.startupProbe.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>redis.architecture</td>
			<td>string</td>
			<td><pre lang="json">
"standalone"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>redis.auth.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>redis.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Set to "false" to disable the redis cache (if you're using a managed cache service).</td>
		</tr>
		<tr>
			<td>redis.fullnameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-redis"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>requiredSecrets</td>
			<td>object</td>
			<td><pre lang="json">
{
  "postgresSecretName": "postgres-secrets",
  "seqrSecretName": "seqr-secrets"
}
</pre>
</td>
			<td>Secrets which are required for seqr's functionality</td>
		</tr>
		<tr>
			<td>requiredSecrets.postgresSecretName</td>
			<td>string</td>
			<td><pre lang="json">
"postgres-secrets"
</pre>
</td>
			<td>The secret containing the postgres credentials. See the README for information on the format of this secret</td>
		</tr>
		<tr>
			<td>requiredSecrets.seqrSecretName</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-secrets"
</pre>
</td>
			<td>The secret containing the seqr required secrets. See the README for information on the format of this secret</td>
		</tr>
		<tr>
			<td>resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>service.nodePort</td>
			<td>int</td>
			<td><pre lang="json">
30950
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>service.port</td>
			<td>int</td>
			<td><pre lang="json">
8000
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>service.type</td>
			<td>string</td>
			<td><pre lang="json">
"NodePort"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>serviceAccount.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>serviceAccount.create</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>tolerations</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumeMounts</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  mountPath: /var/seqr\n  readOnly: false"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  persistentVolumeClaim:\n    readOnly: false\n    claimName: {{ include \"lib.pvc-name\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>lib.exports.global.lib.persistentVolume.accessMode</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteOnce"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>lib.exports.global.lib.persistentVolume.csi</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>lib.exports.global.lib.persistentVolume.local.nodeSelector</td>
			<td>string</td>
			<td><pre lang="json">
"kind-control-plane"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>lib.exports.global.lib.persistentVolume.local.path</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>lib.exports.global.lib.persistentVolume.storageCapacity</td>
			<td>string</td>
			<td><pre lang="json">
"750Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>lib.exports.global.seqrPlatformDeploy</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
	</tbody>
</table>

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
