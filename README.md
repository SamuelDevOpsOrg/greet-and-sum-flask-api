# Greet-And-Sum Flask API

## Services/Tools: GitHub Actions, Flask, Python, Docker, ACR, Azure Container Apps

## Deployment Description

Configured a CI/CD pipeline to build and deploy a Python Flask REST Api to Azure Container Apps using GitHub Actions.

Pipeline Stages:
1. Build
2. Test
3. Deploy

## API Description

This is a simple Python API built using Flask. It includes three endpoints: a root route returning a "Hello, World!" message, a dynamic greeting route, and a POST route for adding two numbers.

## API Endpoints

```
    1. **GET /**

    Returns a simple "Hello, World!!" message.

    2. **GET /greet/<name>**

    Greets a user by name.

    3. **POST /add**
    Adds two numbers provided in the JSON body.
```