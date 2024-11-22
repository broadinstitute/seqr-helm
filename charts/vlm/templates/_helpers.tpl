{{/*
Common labels
*/}}
{{- define "vlm.labels" -}}
helm.sh/chart: {{printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "vlm.selectorLabels" . }}
{{ include "vlm.podMatchLabel" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: seqr-platform
{{- end }}

{{/*
Selector labels
*/}}
{{- define "vlm.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Single label for the pod match expression
*/}}
{{- define "vlm.podMatchLabel" -}}
podType: {{ .Chart.Name }}-{{ .Release.Name }}
{{- end }}
