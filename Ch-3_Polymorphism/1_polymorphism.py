class fetch_api:
    def fetch(self):
        print("Fetching data from API..")

class database_fetch:
    def fetch(self):
        print("Fetching data from database..")

class s3_fetch:
    def fetch(self):
        print("Fetching data from S3..")

obj = fetch_api()
obj.fetch()