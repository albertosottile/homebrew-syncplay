#!/usr/bin/env python3

import glob
import json
import os

filename = glob.glob('*.json')[0]

f = open(filename, 'r')
data = json.load(f)

for formula in data.keys():
    tags = data[formula]['bottle']['tags']
    for osName in tags.keys():
        localName = tags[osName]['local_filename']
        remoteName = "../" + tags[osName]['filename']
        print(("Bottling {} for {}: renaming {} to {}").format(formula, osName, localName, remoteName))
        os.rename(localName, remoteName)
