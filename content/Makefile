export CONTENT_DIR := $(CURDIR)

export TEMPLATE_DIR := $(BASE_DIR)/templates
export SITE_DIR := $(BASE_DIR)/site

export get_page_info = $$(shell $(PYTHON_COMMAND) $(BUILD_SCRIPTS)/get_page_info.py $$(1) $$(2))

export get_page_make = $$(strip $$(call get_page_info,$$(1),make))
export get_page_make_opt_tmp = $$(if $$(1), -f $(CONTENT_DIR)/$$(1).mak,)
export get_page_make_opt = $$(call get_page_make_opt_tmp,$$(call get_page_make,$$(1)))

export COMMA := ,
export SPACE := $() $()
export get_pages = $$(subst ',,$$(subst [,,$$(subst ],,$$(subst $$(COMMA),$$(SPACE),$$(call get_page_info,$$(1),pages)))))

export get_abs_id = $$(shell $$(PYTHON_COMMAND) $$(BUILD_SCRIPTS)/get_abs_id.py $$(1))

export BUILD_SCRIPTS_DEPS := $(addprefix $(BUILD_SCRIPTS)/,content.py)

export RENDER = $(PYTHON_COMMAND) $(BUILD_SCRIPTS)/render.py
export RENDER_DEPS := $(BUILD_SCRIPTS)/render.py $(BUILD_SCRIPTS_DEPS)

export MARKDOWN := $(PYTHON_COMMAND) $(BUILD_SCRIPTS)/markdownContent.py
export MARKDOWN_DEPS := $(BUILD_SCRIPTS)/markdownContent.py

export MAKEFILE_PAGE := $(CONTENT_DIR)/page.mak

export CONTENT_JSON := $(CONTENT_DIR)/content.json
PAGE_ID := content

all:
	$(MAKE) -f recurse.mak PAGE_ID=$(PAGE_ID)

clean:
	$(MAKE) -f recurse.mak PAGE_ID=$(PAGE_ID) clean

.PHONY: all clean

# Recursively build content
#include recurse.mak