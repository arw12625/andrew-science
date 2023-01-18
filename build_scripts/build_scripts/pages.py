import os.path
import shutil 
from datetime import datetime
import json

from build_scripts import BASE_DIR, SITE_DIR, posts

navigable_pages = ["projects"]

def get_navigation():
    #return [{"caption":read_page_info(id)["title"], "href":page_href(id)} for id in read_content_info()["pages"]]
    return [{"caption":read_page_info(id)["title"], "href":page_href(id)} for id in navigable_pages]


def get_href(id):
    return id + ".html"


def content_dir():
    return os.path.join(BASE_DIR, "content")


def content_info_file():
    return os.path.join(content_dir(), "content.json")


def read_content_info():
    with open(content_info_file(), "r") as f:
        return json.load(f)


def write_content_info(content_info):
    with open(content_info_file(), "w") as f:
        json.dump(content_info, f, indent=4, sort_keys=True, default=str)



def page_template(id):
    return id + ".j2"
    #return os.path.join(SITE_DIR, id + ".j2")


def page_href(id):
    return get_href(id)
    

def page_dir(id):
    return os.path.join(content_dir(), id)
    
    
def page_info_file(id):
    return os.path.join(page_dir(id), id + ".json")


def read_page_info(id):
    with open(page_info_file(id), "r") as f:
        return json.load(f)


def write_page_info(id, page_info):
    with open(page_info_file(id), "w") as f:
        json.dump(page_info, f, indent=4, sort_keys=True, default=str)


def augment_page_info(page_info):
    page_id = page_info['id']
    page_info['template_file'] = page_template(page_id)
    page_info['href'] = page_href(page_id)
    page_info['post_infos'] = {post_id: posts.augment_post_info(posts.read_post_info(page_id, post_id))
                               for post_id in page_info["posts"]}
    return page_info


def create_page(id, title, date=None):
    dir = page_dir(id)
    if(os.path.exists(dir)):
        raise ValueError("A post with the same id already exists.")
    os.mkdir(dir)
    
    page_info = {}
    
    page_info["id"] = id
    page_info["title"] = title
    page_info["posts"] = []
    
    if date is None:
        date = datetime.now()
    page_info["creation_date"] = date
    page_info["last_edit_date"] = date
    
    write_page_info(id, page_info)
    
    content_info = read_content_info()
    content_info["pages"].append(id)
    write_content_info(content_info)
    
    
def rename_page(id, new_title):
    
    page_info = read_page_info(id)
    
    page_info["title"] = new_title
    page_info["last_edit_date"] = date = datetime.now()
    
    write_page_info(id, page_info)
    