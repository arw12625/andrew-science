import os, sys
from jinja2 import Environment, FileSystemLoader

from build_scripts import TEMPLATE_DIR, SITE_DIR
from build_scripts.content import Content

if __name__ == "__main__":
    """
    Render a page template .j2 to a .html file using Jinja2
    """
    content = Content()
    
    page_id = sys.argv[1]
    
    env = Environment(loader=FileSystemLoader(["/", TEMPLATE_DIR, SITE_DIR]))
    #template = env.get_template(content.get_page_template(page_id))
    template = env.get_template(sys.argv[2])
    
    output = template.render(page_id=page_id,
                             content=content)

    # to save the results
    with open(sys.argv[3], "w") as f:
        f.write(output)