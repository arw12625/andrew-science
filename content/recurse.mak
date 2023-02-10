PAGES := $(call get_pages,$(PAGE_ID))
CLEAN_PAGES := $(addprefix clean/, $(PAGES))

all: $(PAGES)
clean: $(CLEAN_PAGES)
.PHONY: $(PAGES) $(CLEAN_PAGES)

# Recursively make the list of pages listed in the current page's info file
# The Makefile to run is read from the page's info file
# If none is specified, it is assumed a custom Makefile is present in the page directory
$(PAGES):
	$(MAKE) -C $(dir $@) $(call get_page_make_opt,$@) \
	PAGE_ID=$(notdir $@)

# Recursively clean
$(CLEAN_PAGES): clean/% :
	$(MAKE) -C $(dir $%) $(call get_page_make_opt,$%) \
	PAGE_ID=$(notdir $%) clean