{{/*
Common labels
*/}}
{{- define "hail-search.labels" -}}
helm.sh/chart: {{printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "hail-search.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: seqr-platform
{{- end }}

{{/*
Selector labels
*/}}
{{- define "hail-search.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Name the PV and PVC
*/}}
{{- define "hail-search.pv-name" -}}
{{- if .Values.persistentVolume.csi.volumeHandle -}}
{{ .Chart.Name }}-pv-{{ print .Values.global.hail_search.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
{{ .Chart.Name }}-pv
{{- end }}
{{- end }}

{{- define "hail-search.pvc-name" -}}
{{- if .Values.persistentVolume.csi.volumeHandle -}}
{{ .Chart.Name }}-pvc-{{ print .Values.global.hail_search.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
{{ .Chart.Name }}-pvc
{{- end }}
{{- end }}
