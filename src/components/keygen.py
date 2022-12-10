import rsa
import json
import zlib

hh = [200, 800, 1600, 3200]
d = {}
for i in range(20):
    keys = {}
    for j in hh:
        publicKey, privateKey = rsa.newkeys(j)
        keys[j] = [publicKey.save_pkcs1().decode('utf8'), privateKey.save_pkcs1().decode('utf8')]
        # keys[j] = [publicKey, privateKey]
    d[i] = keys
    print(i)
fp  = open("bipinkeysFinal.json","a")
json.dump(d,fp)
