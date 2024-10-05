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
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.affinity</td>
			<td>string</td>
			<td><pre lang="json">
"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.deploymentAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.environment.HAIL_SEARCH_DATA_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr/seqr-hail-search-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.environment.REFERENCE_DATASETS_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr/seqr-reference-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.image.pullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"Always"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"gcr.io/seqr-project/seqr-hail-search"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.imagePullSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.initContainers</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.nodeSelector</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.podAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.service.port</td>
			<td>int</td>
			<td><pre lang="json">
5000
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.service.type</td>
			<td>string</td>
			<td><pre lang="json">
"ClusterIP"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.serviceAccount.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.serviceAccount.create</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.tolerations</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.volumeMounts</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  mountPath: /seqr\n  readOnly: true"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.volumes</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  persistentVolumeClaim:\n    readOnly: true\n    claimName: {{ include \"lib.pvc-name\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.lib.exports.global.lib.persistentVolume.accessMode</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteOnce"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.lib.exports.global.lib.persistentVolume.csi</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.lib.exports.global.lib.persistentVolume.local.nodeSelector</td>
			<td>string</td>
			<td><pre lang="json">
"kind-control-plane"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.lib.exports.global.lib.persistentVolume.local.path</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.lib.exports.global.lib.persistentVolume.storageCapacity</td>
			<td>string</td>
			<td><pre lang="json">
"750Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>hail-search.lib.exports.global.seqrPlatformDeploy</td>
			<td>bool</td>
			<td><pre lang="json">
false
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
"/seqr"
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
		<tr>
			<td>pipeline-runner.affinity</td>
			<td>string</td>
			<td><pre lang="json">
"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.deploymentAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.environment.SHOULD_TRIGGER_HAIL_BACKEND_RELOAD</td>
			<td>string</td>
			<td><pre lang="json">
"1"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.image.pullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"Always"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"gcr.io/seqr-project/seqr-pipeline-runner"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.imagePullSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.nodeSelector</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.podAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"python3"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].command[1]</td>
			<td>string</td>
			<td><pre lang="json">
"-m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].command[2]</td>
			<td>string</td>
			<td><pre lang="json">
"v03_pipeline.api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].healthCheckRoute</td>
			<td>string</td>
			<td><pre lang="json">
"/status"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].initContainers</td>
			<td>string</td>
			<td><pre lang="json">
"{{- range $r := list \"GRCh37\" \"GRCh38\" }}\n{{- range $s := list \"rsync_reference_data\" \"download_vep_data\"}}\n- name: {{ $s | replace \"_\" \"-\" }}-{{ $r | lower}}\n  image: \"{{ $.Values.image.repository }}:{{ $.Values.image.tag | default $.Chart.AppVersion }}\"\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: [\"/v03_pipeline/bin/{{ $s }}.bash\", \"{{ $r }}\"]\n  resources:\n    requests:\n      memory: \"16Gi\"\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}\n{{- end }}\n{{- end }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].service.port</td>
			<td>int</td>
			<td><pre lang="json">
6000
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].service.type</td>
			<td>string</td>
			<td><pre lang="json">
"ClusterIP"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].sidecar.command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"python3"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].sidecar.command[1]</td>
			<td>string</td>
			<td><pre lang="json">
"-m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].sidecar.command[2]</td>
			<td>string</td>
			<td><pre lang="json">
"v03_pipeline.bin.pipeline_worker"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].sidecar.privileged</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[0].sidecar.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"luigid"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].healthCheckRoute</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].initContainers</td>
			<td>string</td>
			<td><pre lang="json">
"- name: mkdir-luigi-state\n  image: busybox:1.35\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: ['/bin/mkdir', '-p', '/seqr/luigi-state']\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"ui"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].service.nodePort</td>
			<td>int</td>
			<td><pre lang="json">
30901
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].service.port</td>
			<td>int</td>
			<td><pre lang="json">
8082
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].service.type</td>
			<td>string</td>
			<td><pre lang="json">
"NodePort"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.pods[1].sidecar</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.serviceAccount.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.serviceAccount.create</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.tolerations</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.volumeMounts</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  mountPath: /seqr\n  readOnly: false"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.volumes</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  persistentVolumeClaim:\n    readOnly: false\n    claimName: {{ include \"lib.pvc-name\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.lib.exports.global.lib.persistentVolume.accessMode</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteOnce"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.lib.exports.global.lib.persistentVolume.csi</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.lib.exports.global.lib.persistentVolume.local.nodeSelector</td>
			<td>string</td>
			<td><pre lang="json">
"kind-control-plane"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.lib.exports.global.lib.persistentVolume.local.path</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.lib.exports.global.lib.persistentVolume.storageCapacity</td>
			<td>string</td>
			<td><pre lang="json">
"750Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pipeline-runner.lib.exports.global.seqrPlatformDeploy</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.additionalSecrets</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional Secrets (defined directly as yaml)</td>
		</tr>
		<tr>
			<td>seqr.affinity</td>
			<td>string</td>
			<td><pre lang="json">
"podAntiAffinity:\n  preferredDuringSchedulingIgnoredDuringExecution:\n    - weight: 1.0\n      podAffinityTerm:\n        labelSelector:\n          matchExpressions:\n            - key: \"app.kubernetes.io/part-of\"\n              operator: In\n              values:\n              - \"seqr-platform\"\n        topologyKey: \"kubernetes.io/hostname\""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.cronJobs[0].command</td>
			<td>string</td>
			<td><pre lang="json">
