import sys
from build_scripts.content import Content

if __name__ == "__main__":
    content = Content()
    print(content.page_abs_id(sys.argv[1]))