#import requests
import requests.packages.urllib3

if __name__ == '__main__':
    reply = requests.requests.packages.urllib3.get("http://t2shared.herokuapp.com/interests/")
    print reply.status_code
