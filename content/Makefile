export CONTENT_DIR := $(CURDIR)

export TEMPLATE_DIR := $(BASE_DIR)/templates
export SITE_DIR := $(BASE_DIR)/site

# Content to convert to HTML
CONTENT_PAGES := $(shell $(PYTHON_COMMAND) $(BUILD_SCRIPTS)/get_pages.py)
INDEX_J2 := $(TEMPLATE_DIR)/index.j2
INDEX_HTML := $(BUILD_DIR)/index.html
INDEX_DEPS := $(INDEX_J2) $(addprefix $(TEMPLATE_DIR)/,head.j2 header.j2 footer.j2 contacts.j2)

export BUILD_SCRIPTS_DEPS := $(addprefix $(BUILD_SCRIPTS)/,pages.py posts.py)

RENDER_INDEX := $(PYTHON_COMMAND) $(BUILD_SCRIPTS)/renderIndex.py
RENDER_INDEX_DEPS := $(BUILD_SCRIPTS)/renderIndex.py $(BUILD_SCRIPTS_DEPS)

export MARKDOWN := $(PYTHON_COMMAND) $(BUILD_SCRIPTS)/markdownContent.py
export MARKDOWN_DEPS := $(BUILD_SCRIPTS)/markdownContent.py

all: $(CONTENT_PAGES) $(INDEX_HTML)

.PHONY: all clean $(CONTENT_PAGES) $(SITE_DIR)

clean:
	@echo Cleaning content
	rm -rf $(SITE_DIR)
ifneq ("$(wildcard %/Makefile)","")
	for page in $(CONTENT_PAGES); do \
	$(MAKE) -C $$page PAGE_ID=$$page clean; \
	done
else
	for page in $(CONTENT_PAGES); do \
	$(MAKE) -C $$page -f ../MakefilePage PAGE_ID=$$page clean; \
	done
endif

# Multiple recipes for creating each content page	
$(CONTENT_PAGES): % : | $(SITE_DIR)
ifneq ("$(wildcard %/Makefile)","")
# 1. Use Makefile present if present in page directory
	$(MAKE) -C $@ PAGE_ID=$@
else
# 2. Use default rule for pages. Convert markdown to html for the page and make child posts
	$(MAKE) -C $@ -f ../MakefilePage PAGE_ID=$@
endif

$(INDEX_HTML): $(INDEX_DEPS) $(RENDER_INDEX_DEPS)
	$(RENDER_INDEX) $(INDEX_J2) $(INDEX_HTML)

# Make site directory if needed to hold marked up files/templates
$(SITE_DIR):
	mkdir -p $@