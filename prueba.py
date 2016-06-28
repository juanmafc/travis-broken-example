import requests
#import requests.packages.urllib3
import utilities

if __name__ == '__main__':
    utilities.printearInicio()
    reply = requests.get("http://t2shared.herokuapp.com/interests/")
    print reply.status_code
