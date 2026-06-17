apiVersion: v1
kind: Service
metadata:
  name: retailpulse-service
  namespace: default
  labels:
    app: retailpulse
spec:
  type: LoadBalancer
  selector:
    app: retailpulse
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8501
