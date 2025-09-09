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
{{- define "seqr.requiredSecrets" -}}
- name: POSTGRES_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ .Values.requiredSecrets.postgresSecretName }}
      key: password
- name: DJANGO_KEY
  valueFrom:
    secretKeyRef:
      name: {{ .Values.requiredSecrets.seqrSecretName }}
      key: django_key
- name: CLICKHOUSE_READER_PASSWORD
  valueFrom:
    secretKeyRef:
      name: clickhouse-secrets
      key: reader_password
      optional: true
- name: CLICKHOUSE_WRITER_PASSWORD
  valueFrom:
    secretKeyRef:
      name: clickhouse-secrets
      key: writer_password
      optional: true
{{- end }}