"python manage.py check_for_new_samples_from_pipeline"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.cronJobs[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"check-new-samples-job"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.cronJobs[0].schedule</td>
			<td>string</td>
			<td><pre lang="json">
"*/10 * * * *"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.deploymentAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.GUNICORN_WORKER_THREADS</td>
			<td>string</td>
			<td><pre lang="json">
"4"
</pre>
</td>
			<td>The number of threads to allocate to the gunicorn server</td>
		</tr>
		<tr>
			<td>seqr.environment.HAIL_BACKEND_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"hail-search"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.HAIL_BACKEND_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"5000"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.HAIL_SEARCH_DATA_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr/seqr-hail-search-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.LOADING_DATASETS_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr/seqr-loading-temp"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.PIPELINE_RUNNER_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"pipeline-runner"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.PIPELINE_RUNNER_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"5000"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.environment.POSTGRES_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-postgresql"
</pre>
</td>
			<td>The hostname to use for the postgres database connectsion</td>
		</tr>
		<tr>
			<td>seqr.environment.POSTGRES_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"5432"
</pre>
</td>
			<td>The TCP port number to use for the postgres database connection</td>
		</tr>
		<tr>
			<td>seqr.environment.POSTGRES_USERNAME</td>
			<td>string</td>
			<td><pre lang="json">
"postgres"
</pre>
</td>
			<td>The username to use for the postgres database connection</td>
		</tr>
		<tr>
			<td>seqr.environment.REDIS_SERVICE_HOSTNAME</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-redis-master"
</pre>
</td>
			<td>The hostname of the redis cache that seqr should use</td>
		</tr>
		<tr>
			<td>seqr.environment.REDIS_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"6379"
</pre>
</td>
			<td>The port of the redis cache that seqr should use</td>
		</tr>
		<tr>
			<td>seqr.environment.SEQR_SERVICE_PORT</td>
			<td>string</td>
			<td><pre lang="json">
"8000"
</pre>
</td>
			<td>The port that the seqr server should listen on</td>
		</tr>
		<tr>
			<td>seqr.environment.STATIC_MEDIA_DIR</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>If storing static media files in a local filesystem, the path to that filesystem</td>
		</tr>
		<tr>
			<td>seqr.image.pullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"Always"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"gcr.io/seqr-project/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.image.tag</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.imagePullSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.jobAfterHook</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.jobBeforeHook</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.nodeSelector</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.podAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.architecture</td>
			<td>string</td>
			<td><pre lang="json">
"standalone"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.auth.existingSecret</td>
			<td>string</td>
			<td><pre lang="json">
"postgres-secrets"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.auth.secretKeys.adminPasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"postgres"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.fullnameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-postgresql"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.image.tag</td>
			<td>string</td>
			<td><pre lang="json">
"12.19.0-debian-12-r9"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.postgresqlDataDir</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr/postgresql-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"/bin/sh"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].command[1]</td>
			<td>string</td>
			<td><pre lang="json">
"-ec"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].command[2]</td>
			<td>string</td>
			<td><pre lang="json">
"mkdir -p {{ .Values.postgresqlDataDir }}\nchown -R `id -u`:`id -G | cut -d \" \" -f2` {{ .Values.postgresqlDataDir }}\n"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].image</td>
			<td>string</td>
			<td><pre lang="json">
"{{- include \"postgresql.v1.volumePermissions.image\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].imagePullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"IfNotPresent"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-postgresql-init-chmod-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].securityContext.runAsGroup</td>
			<td>int</td>
			<td><pre lang="json">
0
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].securityContext.runAsNonRoot</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].securityContext.seLinuxOptions</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].securityContext.seccompProfile.type</td>
			<td>string</td>
			<td><pre lang="json">
"RuntimeDefault"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].volumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.initContainers[0].volumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.persistence.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"lib.pvc-name\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.persistence.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.postgresql.primary.startupProbe.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.redis.architecture</td>
			<td>string</td>
			<td><pre lang="json">
"standalone"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.redis.auth.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.redis.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.redis.fullnameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-redis"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.requiredSecrets</td>
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
			<td>seqr.requiredSecrets.postgresSecretName</td>
			<td>string</td>
			<td><pre lang="json">
"postgres-secrets"
</pre>
</td>
			<td>The secret containing the postgres credentials. See the README for information on the format of this secret</td>
		</tr>
		<tr>
			<td>seqr.requiredSecrets.seqrSecretName</td>
			<td>string</td>
			<td><pre lang="json">
"seqr-secrets"
</pre>
</td>
			<td>The secret containing the seqr required secrets. See the README for information on the format of this secret</td>
		</tr>
		<tr>
			<td>seqr.resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.service.nodePort</td>
			<td>int</td>
			<td><pre lang="json">
30950
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.service.port</td>
			<td>int</td>
			<td><pre lang="json">
8000
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.service.type</td>
			<td>string</td>
			<td><pre lang="json">
"NodePort"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.serviceAccount.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.serviceAccount.create</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.tolerations</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.volumeMounts</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.volumes</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.lib.exports.global.lib.persistentVolume.accessMode</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteOnce"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.lib.exports.global.lib.persistentVolume.csi</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.lib.exports.global.lib.persistentVolume.local.nodeSelector</td>
			<td>string</td>
			<td><pre lang="json">
"kind-control-plane"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.lib.exports.global.lib.persistentVolume.local.path</td>
			<td>string</td>
			<td><pre lang="json">
"/seqr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.lib.exports.global.lib.persistentVolume.storageCapacity</td>
			<td>string</td>
			<td><pre lang="json">
"750Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>seqr.lib.exports.global.seqrPlatformDeploy</td>
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
