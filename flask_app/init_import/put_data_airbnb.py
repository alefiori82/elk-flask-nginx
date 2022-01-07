import json 
from elasticsearch import Elasticsearch

es = Elasticsearch('elasticsearch', port=9200, http_auth=('elastic', 'changeme'))

''' Reading JSON file '''
fr = open("airbnb.json", "r", encoding="utf-8")
text = fr.read()
fr.close()
text.strip()
lines = text.split("\n")

''' Creating required index '''
create_index = es.indices.create(index='airbnb', ignore=400)
delete_index = es.indices.delete(index='airbnb', ignore=[400, 404])

for l in lines:
    try:
        if l != "":
            jd = json.loads(l)
            ''' Retrieving required info '''


            d = {}
            d["name"] = jd["name"]
            d["summary"] = jd["summary"]
            d["description"] = jd["description"]
            d["amenities"] = jd["amenities"]
            d["url"] = jd["listing_url"]
            d["city"] = jd["address"]["market"]
            d["price"] = jd["price"]


            res = es.index(index="airbnb", body=d)

    except Exception as e:
        print (e)
