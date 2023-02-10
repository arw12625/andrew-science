APP_REPO_URL := https://github.com/arw12625/Rayngler.git
APP_REPO := app_repo
APP_SCREEN_WIDTH = 640
APP_SCREEN_HEIGHT = 480

ifeq ($(BUILD_MODE),all)
HTML_DEPS := app
else
HTML_DEPS := 
endif

all: html

clean:
	rm -rf $(APP_REPO)

.PHONY: all app html clean update_repo

html: $(HTML_DEPS)
	$(MAKE) -f $(MAKEFILE_PAGE)

app: update_repo
	cd $(APP_REPO); \
	docker run --rm -v $$(pwd):/src emscripten/emsdk ./make_page.bash $(APP_SCREEN_WIDTH) $(APP_SCREEN_HEIGHT); \
	cp -r bin/index.html $(SITE_DIR)/$(POST_ID)_app.j2; \
	cp -r bin/js/*.js $(BUILD_DIR)/js; \
	cp -r bin/js/*.wasm $(BUILD_DIR)/js

update_repo: | $(APP_REPO)
	@cd $(APP_REPO) && git pull

$(APP_REPO):
	mkdir -p $@
	git clone $(APP_REPO_URL) $@