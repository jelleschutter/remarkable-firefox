from helper import copyDir, readJson, saveJson, rmDir
import os

tmp_dir = './tmp'

# create tmp dir
if not os.path.exists(tmp_dir):
  os.mkdir(tmp_dir)

# reset firefox to current chrome version
print('Resetting Firefox AddOn to current Chrome Extension...')
rmDir(tmp_dir + '/firefox_addon/')
copyDir(tmp_dir + '/chrome_addon/', tmp_dir + '/firefox_addon/')
print('Firefox AddOn resetted.')

print('Apply required changes to Firefox AddOn.')
# remove unnecessary files
rmDir(tmp_dir + '/firefox_addon/_metadata/')

# load manifest
manifest = readJson(tmp_dir + '/firefox_addon/manifest.json')

# remove unnecessary keys
manifest.pop('options_page')
manifest.pop('update_url')
if 'key' in manifest:
  manifest.pop('key')

# update incompatible keys
manifest['background'] = { 'scripts': ['background.js'] }
manifest['options_ui'] = { 'page': 'options.html' }
manifest['permissions'] = [e for e in manifest['permissions'] if e != 'printerProvider']
manifest['browser_specific_settings'] = {
  'gecko': {
    'id': 'remarkable@schutter.xyz'
  }
}

# save updated manifest
saveJson(tmp_dir + '/firefox_addon/manifest.json', manifest)
print('Firefox AddOn fixed.')
