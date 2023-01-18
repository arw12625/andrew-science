# Python for running build scripts
export PYTHON_COMMAND := python
export BASE_DIR := $(CURDIR)
export BUILD_SCRIPTS := $(BASE_DIR)/build_scripts/build_scripts
export BUILD_DIR := $(BASE_DIR)/build

# Static files to be copied to the build directory
STATIC_DIRS_TO_COPY := images js
STATIC_DIR := $(BASE_DIR)/static
STATIC_DIRS := $(addprefix $(STATIC_DIR)/,$(STATIC_DIRS_TO_COPY))
STATIC_FILES := $(wildcard $(addsuffix /*,$(STATIC_DIRS)))
BUILD_STATIC_DIRS := $(addprefix $(BUILD_DIR)/,$(STATIC_DIRS_TO_COPY))
BUILD_STATIC_FILES := $(patsubst $(STATIC_DIR)/%,$(BUILD_DIR)/%,$(STATIC_FILES))

# Sass style files and partials for css targets
SASS_DIR := $(BASE_DIR)/sass
SASS_FILES := $(wildcard $(SASS_DIR)/*.scss)
SASS_PARTIALS := $(filter $(wildcard $(SASS_DIR)/_*),$(SASS_FILES))
SASS_TOTALS := $(filter-out $(SASS_PARTIALS),$(SASS_FILES))
CSS_DIR := $(BUILD_DIR)/css
CSS_FILES := $(patsubst $(SASS_DIR)/%.scss,$(CSS_DIR)/%.css,$(SASS_TOTALS))
STYLE_DIR := $(CSS_DIR)

# Automatically create favicon from image
CONVERT_IMG := convert
FAVICON_ICO := $(BUILD_DIR)/favicon.ico
FAVICON_IMG := $(BASE_DIR)/res/favicon.png

all: $(BUILD_STATIC_FILES) $(CSS_FILES) content $(FAVICON_ICO)

# Recursively clean
clean:
	rm -rf $(BUILD_DIR)
	$(MAKE) -C content clean

.PHONY: all clean $(BUILD_DIR) $(BUILD_STATIC_DIRS) $(STYLE_DIR) content check upload pytest

# Only use sass to compile non-partial files
$(CSS_FILES): $(CSS_DIR)/%.css : $(SASS_DIR)/%.scss $(SASS_PARTIALS) | $(STYLE_DIR)
	sass $< $@

# Copy static files to build directory if out-of-date
$(BUILD_STATIC_FILES): $(BUILD_DIR)/%: $(STATIC_DIR)/% | $(BUILD_STATIC_DIRS)
	cp $< $@

# Recursively make content
content: | $(BUILD_DIR)
	$(MAKE) -C content

# Make build directories if needed
$(BUILD_DIR):
	mkdir -p $@

$(BUILD_STATIC_DIRS): | $(BUILD_DIR)
	mkdir -p $@

$(STYLE_DIR): | $(BUILD_DIR)
	mkdir -p $@

# Create favicon from image
$(FAVICON_ICO): $(FAVICON_IMG) | $(BUILD_DIR)
	$(CONVERT_IMG) $<  -background white \
	\( -clone 0 -resize 16x16 -extent 16x16 \) \
	\( -clone 0 -resize 32x32 -extent 32x32 \) \
	\( -clone 0 -resize 48x48 -extent 48x48 \) \
	\( -clone 0 -resize 64x64 -extent 64x64 \) \
	-delete 0 -alpha off -colors 256 $@
	
check: pytest

pytest:
	cd $(BUILD_SCRIPTS)/..
	poetry run pytest
	
upload:
	@echo UPLOAD NOT IMPLEMENTED
	# use sftp to upload to site