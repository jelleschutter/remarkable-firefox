# reMarkable for Firefox ([Download](https://addons.mozilla.org/en-GB/firefox/addon/unofficial-remarkable/))
This repo converts the offical [reMarkable Chrome Extension](https://chrome.google.com/webstore/detail/read-on-remarkable/bfhkfdnddlhfippjbflipboognpdpoeh) into a Firefox AddOn published [here](https://addons.mozilla.org/en-GB/firefox/addon/unofficial-remarkable/) under the name "Unofficial reMarkable".

## Process
The process happens in 3 steps:
### Step 1: Download Chrome Extension
```shell
python ./download_chrome.py
```
This step downloads the current version of the Chrome Extension.

### Step 2: Convert Chrome Extension to Firefox AddOn
```shell
python ./chrome_to_firefox.py
```
This step contains the main logic for converting the Chrome Extension to the Firefox AddOn.
1. Change the format of options in the manifest.json to the format required by Firefox.
2. Map the `chrome` variable to the `browser` variable in Firefox.

### Step 3: Publish the Firefox AddOn
```shell
python ./publish_firefox.py
```
This step checks wether the current version of the AddOn has already published to Mozilla. If not it uploads the new version.
