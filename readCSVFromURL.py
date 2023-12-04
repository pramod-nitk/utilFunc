import requests
from io import StringIO
def csvFromURL()
  url = ""
  headers = {"User=Agent": "Mozilla/5.0 (Macintish; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
  req = requests.get(url, headers=headers)
  data = StringIO(req.text)
  return pd.read_csv(data)
