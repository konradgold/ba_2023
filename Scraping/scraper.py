import pickle
import warnings
import elasticsearch


class Scraper:

    already_done = []
    def __int__(self, filename):
        self.filename = filename
        if not self.filename is None:
            with open(self.filename) as f:
                self.already_done = pickle.load(f)
        es_host = "http://localhost:9200"
        es_user = "elastic"
        es_password = "1234"


        es = elasticsearch.Elasticsearch(
            hosts=es_host,  # "http://localhost:9200"
            basic_auth=(es_user, es_password)  # credentials for basic authentication
        )

    def __del__(self):
        with open(self.filename, 'w') as f:
            pickle.dump(self.already_done, f)

    def scrape_fromlink(self, link, update=False):
        if link in self.already_done and not update:
            warnings.WarningMessage("Site has been scraped already.")
            return None


        self.already_done.append(link)

        with open(self.filename, 'w') as f:
            pickle.dump(self.already_done, f)

