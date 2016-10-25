.PHONY: build dev install publish clean

dev:
	@echo "[i] Installing requirements..."
	@pip install --upgrade -r ./requirements/development.txt

install:
	@echo "[i] Installing..."
	@python setup.py install

publish: clean build
	@echo "[i] Publishing..."
	@twine upload dist/*

build: dev
	@echo "[i] Building..."
	@python setup.py sdist bdist_wheel

clean:
	@echo "[i] Cleaning up..."
	rm -rf build dist pepper8.egg-info
	@echo "[i] Removed build and distribution files."
