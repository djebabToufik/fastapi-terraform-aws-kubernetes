# FastAPI deployment using docker AWS Terraform and kubernetes

## prerequisites
1. AWS account with activated payment
2. AWS CLI installed and configured in your local. [Getting started](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

3. [Kubectl](https://kubernetes.io/docs/tasks/tools/)
4. [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
5. Python >= 3.8 


## Useful links

1. [Terraform aws Doc](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
2. [Kuber Docs](https://kubernetes.io/docs/concepts/)

## deployment
1. Build the docker image and push it to your favourite hub.
```sh
docker build -t fastapi-test:latest # build and tag the image
docker push fastapi-test:latest # build and tag the image
```
2. Provision aws resources, this will create a vpc, iam role, cluster and cluster node groups mainly and other dependencies.
```sh
cd terraform
terraform init
terraform validate # to make sure it all good
terraform apply
```
it should look like this
``` 
Apply complete! Resources: 56 added, 0 changed, 0 destroyed.

Outputs:

access_entries = {
  "cluster_creator" = { .....
```
3. Deploy  the images using kubernetes, first go to the kubernetes directory and then :
- Change the deployment file, in the section image 
```yaml
spec:
      containers:
      - name: fastapi-test
        image: aws-id.dkr.ecr.[region].amazonaws.com/fastapi-test:latest # make sure to put the right image url
```
- deploy the pods 
```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
and it should look like this 
```
deployment.apps/fastapi-test created
service/fastapi-test-service created
```
4. Access to the public url, you can get it by excuting this command:
```
kubectl get svc fastapi-test-service

NAME             TYPE           CLUSTER-IP       EXTERNAL-IP                             PORT(S)        AGE
nginx-service   LoadBalancer   xx.xxx.xxx.x     http://id.region.elb.amazonaws.com/      80:xxx/TCP     0m
```
