import requests
import json

def toJson(urlSwagger):

    print(urlSwagger)

    if urlSwagger.find("swagger.json") != -1:
        print("this file is swagger.json")
         
        r = requests.get(urlSwagger)
        swaggerResponse = r.json()
        swaggerResponse["isSwaggerJson"] = True

   
    elif urlSwagger.find("swagger-ui-init.js") != -1:

        print("this is one swagger-ui-init.js")

        r = requests.get(urlSwagger)
        r = r.text[r.text.find("var options")+ 14:r.text.find("url = options.swaggerUrl || url")-4]

        swaggerResponse = json.loads(r)
        swaggerResponse = swaggerResponse["swaggerDoc"]
        swaggerResponse["isSwaggerJson"]= False


    else:
        swaggerResponse = {}
        print("The swagger URL is incompatible ")


    return swaggerResponse


def getApisName(swaggerResponse):
    
    pathsList =  []
    for key in swaggerResponse['paths']:
        pathsList.append(key)

    return pathsList








        


