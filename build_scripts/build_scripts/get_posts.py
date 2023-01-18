import sys

from build_scripts import pages

if __name__ == "__main__":
    print(" ".join(pages.read_page_info(sys.argv[1])["posts"]))