import sys

import markdown

if __name__ == "__main__":
    markdown.markdownFromFile(input=sys.argv[1], output=sys.argv[2], extensions=['md_in_html'])