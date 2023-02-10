
PAGE_ABS_ID := $(call get_abs_id,$(PAGE_ID))
PAGE_PRE_DIR := $(dir $(PAGE_ABS_ID))

PAGE_MD = $(PAGE_ID).md
PAGE_J2 := $(SITE_DIR)/$(PAGE_ABS_ID).j2
PAGE_TEMPLATE_J2 := $(TEMPLATE_DIR)/page.j2
PAGE_HTML := $(BUILD_DIR)/$(PAGE_ABS_ID).html
PAGE_JSON := $(PAGE_ID).json
SUBPAGES := $(call get_pages,$(PAGE_ID))
SUBPAGES_JSON := $(addsuffix .json,$(SUBPAGES))
PAGE_DEPS := $(PAGE_J2) $(PAGE_TEMPLATE_J2) $(addprefix $(TEMPLATE_DIR)/,head.j2 header.j2 footer.j2) $(PAGE_JSON) $(CONTENT_JSON) $(SUBPAGES_JSON)

PAGE_J2_DIR := $(SITE_DIR)/$(PAGE_PRE_DIR)
PAGE_HTML_DIR := $(BUILD_DIR)/$(PAGE_PRE_DIR)

all: $(PAGE_HTML)

.PHONY: all clean

# Use jinja2 to build the html for this page
$(PAGE_HTML):  $(PAGE_DEPS) $(RENDER_DEPS) | $(PAGE_HTML_DIR)
	$(RENDER) $(PAGE_ID) $(PAGE_TEMPLATE_J2) $(PAGE_HTML)

# Convert markdown into html input to jinja2
$(PAGE_J2): $(PAGE_MD) $(MARKDOWN_DEPS) | $(PAGE_J2_DIR)
	$(MARKDOWN) $(PAGE_MD) $(PAGE_J2)

# Make directory if needed
$(PAGE_J2_DIR) $(PAGE_HTML_DIR): 
	mkdir -p $@

# Recursively build child pages
include $(CONTENT_DIR)/recurse.mak