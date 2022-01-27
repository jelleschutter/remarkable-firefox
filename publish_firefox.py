import os
from helper import readJson, generateToken, checkResponse
import requests
import shutil

tmp_dir = './tmp'

# load manifest
print('Loading manifest...')
manifest = readJson(tmp_dir + '/firefox_addon/manifest.json')
print('Loaded manifest.')

# to zip
print('Zipping Fiefox AddOn...')
shutil.make_archive(tmp_dir + '/firefox_addon', 'zip', tmp_dir + '/firefox_addon/')
print('Zipped Firefox AddOn.')

# get addon info
uuid = manifest['browser_specific_settings']['gecko']['id']
version = manifest['version']

# get token
token = generateToken(os.environ['MOZILLA_API_KEY'], os.environ['MOZILLA_API_SECRET'])

# check if version exists
print('Checking if version exists...')
r = requests.get(f'https://addons.mozilla.org/api/v5/addons/addon/{uuid}/versions/', headers={'Authorization': f'JWT {token}'})
checkResponse(r)
version_result = r.json()
previous_versions = [v['version'] for v in version_result['results']]

if not version in previous_versions:
  print('Version does not exist.')

  # upload new version
  print('Uploading new version...')
  files = {'upload': open(tmp_dir + '/firefox_addon.zip', 'rb')}
  r = requests.post(f'https://addons.mozilla.org/api/v5/addons/{uuid}/versions/{version}', headers={'Authorization': f'JWT {token}'}, files=files)
  checkResponse(r)
  print('Uploaded new version:')
  print(r.text)
else:
  print('Version already exists.')