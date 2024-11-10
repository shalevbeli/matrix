In order to setup this application you need to follow this steps:
1. Install minikube
   In order to install minikube you should follow this guide depending on your Operating System: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2Fwindows+package+manager#Ingress
2. Install helm
   In order to install helm you should follow this guide: https://helm.sh/docs/intro/install/
3. Install vault
   In order to install vault you should follow this guide: https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install

After installing the prerequertise you need to deploy the following applications:
1. Install the vault deploment and operator using this guide: https://developer.hashicorp.com/vault/tutorials/kubernetes/vault-secrets-operator
   After installing the vault deployment and operator you need to create vault auth object and enable secret engine (like the guide) for the deployments.
   The deployments require the following environment variables:
   mongo - MONGO_INITDB_ROOT_PASSWORD, MONGO_INITDB_ROOT_USERNAME
   client - REACT_APP_SERVER_URL
   server - FLASK_HOST, FLASK_PORT, MONGODB_DBNAME, MONGODB_HOST, MONGODB_PASSWORD, MONGODB_PORT, MONGODB_USERNAME

2. Install argocd using this commands:
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

3. Configure the argocd to work with your git repository
4. deploy the cert-manager operator in your minikube server with this commands:
   helm repo add jetstack https://charts.jetstack.io --force-update
  helm install \
    cert-manager jetstack/cert-manager \
    --namespace cert-manager \
    --create-namespace \
    --version v1.16.1 \
    --set crds.enabled=true

   Final step is to configure the ingress host name you want and modify the /etc/hosts file in your operating system to route requests from
   this host name to ip 127.0.0.1.
   If you are using minikube docker driver you need to use the command minikube tunnel.
