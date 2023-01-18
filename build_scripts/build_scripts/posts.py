import os.path
import shutil 
from datetime import datetime
import json

from build_scripts import BASE_DIR, SITE_DIR, pages


def post_template(id):
    return id + ".j2"
    #return os.path.join(SITE_DIR, id + ".j2")
    

def post_href(id):
    return pages.get_href(id)


def post_dir(page_id, id):
    return os.path.join(pages.page_dir(page_id), id)
    
    
def post_info_file(page_id, id):
    return os.path.join(post_dir(page_id, id), id + ".json")


def read_post_info(page_id, id):
    with open(post_info_file(page_id, id), "r") as f:
        return json.load(f)


def write_post_info(page_id, id, post_info):
    with open(post_info_file(page_id, id), "w") as f:
        json.dump(post_info, f, indent=4, sort_keys=True, default=str)


def augment_post_info(post_info):
    post_id = post_info['id']
    post_info['template_file'] = post_template(post_id)
    post_info['href'] = post_href(post_id)
    return post_info


def create_post(page_id, id, title, date=None):
    dir = post_dir(page_id, id)
    if(os.path.exists(dir)):
        raise ValueError("A post with the same id already exists.")
    os.mkdir(dir)
    
    post_info = {}
    
    post_info["id"] = id
    post_info["title"] = title
    
    if date is None:
        date = datetime.now()
    post_info["creation_date"] = date
    post_info["last_edit_date"] = date
    
    write_post_info(page_id, id, post_info)
    
    page_info = pages.read_page_info(page_id)
    page_info["posts"].append(id)
    pages.write_page_info(page_id, page_info)
    
    
def rename_post(page_id, id, new_title):
    
    post_info = read_post_info(page_id, id)
    
    post_info["title"] = new_title
    post_info["last_edit_date"] = date = datetime.now()
    
    write_post_info(page_id, id, post_info)
    
    
def move_post(page_id, id, new_page_id, new_id=None):
    
    post_info = read_post_info(page_id, id)
    
    if new_id is None:
        new_id = id
        
    source_dir = post_dir(page_id, id)
    dest_dir = post_dir(new_page_id, new_id)
    shutil.move(source, destination)
    
    post_info["id"] = new_id
    post_info["last_edit_date"] = datetime.now()
    
    write_post_info(new_page_id, new_id, post_info)
    
    page_info = pages.read_page_info(page_id)
    page_info["posts"].remove(id)
    pages.write_page_info(page_id, page_info)
    
    new_page_info = pages.read_page_info(new_page_id)
    new_page_info["posts"].append(id)
    pages.write_page_info(new_page_id, new_page_info)
    