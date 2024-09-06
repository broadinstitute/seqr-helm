{{/*
Common labels
*/}}
{{- define "pipeline-runner.labels" -}}
helm.sh/chart: {{printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "pipeline-runner.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: seqr-platform
{{- end }}

{{/*
Selector labels
*/}}
{{- define "pipeline-runner.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "hail-search.pvc-name" -}}
{{- if .Values.global.hail_search.persistentVolume.csi.volumeHandle -}}
hail-search-pvc-{{ print .Values.global.hail_search.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
hail-search-pvc
{{- end }}
{{- end }}