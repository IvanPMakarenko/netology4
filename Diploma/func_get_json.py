import os.path
import codecs
import json
from pprint import pprint

def create_json_file(group_dict):
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    with open('groups.txt', 'wb') as json_file:
        json.dump(group_dict, codecs.getwriter('utf-8')(json_file), ensure_ascii=False)
    print('Done!')

def load_json_file(name='groups.txt'):
    with open(name, 'rb') as json_file:
        book = json_file.read()
        f = json.loads(book)
        pprint(f)
