import os
from helper import readJson, generateToken
import requests
import shutil

tmp_dir = './tmp'

# load manifest
manifest = readJson(tmp_dir + '/firefox_addon/manifest.json')

# to zip
shutil.make_archive(tmp_dir + '/firefox_addon', 'zip', tmp_dir + '/firefox_addon/')

# get addon info
uuid = manifest['browser_specific_settings']['gecko']['id']
version = manifest['version']

# get token
token = generateToken(os.environ['MOZILLA_API_KEY'], os.environ['MOZILLA_API_SECRET'])

# check if version exists
r = requests.get(f'https://addons.mozilla.org/api/v5/addons/addon/{uuid}/versions/', headers={'Authorization': f'JWT {token}'})
version_result = r.json()
previous_versions = [v['version'] for v in version_result['results']]

if not version in previous_versions:
  # upload new version
  files = {'upload': open(tmp_dir + '/firefox_addon.zip', 'rb')}
  r = requests.post(f'https://addons.mozilla.org/api/v5/addons/{uuid}/versions/{version}', headers={'Authorization': f'JWT {token}'}, files=files)
  print(r.text)