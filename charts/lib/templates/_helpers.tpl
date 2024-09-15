{{/*
Common labels
*/}}
{{- define "seqr-platform.labels" -}}
helm.sh/chart: {{printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "seqr-platform.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: seqr-platform
{{- end }}

{{/*
Selector labels
*/}}
{{- define "seqr-platform.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}


{{/*
Name the PV and PVC
*/}}
{{- define "seqr-platform.pv-name" -}}
{{- if index .Values.global "seqr-platform" "persistentVolume" "csi" "volumeHandle" -}}
seqr-platform-pv-{{ print index .Values.global "seqr-platform" "persistentVolume" "csi" "volumeHandle" | sha256sum | trunc 5}}
{{- else -}}
seqr-platform-pv
{{- end }}
{{- end }}

{{- define "seqr-platform.pvc-name" -}}
{{- if index .Values.global "seqr-platform" "persistentVolume" "csi" "volumeHandle" -}}
seqr-platform-pvc-{{ print index .Values.global "seqr-platform" "persistentVolume" "csi" "volumeHandle" | sha256sum | trunc 5}}
{{- else -}}
seqr-platform-pvc
{{- end }}
{{- end }}