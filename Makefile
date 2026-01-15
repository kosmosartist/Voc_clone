.PHONY: build clean

build:
	python3 tools/build.py

clean:
	rm -rf dist
