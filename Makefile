CC = gcc
BUILD_FILE_NAME = main
BUILD_DIR = build

create_dir:
ifeq ($(OS), Windows_NT)
	mkdir $(BUILD_DIR)
else
	mkdir -p $(BUILD_DIR)
endif

build: create_dir
	$(CC) main.c -o $(BUILD_DIR)/$(BUILD_FILE_NAME)

.PHONY: build create_dir