{{/*
Common labels
*/}}
{{- define "seqr.labels" -}}
helm.sh/chart: {{printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "seqr.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: seqr-platform
{{- end }}

{{/*
Selector labels
*/}}
{{- define "seqr.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Seqr environment shared between application and cron
*/}}
{{- define "seqr.environment" -}}
envFrom:
  - configMapRef:
      name: {{ .Chart.Name }}
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
  {{- end }}
  {{- with .Values.additional_secrets }}
    {{- toYaml . | nindent 2}}
  {{- end }}
{{- end }}
