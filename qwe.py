import requests
import lxml
import lxml.html


def test_x():
    x = requests.get(url='https://10.10.3.66:8443/MinsoprDocflow/', verify=False)
    tree = lxml.html.fromstring(x.text)
    title_elem = tree.cssselect('[id="kc-form-login"]')[0].attrib['action']
    print(title_elem)
    y = requests.post(url='http://sso.opencode.su/auth/realms/UnifiedAuthorizationSystem/protocol/openid-connect/token', data={'username': '2', 'password': '2', 'credentialId': '', 'clientId': "minsopr-app",
                                            'clientSecret': 'ef5768d3-8a52-4d2b-9054-37257052724a', 'grant_type':'password'}, verify=False,
                      allow_redirects=True)
    print(y)
    print(y.text)
    resp = requests.post(url='https://10.10.3.66:8443/MinsoprDocflow/docflow/storage/multiUpload?',
                         files={'file': open('load_file.doc', 'rb')}, verify=False)
    # print(resp.text)
