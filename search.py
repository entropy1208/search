#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 entro <entropy1208@yahoo.co.in>
#
# Distributed under terms of the Psycho license.

import pymongo

try:
    client = pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
    print "Could not clientect to MongoDB: %s" % e
db = client.indexes
res = db.indexes1

def count_keywords(doc, keywords):
    count = 0
    keywords = keywords.split() 
    keywords = map(str.lower, keywords)
    for j in keywords:
        for i in ['title', 'stars', 'director']:
            k = map(unicode.lower, doc[i])
            for m in k:
                if (j in m):
                    count += 1    
    return count

keywords = raw_input("Enter the keywords:")

res1 = db.test_collection
for i in res.find():
   m = {}
   m['count'] = count_keywords(i, keywords)
   m['doc_id'] = i['_id']
   res1.insert_one(m)

m = filter(lambda s : s['count'] > 0, res1.find())

if (len(m) > 0):
    for i in m:
       r = res.find_one({"_id":i['doc_id']})
       for j in r:
           if (j != "_id"):
               print ("%s : %s") % (j, r[j])
       print("\n")
else:
    ('No results were found!')
db.test_collection.drop()
