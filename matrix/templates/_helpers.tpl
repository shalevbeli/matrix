{{/*
Expand the name of the chart.
*/}}
{{- define "matrix.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "matrix.fullname" -}}
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
{{- define "matrix.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels - client
*/}}
{{- define "matrix.labels-client" -}}
helm.sh/chart: {{ include "matrix.chart" . }}
{{ include "matrix.selectorLabels-client" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Common labels - server
*/}}
{{- define "matrix.labels-server" -}}
helm.sh/chart: {{ include "matrix.chart" . }}
{{ include "matrix.selectorLabels-server" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Common labels - mongo
*/}}
{{- define "matrix.labels-mongo" -}}
helm.sh/chart: {{ include "matrix.chart" . }}
{{ include "matrix.selectorLabels-mongo" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Common labels - mongo-compass
*/}}
{{- define "matrix.labels-mongocompass" -}}
helm.sh/chart: {{ include "matrix.chart" . }}
{{ include "matrix.selectorLabels-mongocompass" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels for client
*/}}
{{- define "matrix.selectorLabels-client" -}}
app.kubernetes.io/name: "client"
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Selector labels for server
*/}}
{{- define "matrix.selectorLabels-server" -}}
app.kubernetes.io/name: "server"
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Selector labels for mongo
*/}}
{{- define "matrix.selectorLabels-mongo" -}}
app.kubernetes.io/name: "mongo"
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Selector labels for mongo-compass
*/}}
{{- define "matrix.selectorLabels-mongocompass" -}}
app.kubernetes.io/name: "mongo-compass"
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}