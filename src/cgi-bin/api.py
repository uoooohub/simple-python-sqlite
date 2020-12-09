#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import time
import json
import cgi

form = cgi.FieldStorage()

def _res(s, **keywords ):
    d={"status":s}
    d.update(keywords)
    return d

print("Content-type: application/json")
print("\n\n")
try:
    apiName = form['apiName']

    if not apiName:
        print(json.dumps(_res(500,msg="non apiName")))
        exit()

    # update aikotoba list
    if apiName.value == 'get':
        import sqlite3
        conn = sqlite3.connect('/code/data/example.db')
        c = conn.cursor()
        c.execute("select * from articles")
        d = []
        for row in c:
            d.append(row.fetchone())
        conn.close()
        print(json.dumps(_res(200,msg="ok",data=d)))
    else:
        print( json.dumps(_res(500,error="non apiName.value")) )
    exit()

except Exception as err:
    print(_res(500,error=err))
    exit()

exit()