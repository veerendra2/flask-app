# HEX to RGB Flask App
## Introduction
A simple application exposes an endpoint that takes a HEX color and returns its RGB representation, implemented in Python `Flask` framework. 

##### `POST`

`curl -X POST -H 'Content-Type: application/json' -d '{"code": "<HEX color code>"}' <app-ulr>`

## Deployment

```
+--------------------------------------------------------+
|                                                        |
|                                                        |
|                  +------------------------------+      |
|                  |                              |      |
|        +---------------+                        |      |
|        | mod_wsgi|     |   APACHE WEB SERVER    +<---------------------- Requests
|        ++--------------+                        |      |
|         |        |                              |      |
|         |        +------------------------------+      |
|         |                                              |
|         |                                              |
|         |        +------------------------------+      |
|         |        |                              |      |
|         +------->+       Python Flask App       |      |
|                  |                              |      |
|                  +------------------------------+      |
|                                                        |
|                                                        |
+--------------------------------------------------------+
```

## Containerization
```
QUAY_USER=""
QUAY_PASS=""

sudo docker build -t color .
sudo docker tag color:latest quay.io/$QUAY_USER/color:latest
sudo docker push quay.io/$QUAY_USER/color:latest
```

Kubernetes deployment manifest files to deploy on K8s cluster.
```
$ kubectl create -f app-deployment.yaml
$ kubectl create -f app-hpa.yaml
```

* `app-deployment.yaml` deploys app pod and creates K8s `service` with type as `NodePort`.
* `app-hpa.yaml` creates [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) for scalability 

**NOTE**: In order to work `HPA`, the K8s cluster should have `metric-server` installed

## Deploy on `minikube`
> Minikube is a tool that makes it easy to run Kubernetes locally. Minikube runs a single-node Kubernetes cluster inside a Virtual Machine (VM) on your laptop for users looking to try out Kubernetes or develop with it day-to-day.
 

Get the `minikube` cluster info like below and run `test.py`
```
## Make sure minikube up and running
$ minikube ip
192.168.39.228

## Copy the cluster node IP

## Make app running in minikube cluster
$ kubectl get svc colors -o wide
NAME     TYPE       CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE   SELECTOR
colors   NodePort   10.111.37.3   <none>        80:32438/TCP   93m   name=color

## Copy Nodeport

## Run test script to test it
$ python test.py 192.168.39.228 32438
[+] Running Positive Test Cases
[*] PAYLOAD => {"code": "#C0C0C0"}, RESPONSE=> {"result": "(192, 192, 192)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#808080"}, RESPONSE=> {"result": "(128, 128, 128)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#000000"}, RESPONSE=> {"result": "(0, 0, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#FF0000"}, RESPONSE=> {"result": "(255, 0, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#800000"}, RESPONSE=> {"result": "(128, 0, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#FFFF00"}, RESPONSE=> {"result": "(255, 255, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#808000"}, RESPONSE=> {"result": "(128, 128, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#00FF00"}, RESPONSE=> {"result": "(0, 255, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#008000"}, RESPONSE=> {"result": "(0, 128, 0)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#00fFFF"}, RESPONSE=> {"result": "(0, 255, 255)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#008080"}, RESPONSE=> {"result": "(0, 128, 128)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#0000FF"}, RESPONSE=> {"result": "(0, 0, 255)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#000080"}, RESPONSE=> {"result": "(0, 0, 128)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#fF00FF"}, RESPONSE=> {"result": "(255, 0, 255)"}, RESPOSE CODE=> 200
[*] PAYLOAD => {"code": "#800080"}, RESPONSE=> {"result": "(128, 0, 128)"}, RESPOSE CODE=> 200
[+] Running Negetive Test Cases
[.] PAYLOAD => {"code": "#GGGGGGG"}, RESPONSE=> {"result": "Invalid POST data/HEX color code"}, RESPOSE CODE=> 400
[.] PAYLOAD => {"code": "#12121212FF"}, RESPONSE=> {"result": "Invalid POST data/HEX color code"}, RESPOSE CODE=> 400
[.] PAYLOAD => {"code": "$0000FF"}, RESPONSE=> {"result": "Invalid POST data/HEX color code"}, RESPOSE CODE=> 400
[.] PAYLOAD => {"code": "#$A0000"}, RESPONSE=> {"result": "Invalid POST data/HEX color code"}, RESPOSE CODE=> 400
[.] PAYLOAD => {"code": "#AAAA7"}, RESPONSE=> {"result": "Invalid POST data/HEX color code"}, RESPOSE CODE=> 400
[.] PAYLOAD => {"code": "AAAAFF"}, RESPONSE=> {"result": "Invalid POST data/HEX color code"}, RESPOSE CODE=> 400

```

## Metrics
Added basic instrumentation to get application metrics with help of `prometheus-flask-exporter` which are exportable to [Prometheus](https://prometheus.io/). This module by default exposes the metrics on application port `/metrics` endpoint.

## Project Tree
```
.
├── app
│   ├── colors_app
│   │   └── __init__.py
│   └── colors_app.wsgi
├── app-deployment.yaml
├── app-hpa.yaml
├── build.sh
├── cadvisor-daemonset.yml
├── Dockerfile
├── httpd.conf
├── LICENSE
├── metrics_list.txt
├── README.md
└── test.py

```

