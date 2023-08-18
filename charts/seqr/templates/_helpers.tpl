{{/*
Expand the name of the chart.
*/}}
{{- define "seqr.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "seqr.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "seqr.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "seqr.labels" -}}
helm.sh/chart: {{ include "seqr.chart" . }}
{{ include "seqr.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "seqr.selectorLabels" -}}
app.kubernetes.io/name: {{ include "seqr.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Seqr environment shared between application and cron
*/}}
{{- define "seqr.environment" -}}
envFrom:
  - configMapRef:
    name: {{ .Release.Name }}-environment
env:
  - name: POSTGRES_PASSWORD
    valueFrom:
      secretKeyRef:
        name: {{ .Values.required_secrets.postgresSecretName }}
        key: password
  - name: DJANGO_KEY
    valueFrom:
      secretKeyRef:
        name: {{ .Values.required_secrets.seqrSecretName }}
        key: django_key
  {{- if .Values.enable_elasticsearch_auth }}
  - name: SEQR_ES_PASSWORD
    valueFrom:
      secretKeyRef:
        name: {{ .Values.required_secrets.seqrSecretName }}
        key: seqr_es_password
  - name: KIBANA_ES_PASSWORD
    valueFrom:
      secretKeyRef:
        name: {{ .Values.required_secrets.kibanaSecretName }}
        key: elasticsearch.password
  {{- end }}
  {{- with .Values.additional_secrets }}
    {{- toYaml . | nindent 10 }}
  {{- end }}
{{- end }}
