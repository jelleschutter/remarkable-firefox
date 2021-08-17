from helper import copyDir, readJson, saveJson, rmDir, encloseText
import os

rmDir('./firefox_addon/')
copyDir('./chrome_addon/', './firefox_addon/')

rmDir('./firefox_addon/_metadata/')

manifest = readJson('./firefox_addon/manifest.json')

manifest.pop('options_page')
manifest.pop('update_url')
manifest.pop('key')

manifest['background'] = { 'scripts': ['background.js'] }

manifest['options_ui'] = { 'page': 'options.html' }

manifest['permissions'] = [e for e in manifest['permissions'] if e != 'printerProvider']

manifest['browser_specific_settings'] = {
  'gecko': {
    'id': 'remarkable@schutter.xyz'
  }
}

saveJson('./firefox_addon/manifest.json', manifest)

for js_file in os.listdir('./firefox_addon/'):
  if js_file.endswith('.js'):
    encloseText(
      './firefox_addon/' + js_file,
      '(function(chrome) {\n',
      '\n})(browser);'
    )