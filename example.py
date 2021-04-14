from src.swagger.scann import toJson, getApisName
import requests 
print("Test")
urlSwagger = "https://petstore.swagger.io/v2/swagger.json"
urlSwagger = "https://edutelling-api-develop.openshift.techgap.it/api/v1/api-docs/swagger-ui-init.js"

swaggerResponse =toJson(urlSwagger)


# print(swaggerResponse)

pathsList = getApisName(swaggerResponse)
print("---")
print(pathsList)


