# pipeline-runner

![Version: 0.1.2-dev](https://img.shields.io/badge/Version-0.1.2--dev-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: e15e33e99648d7a765d1e204bb6c6bc92a40b0f9](https://img.shields.io/badge/AppVersion-e15e33e99648d7a765d1e204bb6c6bc92a40b0f9-informational?style=flat-square)

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
| file://../lib | lib | 0.1.3 |

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
			<td>environment.SHOULD_TRIGGER_HAIL_BACKEND_RELOAD</td>
			<td>string</td>
			<td><pre lang="json">
"1"
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
"{{- range $r := list \"GRCh37\" \"GRCh38\" }}\n{{- range $s := list \"rsync_reference_data\" \"download_vep_data\"}}\n- name: {{ $s | replace \"_\" \"-\" }}-{{ $r | lower}}\n  image: \"{{ $.Values.image.repository }}:{{ $.Values.image.tag | default $.Chart.AppVersion }}\"\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: [\"/v03_pipeline/bin/{{ $s }}.bash\", \"{{ $r }}\"]\n  resources:\n    requests:\n      memory: \"16Gi\"\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}\n{{- end }}\n{{- end }}"
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
			<td>pods[0].sidecar.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Gi"
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
"- name: mkdir-luigi-state\n  image: busybox:1.35\n  imagePullPolicy: {{ $.Values.image.pullPolicy }}\n  command: ['/bin/mkdir', '-p', '/seqr/luigi-state']\n  {{- with $.Values.volumeMounts }}\n  volumeMounts:\n    {{- tpl . $ | nindent 4 }}\n  {{- end }}"
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
30901
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
			<td>replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
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
"- name: seqr-datasets\n  mountPath: /seqr\n  readOnly: false"
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
	</tbody>
</table>

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
