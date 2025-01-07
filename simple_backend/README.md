# File Structure

```bash
app/
├── backend-fastapi/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
├── node-api/
│   ├── Dockerfile
│   ├── server.js
│   ├── package.json
├── kubernetes/
│   ├── fastapi.yaml
│   ├── node-api.yaml
│   ├── postgresql.yaml
├── docker-compose.yaml

```

## Deploy on Kubernetes
Start Minikube:

```bash
minikube start
```
Apply all manifests:

```bash
kubectl apply -f kubernetes/postgresql.yaml
kubectl apply -f kubernetes/fastapi.yaml
kubectl apply -f kubernetes/node-api.yaml
```

Check resources:

```bash
kubectl get pods
kubectl get services
```

Expose the Node.js API:

```bash
minikube service node-service
```

## Test the Application
Send a request to the Node.js API:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"a": 5, "b": 10}' http://<NODE_SERVICE_URL>/api/calculate
```
The response will include the calculation result:

```json
{"result": 15}
```