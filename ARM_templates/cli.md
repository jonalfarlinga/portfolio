# Deployment Templates for Storage Account and CDN

## Deploy Static Account

az deployment group create `
  --name storage-template `
  --resource-group bucklin-portfolio-RG `
  --template-file "ARM_templates/deploy_storage.json" `
  --parameters storagePrefix="store"

After deploying, navigate to the storage account on Azure Portal and enable Static websites.

## Deploy CDN Profile and Endpoint

az deployment group create `
  --name cdn-template `
  --resource-group bucklin-portfolio-RG `
  --template-file "ARM_templates/deploy_endpoint.json" `
  --parameters profilePrefix="cdnprofile" endpointName="staticweb"
