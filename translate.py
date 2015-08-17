#!/usr/bin/env python
import json, os, sys, urllib, re 
urllib.urlretrieve("https://translate.yandex.net/api/v1.5/tr.json/getLangs?key=trnsl.1.1.20150817T175044Z.7a92ab24a4241451.f9616f7ec486a93d5152908fa30d878b7d748156&ui=en", 'languages.json')
file=open('languages.json')
langs=json.load(file)
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
if len(sys.argv) == 2:
    if sys.argv[1] in ["--languages", "-l"]:
        urllib.urlretrieve("https://translate.yandex.net/api/v1.5/tr.json/getLangs?key=trnsl.1.1.20150817T175044Z.7a92ab24a4241451.f9616f7ec486a93d5152908fa30d878b7d748156&ui=en", 'languages.json')
        file=open('languages.json')
        data=json.load(file)
        n = 0
        for key, value in data["langs"].items():
            print "%s [%s] " %(byteify(value), byteify(key)),
            n+=1
            if n == 4:
                print ""
                n = 0
if len(sys.argv) == 4:
    if len(sys.argv[2]) == 2 and len(sys.argv[3]) == 2:
        sourceLanguage = sys.argv[2]
        destinationLanguage = sys.argv[3]
        string = sys.argv[1]
        precall = "&lang=%s-%s&text=" %(sourceLanguage, destinationLanguage)
        mstring = string
        mstring.replace(" ", "+")
        call = precall + mstring
        urllib.urlretrieve("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20150817T175044Z.7a92ab24a4241451.f9616f7ec486a93d5152908fa30d878b7d748156%s" %call, 'translate.json')
        file=open('translate.json')
        data=json.load(file)
        print "%s [%s] --> %s [%s]" %(langs["langs"][sourceLanguage], sourceLanguage, langs["langs"][destinationLanguage], destinationLanguage)
        print data["text"][0].encode('utf-8')
    else:
        print "Usage: translate <text> <source lang> <destination lang>"
os.system('/bin/rm languages.json translate.json')
            