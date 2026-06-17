apiVersion: apps/v1
kind: Deployment
metadata:
  name: retailpulse
  namespace: default
  labels:
    app: retailpulse
    version: "1.0"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: retailpulse
  template:
    metadata:
      labels:
        app: retailpulse
    spec:
      containers:
        - name: retailpulse
          image: your-registry/retailpulse:latest   # replace with your image
          imagePullPolicy: Always
          ports:
            - containerPort: 8501
          env:
            - name: STREAMLIT_SERVER_PORT
              value: "8501"
            - name: STREAMLIT_BROWSER_GATHER_USAGE_STATS
              value: "false"
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2000m"
              memory: "4Gi"
          livenessProbe:
            httpGet:
              path: /_stcore/health
              port: 8501
            initialDelaySeconds: 60
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /_stcore/health
              port: 8501
            initialDelaySeconds: 30
            periodSeconds: 10
          volumeMounts:
            - name: data-volume
              mountPath: /app/data
            - name: models-volume
              mountPath: /app/models
      volumes:
        - name: data-volume
          persistentVolumeClaim:
            claimName: retailpulse-data-pvc
        - name: models-volume
          persistentVolumeClaim:
            claimName: retailpulse-models-pvc
