{{/*
Common labels
*/}}
{{- define "lib.labels" -}}
helm.sh/chart: {{printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "lib.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: seqr-platform
{{- end }}

{{/*
Selector labels
*/}}
{{- define "lib.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}


{{/*
Name the PV and PVC
*/}}
{{- define "lib.pv-name" -}}
{{- if .Values.global.lib.persistentVolume.csi.volumeHandle -}}
seqr-platform-pv-{{ print .Values.global.lib.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
seqr-platform-pv
{{- end }}
{{- end }}

{{- define "lib.pvc-name" -}}
{{- if .Values.global.lib.persistentVolume.csi.volumeHandle -}}
seqr-platform-pvc-{{ print .Values.global.lib.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
seqr-platform-pvc
{{- end }}
{{- end }}