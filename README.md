Personal Website
================
This is the repository containing the content for my personal website and the tools used to build it.
The content is written in Markdown and is converted to HTML using a custom static site generator using GNU Make and Python.

## Building
The project is built using GNU Make.
Currently, only building on Unix-style systems is supported as writing cross-platform Makefiles is a pain.
Building requires the following to be installed:
- [Python >=3.8](https://www.python.org/) - for build scripts
- [Poetry](https://python-poetry.org/) - for managing Python dependencies
- [ImageMagick convert](https://imagemagick.org/index.php) - for automatic image resizing

Building requires that the Poetry virtual environment be active.
This can be done by running `poetry shell` in the ``build_scripts`` directory.
Then to build, simply run `make` in the project's root directory.
Similarly, the project can be cleaned up by running `make clean`.

The project has additional dependencies that are installed by Poetry:
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) - for templating
- [Python-Markdown](https://python-markdown.github.io/) - for converting Markdown to HTML
- [pytest](https://docs.pytest.org/en/7.2.x/) - for testing

Some projects require Docker to build, so ensure your instance of Docker is running before building.
Some of the pages also utilize WebAssembly, and must be hosted on a server as they cannot be viewed locally due to CORS restrictions.