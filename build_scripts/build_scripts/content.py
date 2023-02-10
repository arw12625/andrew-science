import os.path
import shutil 
from datetime import datetime
import json
from enum import Enum

from build_scripts import BASE_DIR, SITE_DIR


class PageType(Enum):
    PAGE = "page"
    POST = "post"
    

class Content:

    def __init__(self, id="content", dir=None):
        self.id = id
        if dir is None:
            dir = os.path.join(BASE_DIR, id)
        self.dir = dir
        self.url_prefix = "/"
        
    def info_file(self):
        return os.path.join(self.dir, self.id + ".json")
    
    def get_info(self):
        return read_json_info(self.info_file())
    
    def set_info(self, info):
        return write_json_info(self.info_file(), info)
    
    def page_abs_id(self, id):
        return os.path.relpath(os.path.join(os.getcwd(), id), self.dir)

    def page_rel_abs_id(self, id):
        print("HELLO", id, os.path.relpath(os.path.join(self.dir,id)), os.path.relpath(os.path.join(os.getcwd(), os.path.relpath(os.path.join(self.dir,id))), self.dir))
        return os.path.relpath(os.path.join(self.dir,id))
        
    def page_rel_id(self, id, start=None):
        return os.path.relpath(id, start)
        
    def page_info_file(self, id):
        return id + ".json"
    
    def get_page_info(self, id):
        return read_json_info(self.page_info_file(id))
    
    def set_page_info(self, id, info):
        return write_json_info(self.page_info_file(), info)
    
    def get_page_template(self, id):
        #return os.path.join(SITE_DIR, self.page_abs_id(id) + ".j2")
        return self.page_abs_id(id) + ".j2"
    
    def get_page_url(self, id):
        return os.path.join(self.url_prefix, self.page_abs_id(id)+".html")

        
    def create_page(self, id, title, date=None, page_type=PageType.PAGE, navigable=False, parent_id=None):
        
        info_file = self.page_info_file(id)
        if(os.path.exists(info_file)):
            raise ValueError("A page with the same id already exists.")        
        dir = os.path.dirname(info_file)
        os.makedirs(dir, exist_ok=True)
        
        page_info = {}
        
        page_info["id"] = id
        page_info["title"] = title
        page_info["pages"] = []
        
        if date is None:
            date = datetime.now()
        page_info["creation_date"] = date
        page_info["last_edit_date"] = date
        
        page_info["type"] = page_type
        
        self.set_page_info(id, page_info)
        
        
        content_info = self.get_info()
        if navigable:
            assert renderable
            content_info["navigable"].append(id)
        write_content_info(content_info)
        
        
        if parent_id is not None:
            parent_info = self.get_page_info(parent_id)
            parent_info["pages"].append(self.page_rel_id(id, parent_id))
            self.set_page_info(parent_id, parent_info)
                
    def retitle_page(self, id, new_title):
        
        page_info = self.get_page_info(id)
        
        page_info["title"] = new_title
        page_info["last_edit_date"] = datetime.now()
        
        self.set_page_info(id, page_info)
        

def create_content(id="content"):
    content = Content(id)
    info = {"pages":[], "navigable":[]}
    content.set_info(info)
    return content
    
    

def read_json_info(path):
    with open(path, "r") as f:
        return json.load(f)
        

def write_json_info(path, info_dic):
    with open(path, "w") as f:
        json.dump(info_dic, f, indent=4, sort_keys=True, default=str)