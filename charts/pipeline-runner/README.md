# pipeline-runner

![Version: 2.61.0](https://img.shields.io/badge/Version-2.61.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4b1aab2c33c8b13d56768027971dff1e8c23fe24](https://img.shields.io/badge/AppVersion-4b1aab2c33c8b13d56768027971dff1e8c23fe24-informational?style=flat-square)

A Helm chart for deploying the loading pipeline of Seqr, an open source software platform for rare disease genomics

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| seqr | <seqr@broadinstitute.org> |  |

## Source Code

* <https://github.com/broadinstitute/seqr-helm>
* <https://github.com/broadinstitute/seqr-loading-pipelines>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../lib | lib | 1.1.0 |

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
			<td>additionalSecrets[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"CLICKHOUSE_WRITER_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>additionalSecrets[0].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"writer_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>additionalSecrets[0].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"clickhouse-secrets"
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
			<td>deploymentAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.CLICKHOUSE_WRITER_USER</td>
			<td>string</td>
			<td><pre lang="json">
"seqr_clickhouse_writer"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.LUIGI_STATE_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/luigi-state"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.PIPELINE_DATA_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/pipeline-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment.REFERENCE_DATASETS_DIR</td>
			<td>string</td>
			<td><pre lang="json">
"/var/seqr/seqr-reference-data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.seqr.environment</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
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
			<td>hailWorkerResources</td>
			<td>string</td>
			<td><pre lang="json">
"requests:\n  memory: \"12Gi\""
</pre>
</td>
			<td></td>
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
"gcr.io/seqr-project/seqr-pipeline-runner"
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
			<td>initRsyncEnabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>networkPolicy.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
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
			<td>pods[0].command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"python3"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].command[1]</td>
			<td>string</td>
			<td><pre lang="json">
"-m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].command[2]</td>
			<td>string</td>
			<td><pre lang="json">
"v03_pipeline.api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].healthCheckRoute</td>
			<td>string</td>
			<td><pre lang="json">
"/status"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].initContainers</td>
			<td>string</td>
			<td><pre lang="json">
"{{- if $.Values.initRsyncEnabled }}\n{{- range $r := list \"GRCh37\" \"GRCh38\" }}\n{{- range $s := list \"rsync_reference_data\" \"download_vep_reference_data\"}}\n- name: {{ $s | replace \"_\" \"-\" }}-{{ $r | lower}}\n  image: \"{{ $.Values.image.repository }}:{{ $.Values.image.tag | default $.Chart.AppVersion }}\"\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: [\"/v03_pipeline/bin/{{ $s }}.bash\", \"{{ $r }}\"]\n  envFrom:\n    - configMapRef:\n        name: {{ $.Chart.Name }}\n  {{- with $.Values.hailWorkerResources }}\n  resources:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}\n{{- end }}\n{{- end }}\n{{- else }}\n  []\n{{- end }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].service.port</td>
			<td>int</td>
			<td><pre lang="json">
6000
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].service.type</td>
			<td>string</td>
			<td><pre lang="json">
"ClusterIP"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].sidecar.command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"python3"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].sidecar.command[1]</td>
			<td>string</td>
			<td><pre lang="json">
"-m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].sidecar.command[2]</td>
			<td>string</td>
			<td><pre lang="json">
"v03_pipeline.bin.pipeline_worker"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[0].sidecar.privileged</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].command[0]</td>
			<td>string</td>
			<td><pre lang="json">
"luigid"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].healthCheckRoute</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].initContainers</td>
			<td>string</td>
			<td><pre lang="json">
"- name: mkdir-luigi-state\n  image: busybox:1.35\n  imagePullPolicy: {{ .Values.image.pullPolicy }}\n  command: ['/bin/mkdir', '-p', {{ .Values.environment.LUIGI_STATE_DIR }}]\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"ui"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].service.nodePort</td>
			<td>int</td>
			<td><pre lang="json">
30951
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].service.port</td>
			<td>int</td>
			<td><pre lang="json">
8082
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].service.type</td>
			<td>string</td>
			<td><pre lang="json">
"NodePort"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>pods[1].sidecar</td>
			<td>object</td>
			<td><pre lang="json">
{}
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
"- name: seqr-datasets\n  mountPath: /var/seqr\n  readOnly: false\n- name: docker-socket\n  mountPath: /var/run/docker.sock\n  readOnly: false\n- name: luigi-config\n  mountPath: /etc/luigi/luigi.cfg\n  subPath: luigi.cfg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes</td>
			<td>string</td>
			<td><pre lang="json">
"- name: seqr-datasets\n  persistentVolumeClaim:\n    readOnly: false\n    claimName: {{ include \"lib.pvc-name\" . }}\n- name: docker-socket\n  hostPath:\n    path: /var/run/docker.sock\n- name: luigi-config\n  configMap:\n    name: luigi-config\n    items:\n      - key: luigi.cfg\n        path: luigi.cfg"
</pre>
</td>
			<td></td>
		</tr>
	</tbody>
</table>

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
