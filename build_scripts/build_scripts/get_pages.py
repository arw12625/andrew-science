from build_scripts import pages

if __name__ == "__main__":
    print(" ".join(pages.read_content_info()["pages"]))