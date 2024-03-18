az deployment group create --name cdn-template --resource-group bucklin-portfolio-RG --template-file "ARM_templates/deploy_endpoint.json" --parameters profilePrefix="cdnprofile" endpointName="staticweb"
az deployment group create --name storage-template --resource-group bucklin-portfolio-RG --template-file "ARM_templates/deploy_storage.json" --parameters storagePrefix="store"
