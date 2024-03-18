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

## Deploy FunctionApp

az deployment group create `
  --name api-func `
  --resource-group bucklin-portfolio-RG `
  --template-file "ARM_templates/deploy_function_api.json" `
  --parameters storageAccountName="store2kjoo37i24nsw" repoUrl="https://github.com/jonalfarlinga/portfolio" apiPrefix="api_func"

## New GIT Action for API

name: Build and deploy Python project to Azure Function App - bucklin-functions

on:
  push:
    branches:
      - main
  workflow_dispatch:

env:
  AZURE_FUNCTIONAPP_PACKAGE_PATH: '.' # set this to the path to your web app project, defaults to the repository root
  PYTHON_VERSION: '2.11' # set this to the python version to use (supports 3.6, 3.7, 3.8)

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Python version
        uses: actions/setup-python@v0
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Create and start virtual environment
        run: |
          python -m venv venv
          source venv/bin/activate

      - name: Install dependencies
        run: pip install -r requirements.txt

      # Optional: Add step to run tests here

      - name: Zip artifact for deployment
        run: zip release.zip ./* -r

      - name: Upload artifact for deployment job
        uses: actions/upload-artifact@v2
        with:
          name: python-app
          path: |
            release.zip
            !venv/

  deploy:
    runs-on: ubuntu-latest
    needs: build
    environment:
      name: 'production'
      url: ${{ steps.deploy-to-function.outputs.webapp-url }}
    permissions:
      id-token: write #This is required for requesting the JWT

    steps:
      - name: Download artifact from build job
        uses: actions/download-artifact@v2
        with:
          name: python-app

      - name: Unzip artifact for deployment
        run: unzip release.zip

      - name: Login to Azure
        uses: azure/login@v0
        with:
          client-id: ${{ secrets.__clientidsecretname__ }}
          tenant-id: ${{ secrets.__tenantidsecretname__ }}
          subscription-id: ${{ secrets.__subscriptionidsecretname__ }}

      - name: 'Deploy to Azure Functions'
        uses: Azure/functions-action@v0
        id: deploy-to-function
        with:
          app-name: 'bucklin-functions'
          slot-name: 'production'
          package: ${{ env.AZURE_FUNCTIONAPP_PACKAGE_PATH }}
          scm-do-build-during-deployment: true
          enable-oryx-build: true
