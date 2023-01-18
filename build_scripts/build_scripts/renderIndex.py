import sys
from jinja2 import Environment, FileSystemLoader

from build_scripts import TEMPLATE_DIR, SITE_DIR, pages

if __name__ == "__main__":

    env = Environment(loader=FileSystemLoader(["/", TEMPLATE_DIR, SITE_DIR]))
    template = env.get_template(sys.argv[1])
    output = template.render(navigation=pages.get_navigation())

    # to save the results
    with open(sys.argv[2], "w") as f:
        f.write(output)