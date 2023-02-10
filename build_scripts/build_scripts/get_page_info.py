import sys
from build_scripts.content import Content

if __name__ == "__main__":
    content = Content()
    print(content.get_page_info(sys.argv[1]).get(sys.argv[2], ""))