client = pymongo.MongoClient("mongodb://toanphan:toan123@ds235418.mlab.com:35418/nps_trial",connectTimeoutMS=30000)
data = json.loads(open('/Users/h/national_park_scrapy/nps_tripadvisor/nps_tripadvisor/spiders/nps_urls.json').read())
db =client.get_database("nps_trial")
user = db.user_db
for item in data:
    user.insert_one(item)
