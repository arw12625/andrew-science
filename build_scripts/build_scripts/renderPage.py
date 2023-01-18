import sys
from jinja2 import Environment, FileSystemLoader

from build_scripts import TEMPLATE_DIR, SITE_DIR, pages, posts

if __name__ == "__main__":
    """
    Render a page template .j2 to a .html file using Jinja2
    """
    
    page_id = sys.argv[1]
    page_info = pages.augment_page_info(pages.read_page_info(page_id))
    
    env = Environment(loader=FileSystemLoader(["/", TEMPLATE_DIR, SITE_DIR]))
    template = env.get_template(sys.argv[2])
    output = template.render(page_info=page_info,
                             navigation=pages.get_navigation())

    # to save the results
    with open(sys.argv[3], "w") as f:
        f.write(output)