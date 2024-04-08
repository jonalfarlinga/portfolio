# Deployment Templates for Storage Account and CDN

## Deploy Storage Account and FunctionApp

az deployment group create `
  --name api-func `
  --resource-group bucklin-portfolio-RG `
  --template-file "ARM_templates/deploy_function_api.json" `
  --parameters repoUrl="https://github.com/jonalfarlinga/portfolio" apiPrefix="apifunc" storagePrefix="store" domainName="portfolio.denny-bucklin.net"

After deploying, navigate to the storage account on Azure Portal and enable Static websites.

## Deploy CDN Profile and Endpoint

az deployment group create `
  --name cdn-template `
  --resource-group bucklin-portfolio-RG `
  --template-file "ARM_templates/deploy_endpoint.json" `
  --parameters profilePrefix="cdnprofile" endpointName="staticweb" storageAccountName="store2kjoo37i24nsw"
