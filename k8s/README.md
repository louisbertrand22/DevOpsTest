# Kubernetes Deployment Guide

This directory contains Kubernetes manifests for deploying the DevOpsTest application.

## Files

- **deployment.yml**: Defines the application deployment
- **service.yml**: Defines the ClusterIP service for internal communication
- **ingress.yml**: Defines the Ingress resource for external access with TLS
- **issuer-staging.yaml**: Let's Encrypt staging ClusterIssuer for testing
- **cluster-issuer.yaml**: Let's Encrypt production ClusterIssuer
- **kustomization.yaml**: Kustomize configuration to deploy all resources together

## Quick Start

```bash
# Deploy everything at once
kubectl apply -k .

# Or deploy individually
kubectl apply -f issuer-staging.yaml
kubectl apply -f cluster-issuer.yaml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
```

## Certificate Management

### Understanding the Certificate Flow

1. **Ingress Created**: When the ingress is created, cert-manager sees the `cert-manager.io/cluster-issuer` annotation
2. **Certificate Resource**: cert-manager automatically creates a Certificate resource
3. **Certificate Request**: The Certificate creates a CertificateRequest
4. **ACME Order**: An Order is created with Let's Encrypt
5. **Challenge**: A Challenge is created for domain validation (HTTP-01)
6. **Validation**: Let's Encrypt validates by accessing `http://app.lucho-dev.xyz/.well-known/acme-challenge/<token>`
7. **Certificate Issued**: Once validated, the certificate is issued and stored in the secret specified in the ingress

### Monitoring Certificate Issuance

```bash
# Watch all certificate-related resources
kubectl get certificate,certificaterequest,order,challenge

# Detailed view
kubectl describe certificate devopstest-tls
kubectl describe challenge
```

### Common Issues and Solutions

#### Challenge State: "invalid"

**Symptoms:**
```bash
kubectl get challenge
NAME                                    STATE     DOMAIN              AGE
devopstest-tls-1-213233895-2693839326   invalid   app.lucho-dev.xyz   57m
```

**Possible Causes and Solutions:**

1. **DNS Not Pointing to Cluster**
   ```bash
   # Verify DNS
   nslookup app.lucho-dev.xyz
   
   # Should return the external IP of your ingress controller
   kubectl get svc -n ingress-nginx
   ```

2. **Ingress Controller Not Receiving Traffic**
   ```bash
   # Check ingress controller service has EXTERNAL-IP
   kubectl get svc -n ingress-nginx
   
   # If EXTERNAL-IP is <pending>, check your cloud provider's load balancer
   ```

3. **Port 80 Blocked by Firewall**
   - HTTP-01 challenge requires port 80 to be accessible from the internet
   - Check your cloud provider's security groups/firewall rules
   - Azure AKS: Check Network Security Groups (NSGs)

4. **Wrong Ingress Class**
   ```bash
   # Verify ingress class matches in both ingress and ClusterIssuer
   kubectl get ingress devopstest-ingress -o yaml | grep -A 2 "class"
   
   # Should show:
   #   kubernetes.io/ingress.class: nginx
   #   ingressClassName: nginx
   ```

5. **cert-manager Not Running**
   ```bash
   # Check cert-manager pods
   kubectl get pods -n cert-manager
   
   # All pods should be Running
   ```

#### Recreating Certificate After Fixing Issues

```bash
# Delete the failed certificate and secret
kubectl delete certificate devopstest-tls
kubectl delete secret devopstest-tls

# Delete and recreate the ingress to trigger new certificate request
kubectl delete ingress devopstest-ingress
kubectl apply -f ingress.yml

# Monitor the new certificate request
kubectl get certificate --watch
```

### Switching from Staging to Production

The default configuration uses Let's Encrypt staging for testing. Once everything works:

1. **Edit ingress.yml**:
   ```yaml
   annotations:
     cert-manager.io/cluster-issuer: letsencrypt-prod  # Changed from letsencrypt-staging
   ```

2. **Delete old certificate and apply**:
   ```bash
   kubectl delete secret devopstest-tls
   kubectl delete certificate devopstest-tls
   kubectl apply -f ingress.yml
   ```

3. **Verify production certificate**:
   ```bash
   kubectl get certificate devopstest-tls
   # Status should show Ready: True
   
   # Test in browser - should show valid certificate
   curl -v https://app.lucho-dev.xyz
   ```

## Debugging Tips

### Check ACME Challenge Endpoint

```bash
# The challenge creates a temporary pod and service
# Let's Encrypt will try to access:
# http://app.lucho-dev.xyz/.well-known/acme-challenge/<token>

# You can test this manually:
kubectl get challenge -o yaml

# Look for the token in the challenge spec
# Then test:
curl http://app.lucho-dev.xyz/.well-known/acme-challenge/<token>
```

### Check cert-manager Logs

```bash
# Controller logs
kubectl logs -n cert-manager deploy/cert-manager

# Webhook logs
kubectl logs -n cert-manager deploy/cert-manager-webhook

# CA injector logs
kubectl logs -n cert-manager deploy/cert-manager-cainjector
```

### Verify Ingress Controller Configuration

```bash
# Check if ingress controller is processing the ingress
kubectl logs -n ingress-nginx deploy/ingress-nginx-controller

# Check ingress details
kubectl describe ingress devopstest-ingress
```

## Production Checklist

Before going to production:

- [ ] DNS A record points to cluster external IP
- [ ] cert-manager is installed and running
- [ ] NGINX Ingress Controller is installed and has external IP
- [ ] Tested certificate issuance with staging issuer
- [ ] Port 80 and 443 are open in firewall
- [ ] Switched to production issuer
- [ ] Verified certificate is trusted in browser
- [ ] Tested application access via HTTPS

## Additional Resources

- [cert-manager Documentation](https://cert-manager.io/docs/)
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)
- [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)
- [Troubleshooting cert-manager](https://cert-manager.io/docs/troubleshooting/)
