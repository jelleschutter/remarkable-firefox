import os
import requests
from struct import Struct
from zipfile import ZipFile

id = 'bfhkfdnddlhfippjbflipboognpdpoeh'
url = f'https://clients2.google.com/service/update2/crx?response=redirect&prodversion=92.0.4515.159&x=id%3D{id}%26installsource%3Dondemand%26uc&nacl_arch=x86-64&acceptformat=crx2,crx3'
tmp_dir = './tmp'
filename = tmp_dir + '/chrome_addon'

# create tmp dir
if not os.path.exists(tmp_dir):
  os.mkdir(tmp_dir)

# get crx file
print('Downloading Chrome Extension...')
r = requests.get(url=url, stream=True)
print('Downloaded Chrome Extension')

print('Saving crx...')
crx_filename = filename + '.crx'

chunk_size = 16 * 1024
dowloaded_bytes = 0
with open(crx_filename, 'wb') as fd:
  for chunk in r.iter_content(chunk_size):
    fd.write(chunk)
    dowloaded_bytes += len(chunk)
print('Saved crx')

# crx to zip file
print('Converting crx to zip...')
crx_struct = Struct('<4s2I')
zip_filename = filename + '.zip'

with open(crx_filename, 'rb') as fd:
  header = fd.read(12)
  magic, version, key_len = crx_struct.unpack(header)
  fd.seek(key_len, os.SEEK_CUR)

  with open(zip_filename, 'wb') as zip_fd:
    zip_fd.write(fd.read())
print('Converted crx to zip')

# extract zip file
print('Extracting zip file...')
zip = ZipFile(zip_filename)
zip.extractall('./tmp/chrome_addon/')
print('Extracted zip file')