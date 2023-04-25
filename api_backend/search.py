

def plainSearch(query: str, es):
    json = {"papers": [{
            "id": 1,
            "title": "Book 1",
            "date": 2001,
            "abstract": "This is a book",
            "authors": ["a1", "a2"],
            "link": "https://aclanthology.org",
            "conf": "acl"
    }, {
            "id": 2,
            "title": "Book 2",
            "date": 2000,
            "abstract": "This is another book",
            "authors": ["a2", "a3"],
            "link": "https://aclanthology.org",
            "conf": "acl"
    }], "authors": [{
            "name": "A 1",
            "url": "https://aclanthology.org",
            "papers": {"Book 1":"1"}
    }, {
            "name": "A 2",
            "url": "https://aclanthology.org",
            "papers": {"Book 1":"https://aclanthology.org", "Book 2": "https://aclanthology.org"}
    }]}
    return json