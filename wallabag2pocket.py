from wallabag_api.wallabag import Wallabag
from pocket import Pocket, PocketException
import os

params = {'username': os.environ['WALLABAG_USER'],
          'password': os.environ['WALLABAG_PASS'],
          'client_id': os.environ['WALLABAG_CLIENT'],
          'client_secret': os.environ['WALLABAG_SECRET'],
          'host': os.environ['WALLABAG_HOST']}

token = Wallabag.get_token(**params)
wb = Wallabag(params['host'], token, params['client_id'], params['client_secret'])
entries = wb.get_entries()

urls = []
while entries['page'] <= entries['pages']:
    for item in entries['_embedded']['items']:
        urls.append(item['url'])
    entries = wb.get_entries(page = entries['page'] + 1)

print(len(urls), "urls fetched from wallabag")

p = Pocket( consumer_key=os.environ['POCKET_KEY'], access_token=os.environ['POCKET_TOKEN'])

for i, url in enumerate(urls):
    print(i, url)
    p.add(url)
