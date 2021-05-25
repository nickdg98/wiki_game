import requests
import string
import random

URL = "https://en.wikipedia.org/w/api.php"

NAMESPACES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 90, 91, 92, 93, 100, 101, 102, 103, 104, 105, 106, 107, 486, 487, 828, 829, 1198, 1199, 2300, 2301, 2302, 2303, 2600, 5500, 5501]

def get_random_page():
    apfrom = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    namespace = random.choice(NAMESPACES)
    aplimit = random.choice(range(5000,10000))
    PARAMS = {
            "action": "query",
            "format": "json",
            "list": "allpages",
            "apfrom": apfrom,
            "namespace": namespace,
            "aplimit": aplimit,
            "apminsizes": 1000000000000
    }
    S = requests.Session()
    R = S.get(url=URL, params=PARAMS)
    S.close()
    DATA = R.json()

    return id_name_class(DATA["query"]["allpages"][-1]["title"], DATA["query"]["allpages"][-1]['pageid'])

def get_popular_page():
    index = random.choice(range(1,250))
    POPULAR_URL = f"http://wikirank-2021.di.unimi.it/Q/?filter%5Btext%5D=Harmonic+centrality&filter%5Bselected%5D=true&filter%5Bvalue%5D=harmonic&view=list&pageSize=1&pageIndex={index}&type=harmonic&score=false"
    S = requests.Session()
    popular_json = S.get(url=POPULAR_URL).json()
    S.close()
    output = popular_json['list'].split("—")[0].split(".")[1:]

    return "".join(output).strip()

class id_name_class():
    def __init__(self, name, id):
        self.name = name
        self.id = id



        
        
