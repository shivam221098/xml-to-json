import requests
from bs4 import BeautifulSoup

"""request = requests.get("https://api.polygon.io/v2/aggs/ticker/SPLK/range/1/hour/2020-06-01/2020-06-17?&apiKey=84unE7uySSqmHONRBQ1fNrQ8Bx1aEqzK").json()

print(request)"""

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        }

payload = {
    "weblogin_netid": "mschrier@uw.edu",
    "weblogin_password": "Mountrainier1!" 
}
with requests.Session() as session:
    #post = session.post("https://idp.u.washington.edu/idp/profile/SAML2/Redirect/SSO;jsessionid=304437847AB32422EE12564084BD5C05.idp05?execution=e1s1", data=payload)
    r = session.get("https://uw.joinhandshake.com/jobs/4408854?ref=open-in-new-tab&search_id=dcefec24-5252-4ee2-9871-15b8f06b32d5")
    soup = BeautifulSoup(r.content, "html.parser")
    link = soup.find_all("a")
    for a in link:
        if len(a['href']) > 50:
            post = session.post(a['href'], data=payload, headers=headers)
            r = r = session.get("https://uw.joinhandshake.com/jobs/4408854?ref=open-in-new-tab&search_id=dcefec24-5252-4ee2-9871-15b8f06b32d5")
            soup = BeautifulSoup(r.content, "html.parser")
            print(soup)
            print(soup.prettify())