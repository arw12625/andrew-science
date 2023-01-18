import sys
from jinja2 import Environment, FileSystemLoader

from build_scripts import TEMPLATE_DIR, SITE_DIR, posts, pages

if __name__ == "__main__":
    """
    Render a post template .j2 to a .html file using Jinja2
    """

    page_id = sys.argv[1]
    post_id = sys.argv[2]
    post_info = posts.augment_post_info(posts.read_post_info(page_id, post_id))
    
    env = Environment(loader=FileSystemLoader(["/", TEMPLATE_DIR, SITE_DIR]))
    # TODO - add navigation (and maybe content data) as global in environment
    template = env.get_template(sys.argv[3])
    output = template.render(post_info=post_info,
                             navigation=pages.get_navigation())

    # to save the results
    with open(sys.argv[4], "w") as f:
        f.write(output)