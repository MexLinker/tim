import pymongo

# the DB named todolist
# the Collection named todoList
# which is in the database named todoCluster

# connect to the database
client = pymongo.MongoClient("mongodb+srv://max:gao12345@todocluster.h6wo1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# get the database
mg_db = client.todoList

# get the collection
mg_col = mg_db.userGaoList

def insert_data(data):
    mg_col.insert_one({"method":1,"data":{"date":2019,"tag":"work","content":data,"done":"false"}})

def get_all():
    return mg_col.find({})

def delete_item(data):
    data = {"data":{"date":2019,"tag":"work","content":data,"done":"false"}}
    find_result = mg_col.find(data)
    find_content = ""
    for oneItem in find_result:
        find_content += oneItem.get("data").get("content")

    if(find_content != ""):
        mg_col.delete_one(data)
        return "delete success"
        print("delete the item successfluly")
    else:
        return "did not find the item"

print("load main.py success")