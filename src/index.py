# -*- coding: utf8 -*-

import main
import random
import json
def main_handler(event, context):

    k = "k did not changed"
    c = "c did not changed"
    b = "b did not changed"
    insertStatus = "err -- did nothing"
    contenShow = ""
    find_result = "did not get from server"

    try:
        qS = event.get("queryString")
        b = qS.get("method")
        if(b == "0"):
            find_result = main.get_all()
            for oneItem in find_result:
                contenShow += "==>"
                contenShow += oneItem.get("data").get("content")
                contenShow += "\n"  
        elif(b == "1"):
            contenShow = "not find but insert"
            try:
                c = qS.get("content")
                if(c):
                    main.insert_data(c)
                    insertStatus = "successfuly inserted"
            except:
                statusCode = "fata err, wrong spelling API"
        elif(b == "3"):
            contenShow = "successfully deleted"
            try:
                c = qS.get("content")
                if(c):
                    contenShow = main.delete_item(c)
            except:
                contenShow = "delete fata err"
        elif(b == "2"):
            try:
                find_result = main.get_all()
                n = find_result.count()
                n = random.randint(0,n)
                i = 0
                for oneItem in find_result:
                    if i == n:
                        contenShow = oneItem.get("data").get("content")
                    i += 1
            except:
                contenShow = "method2 error"
    except:
            b = "b did not geted"

    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps({"qS":qS,"insertStatus":insertStatus,"c":c,"b":b,"contenshow":contenShow})
    }