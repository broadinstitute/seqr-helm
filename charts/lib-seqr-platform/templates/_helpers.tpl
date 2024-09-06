{{/*
Name the PV and PVC
*/}}
{{- define "seqr-platform.pv-name" -}}
{{- if .Values.global.seqr_platform.persistentVolume.csi.volumeHandle -}}
seqr-platform-pv-{{ print .Values.global.seqr_platform.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
seqr-platform-pv
{{- end }}
{{- end }}

{{- define "seqr-platform.pvc-name" -}}
{{- if .Values.global.seqr_platform.persistentVolume.csi.volumeHandle -}}
seqr-platform-pvc-{{ print .Values.global.seqr_platform.persistentVolume.csi.volumeHandle | sha256sum | trunc 5}}
{{- else -}}
seqr-platform-pvc
{{- end }}
{{- end }}