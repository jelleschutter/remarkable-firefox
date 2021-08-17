import os
import json
import shutil

def rmDir(path):
  if os.path.exists(path):
    shutil.rmtree(path)

def copyDir(src, dst):
  if not os.path.exists(dst):
    os.makedirs(dst)
  for item in os.listdir(src):
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if os.path.isdir(s):
      copyDir(s, d)
    else:
      shutil.copy2(s, d)

def readJson(path):
  with open(path, 'r') as f:
    return json.load(f)

def saveJson(path, data):
  with open(path, 'w') as f:
    json.dump(data, f, indent=3)

def encloseText(path, prefix, suffix):
  with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
  with open(path, 'w', encoding='utf-8') as f:
    f.write(prefix)
    f.write(content)
    f.write(suffix)